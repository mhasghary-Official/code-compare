import subprocess
import time

def run_python(py_file, input_file, output_file, timeout=10):
    """Run Python code"""
    try:
        with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
            start = time.perf_counter()
            run_result = subprocess.run(
                ["python", py_file],
                stdin=fin,
                stdout=fout,
                timeout=timeout
            )
            end = time.perf_counter()
    except subprocess.TimeoutExpired:
        print("⏳ Python execution timed out (timeout)")
        return None, None
    except Exception as e:
        print(f"❌ Python execution error: {e}")
        return None, None

    if run_result.returncode != 0:
        print("❌ Python terminated with error.")
        return None, None

    return end - start, output_file
import subprocess
import os
import tempfile
import time
from pathlib import Path

def compile_and_run_cpp(cpp_file, input_file, output_file, timeout=100):
    """Compile and run C++ code"""
    exe_file = tempfile.NamedTemporaryFile(delete=False).name

    # Step 1: Compile
    try:
        compile_result = subprocess.run(
            ["clang++", "-O2", "-std=c++17", cpp_file, "-o", exe_file],
            capture_output=True,
            text=True,
            timeout=100
        )
        if compile_result.returncode != 0:
            print("❌ C++ Compilation Error:")
            print(compile_result.stderr)
            return None, None
    except FileNotFoundError:
        print("❌ g++ not found. Please install GCC.")
        return None, None

    # Step 2: Run
    try:
        with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
            start = time.perf_counter()
            run_result = subprocess.run(
                [exe_file],
                stdin=fin,
                stdout=fout,
                timeout=timeout
            )
            end = time.perf_counter()
    except subprocess.TimeoutExpired:
        print("⏳ C++ execution timed out (timeout)")
        return None, None
    except Exception as e:
        print(f"❌ C++ execution error: {e}")
        return None, None
    finally:
        # Clean up executable file
        if os.path.exists(exe_file):
            os.remove(exe_file)

    if run_result.returncode != 0:
        print("❌ C++ terminated with error.")
        return None, None

    return end - start, output_file
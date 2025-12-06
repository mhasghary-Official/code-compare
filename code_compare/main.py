import argparse
import os
import tempfile
from .runner.cpp_runner import compile_and_run_cpp
from .runner.py_runner import run_python
from .utils import generate_random_input, write_input_to_file, read_output_from_file

def main():
    parser = argparse.ArgumentParser(description="Compare C++ and Python code")
    parser.add_argument("--cpp", required=True, help="Path to C++ file")
    parser.add_argument("--py", required=True, help="Path to Python file")
    parser.add_argument("--size", type=int, default=1000, help="Number of inputs (default: 1000)")
    args = parser.parse_args()

    if not os.path.exists(args.cpp):
        print(f"❌ C++ file not found: {args.cpp}")
        return
    if not os.path.exists(args.py):
        print(f"❌ Python file not found: {args.py}")
        return

    # Step 1: Generate input
    print(f"🔄 Generating {args.size} random numbers...")
    input_data = generate_random_input(n=args.size)
    input_file = write_input_to_file(input_data, prefix="common_input")

    # Temporary output files
    cpp_out = tempfile.NamedTemporaryFile(delete=False).name
    py_out = tempfile.NamedTemporaryFile(delete=False).name

    # Step 2: Run C++
    print("⚙️ Compiling and running C++ code...")
    cpp_time, cpp_out_path = compile_and_run_cpp(args.cpp, input_file, cpp_out)
    if cpp_time is None:
        return

    # Step 3: Run Python
    print("🐍 Running Python code...")
    py_time, py_out_path = run_python(args.py, input_file, py_out)
    if py_time is None:
        return

    # Step 4: Compare outputs
    cpp_output = read_output_from_file(cpp_out_path)
    py_output = read_output_from_file(py_out_path)

    print("\n" + "="*50)
    if cpp_output == py_output:
        print("✅ Outputs are identical!")
    else:
        print("❌ Outputs are different!")
        print("   (Check output files for debugging)")

    # Step 5: Display execution times
    print(f"\n⏱️ Execution Time:")
    print(f"   - C++:   {cpp_time:.4f} seconds")
    print(f"   - Python: {py_time:.4f} seconds")
    if cpp_time > 0:
        ratio = py_time / cpp_time
        print(f"📊 Python ≈ {ratio:.1f}x slower than C++")

    # Clean up temporary files
    for f in [input_file, cpp_out_path, py_out_path]:
        if os.path.exists(f):
            os.remove(f)

def cli():
    main()
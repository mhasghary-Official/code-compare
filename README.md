# code-compare

**C++ vs Python Code Comparator**

A tool to compare execution times and outputs between C++ and Python implementations of the same algorithm.

**Features**

· Automatic compilation of C++ code using clang++
· Random input generation for testing
· Execution time measurement for both languages
· Output comparison to verify correctness
· Temporary file management - automatic cleanup

***Requirements***

**Python Dependencies**

· Python 3.8+
· No external Python packages required (uses only standard library)

**System Requirements**

· C++ Compiler: clang++ or g++ (clang++ is preferred)
· Python: Python 3.x interpreter

**Installation**

1. Clone or download this repository
2. Ensure your system has:
   · Python 3.x installed
   · A C++ compiler (clang++ or g++) installed and in PATH

**Project Structure**

```
project/
├── runner/
│   ├── cpp_runner.py    # C++ compilation and execution module
│   └── py_runner.py     # Python execution module
├── utils.py             # Utility functions for input/output handling
├── main.py              # Main comparison script
└── README.md            # This file
```

***Usage***

**Basic Comparison**

Run the comparison with default settings (1000 random numbers):

```bash
python main.py --cpp example.cpp --py example.py
```

**Custom Input Size**

Compare with a specific number of inputs:

```bash
python main.py --cpp example.cpp --py example.py --size 5000
```

**Example C++ and Python Files**

example.cpp (C++ implementation):

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    
    std::vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
        std::cin >> numbers[i];
    }
    
    // Example: Find maximum
    int max_val = *std::max_element(numbers.begin(), numbers.end());
    std::cout << max_val << std::endl;
    
    return 0;
}
```

example.py (Python implementation):

```python
import sys

def main():
    n = int(sys.stdin.readline())
    numbers = [int(sys.stdin.readline()) for _ in range(n)]
    
    # Example: Find maximum
    max_val = max(numbers)
    print(max_val)

if __name__ == "__main__" :
    main()
```

**Command Line Arguments**

Argument Description Default
--cpp Path to C++ source file Required
--py Path to Python source file Required
--size Number of random inputs to generate 1000

**Output Example**

```
🔄 Generating 1000 random numbers...
⚙️ Compiling and running C++ code...
🐍 Running Python code...

==================================================
✅ Outputs are identical!

⏱️ Execution Time:
   - C++:   0.0034 seconds
   - Python: 0.0121 seconds
📊 Python ≈ 3.6x slower than C++
```

**How It Works**

1. Input Generation: Creates random integer inputs using utils.generate_random_input()
2. C++ Execution:
   · Compiles C++ code with optimizations (-O2 -std=c++17)
   · Runs the executable with generated input
   · Measures execution time
3. Python Execution:
   · Runs Python script with the same input
   · Measures execution time
4. Comparison:
   · Compares outputs from both programs
   · Calculates performance ratio
5. Cleanup: Removes all temporary files

***Configuration***

**timeout Settings**

· C++ timeout: 100 seconds (modifiable in cpp_runner.py)
· Python timeout: 10 seconds (modifiable in py_runner.py)

**Input Range**

· Default: Random integers between 1 and 10,000
· Modifiable in utils.py (min_val, max_val parameters)

***Troubleshooting***

**Common Issues**

1. "clang++ not found" error
   · Install clang++ or modify cpp_runner.py to use g++
   · On Ubuntu: sudo apt-get install clang
   · On macOS: xcode-select --install
2. Python not found
   · Ensure Python is in PATH
   · On some systems, use python3 instead of python
3. Permission errors
   · Ensure you have write permissions in the current directory
   · The tool creates temporary files in the system temp directory
4. Timeout issues
   · Increase timeout values in cpp_runner.py or py_runner.py for complex algorithms

***Extending the Tool***

**Adding New Languages**

1. Create a new runner module (e.g., java_runner.py)
2. Implement a function similar to compile_and_run_cpp() or run_python()
3. Add support in main.py

**Custom Input Generation**

Modify utils.generate_random_input() to create different types of test data (strings, floats, etc.)

**Limitations**

· Currently only supports single-file C++ and Python programs
· Input is limited to integer arrays (but can be extended)
· Comparison is based on exact string matching of outputs

**License**

licensed under the MIT license.

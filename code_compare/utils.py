import random
import tempfile
import os

def generate_random_input(n=1000, min_val=1, max_val=10000):
    """Generate random input: n integers"""
    return [random.randint(min_val, max_val) for _ in range(n)]

def write_input_to_file(data, prefix="input"):
    """Save input to temporary file"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, prefix=prefix, suffix='.txt') as f:
        f.write('\n'.join(map(str, data)))
        return f.name

def read_output_from_file(filepath):
    """Read output from file"""
    try:
        with open(filepath, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""
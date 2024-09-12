import subprocess
import time
import os

def run_command(command, cwd):
    start_time = time.time()
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    end_time = time.time()
    return result.stdout, result.stderr, end_time - start_time

def compile_cpp():
    cpp_dir = os.path.join(os.getcwd(), "cpp")
    compile_command = ["g++", "-std=c++20", "main.cpp", "-o", "main"]
    result = subprocess.run(compile_command, cwd=cpp_dir, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"C++ compilation failed:\n{result.stderr}")
        return False
    return True

languages = [
    ("Python", ["python", "improved_async_tasks.py"], "python"),
    ("Go", ["go", "run", "main.go"], "golang"),
    ("Rust", ["cargo", "run", "--release"], "rust"),
    ("C++", ["./main"], "cpp")
]

results = []

if not compile_cpp():
    print("Skipping C++ test due to compilation failure.")
    languages = [lang for lang in languages if lang[0] != "C++"]

for lang, command, cwd in languages:
    print(f"Running {lang} implementation...")
    stdout, stderr, execution_time = run_command(command, cwd)
    print(f"{lang} output:")
    print(stdout)
    if stderr:
        print(f"{lang} errors:")
        print(stderr)
    results.append((lang, execution_time))

print("\nExecution time comparison:")
for lang, execution_time in results:
    print(f"{lang}: {execution_time:.3f} seconds")

with open("comparison_results.log", "w") as log_file:
    log_file.write("Execution time comparison:\n")
    for lang, execution_time in results:
        log_file.write(f"{lang}: {execution_time:.3f} seconds\n")

"""
To run the comparison:

1. Ensure all implementations are built (especially for C++)
2. Run `python compare_results.py` from the project root directory

This script will run each implementation and display their outputs and execution times, 
allowing you to compare the performance and behavior of the concurrent task 
execution across the four languages.
"""
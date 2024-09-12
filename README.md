# Concurrent Task Execution Comparison

This project aims to implement and compare concurrent task execution in multiple programming languages: Python, Rust, Go, and C++. The goal is to explore software engineering concepts related to concurrency, parallelism, and asynchronous programming.
We're exploring concurrency vs parallelism in this project. The implementations in different languages demonstrate various approaches to concurrent task execution, which is not necessarily the same as parallelism.

Concurrency is about dealing with multiple tasks at the same time, but not necessarily executing them simultaneously. Parallelism, on the other hand, is about actually executing multiple tasks at the exact same time, typically on different CPU cores.

In our implementations:
- Python uses asyncio for cooperative multitasking (concurrency).
- Go uses goroutines and channels for concurrent execution.
- Rust uses tokio for asynchronous programming (concurrency).
- C++ uses coroutines for cooperative multitasking (concurrency).

While these implementations focus on concurrency, they may or may not result in parallel execution depending on the runtime and system capabilities. The main goal is to compare how different languages handle concurrent task execution and their respective performance characteristics.

## Project Structure

- `python/`: Contains the Python implementation
- `rust/`: Contains the Rust implementation
- `go/`: Contains the Go implementation
- `cpp/`: Contains the C++ implementation

Each language-specific directory contains:
- The main implementation file
- A README with language-specific instructions
- Any necessary configuration files

## Running the Examples

### Python

1. Ensure you have Python 3.7+ installed
2. Navigate to the `python/` directory
3. Run `python improved_async_tasks.py`

### Rust

(Instructions will be added once the Rust implementation is complete)

### Go

(Instructions will be added once the Go implementation is complete)

### C++

(Instructions will be added once the C++ implementation is complete)

## Comparing Results

After implementing the concurrent task execution in all four languages, we will:

1. Compare the execution times
2. Analyze the code complexity and readability
3. Discuss the pros and cons of each language's concurrency model
4. Explore potential optimizations and best practices

## Contributing

Feel free to contribute by improving existing implementations or adding new features. Please follow the coding standards and conventions established for each language.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Notes

The execution time differences between the languages can be attributed to several factors:

1. Python (2.104 seconds):
Python's asyncio is efficient for I/O-bound tasks. The implementation uses cooperative multitasking, which allows for quick context switching between tasks.

2. Go (2 seconds):
Go's goroutines are lightweight and efficient. The slightly longer execution time compared to Python might be due to the overhead of creating and managing goroutines and channels.

3. Rust (2.002 seconds):
Rust's tokio runtime provides asynchronous programming capabilities. The slightly longer execution time could be due to the additional safety checks and abstractions that Rust provides.

4. C++ (5.00711 seconds):
C++ coroutines are a relatively new feature, and compiler optimizations might not be as mature as for other concurrency models.



To understand why these differences occur:

1. Runtime differences: Each language has its own runtime with different scheduling and task management strategies.
2. Implementation details: The way tasks are created and managed differs in each language.
3. Compiler optimizations: Different languages and their compilers apply various optimizations.
4. Overhead: Creating and managing concurrent tasks has different overheads in each language.



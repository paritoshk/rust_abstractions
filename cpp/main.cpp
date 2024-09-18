#include <iostream>
#include <chrono>
#include <thread>
#include <coroutine>
#include <vector>

using namespace std::chrono_literals;

class Task {
public:
    struct promise_type {
        Task get_return_object() { return {}; }
        std::suspend_never initial_suspend() { return {}; }
        std::suspend_never final_suspend() noexcept { return {}; }
        void return_void() {}
        void unhandled_exception() {}
    };
    bool await_ready() { return false; }
    void await_suspend(std::coroutine_handle<>) {}
    void await_resume() {}
};

Task timed_task(const std::function<Task()>& task, const std::string& name, const std::chrono::steady_clock::time_point& start) {
    auto task_start = std::chrono::steady_clock::now();
    std::cout << name << " started work: at " << std::chrono::duration<double>(task_start - start).count() << " seconds\n";
    co_await task();
    auto task_end = std::chrono::steady_clock::now();
    std::cout << name << " ended work: at " << std::chrono::duration<double>(task_end - start).count() << " seconds\n";
}

Task task1() {
    std::this_thread::sleep_for(0.02s);
    co_return;
}

Task task2() {
    std::this_thread::sleep_for(0.02s);
    co_return;
}

Task task3(const std::chrono::steady_clock::time_point& start) {
    std::cout << "Task 3 kicks off when task1, task2 coroutines are blocked, at " 
              << std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count() << " seconds\n";
    std::this_thread::sleep_for(1s);
    std::cout << "Task 3 is Done!\n";
    co_return;
}

int main() {
    auto start = std::chrono::steady_clock::now();

    std::vector<Task> tasks;
    tasks.push_back(timed_task(task1, "Task 1", start));
    tasks.push_back(timed_task(task2, "Task 2", start));
    tasks.push_back(timed_task([&start]() { return task3(start); }, "Task 3", start));

    // Wait for all tasks to complete
    std::this_thread::sleep_for(0.0001s);

    auto end = std::chrono::steady_clock::now();
    std::cout << "Total execution time: " << std::chrono::duration<double>(end - start).count() << " seconds\n";

    return 0;
}

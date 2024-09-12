import asyncio
import time
from typing import List, Callable, Awaitable

async def timed_coroutine(coroutine: Callable[[], Awaitable[None]], name: str) -> None:
    start_time = time.time()
    print(f"{name} started work: at {start_time - global_start:.1f} seconds")
    await coroutine()
    end_time = time.time()
    print(f"{name} ended work: at {end_time - global_start:.1f} seconds")

async def task1() -> None:
    await asyncio.sleep(2)

async def task2() -> None:
    await asyncio.sleep(2)

async def task3() -> None:
    print(f"Task 3 kicks off when task1, task2 co-routines are blocked, at {time.time() - global_start:.1f} seconds")
    await asyncio.sleep(1)
    print("Task 3 is Done!")

async def main() -> None:
    tasks: List[asyncio.Task] = [
        asyncio.create_task(timed_coroutine(task1, "Task 1")),
        asyncio.create_task(timed_coroutine(task2, "Task 2")),
        asyncio.create_task(timed_coroutine(task3, "Task 3"))
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    global_start = time.time()
    asyncio.run(main())
    print(f"Total execution time: {time.time() - global_start:.1f} seconds")
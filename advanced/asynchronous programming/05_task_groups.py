"""
Task groups provide built-in error handling, which is why, it is preferred over the `gather` function
"""

import asyncio


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} is fetching the data...")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:  # Asynchronous context manager
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")


asyncio.run(main())

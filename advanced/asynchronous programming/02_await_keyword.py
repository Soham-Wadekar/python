import asyncio
import time


async def fetch_data(delay, id):
    """A coroutine that simulates a time consuming task"""

    print(f"Fetching data for {id}...")
    await asyncio.sleep(delay)  # Simulating an IO operation with a sleep delay
    print(f"Data fetched for {id}!")
    return {"data": "test", "id": id}


async def main():
    """A coroutine that calls the above coroutine"""

    print("Start of main coroutine")
    task_1 = fetch_data(3, 1)
    task_2 = fetch_data(5, 2)

    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result_1 = await task_1
    print(f"Received result: {result_1}")

    result_2 = await task_2
    print(f"Received result: {result_2}")

    print("End of main coroutine")


start = time.time()
asyncio.run(main())
end = time.time()
print(f"The function took {end - start} seconds to execute.")

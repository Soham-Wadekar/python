import asyncio
import time

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} is fetching the data...")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    '''Tasks allows coroutines to run concurrently'''

    task1 = asyncio.create_task(fetch_data(1, 3))
    task2 = asyncio.create_task(fetch_data(2, 1))
    task3 = asyncio.create_task(fetch_data(3, 5))

    results = await asyncio.gather(task1, task2, task3)         # Runs multiple coroutines concurrently

    for result in results:
        print(result)

start = time.time()
asyncio.run(main())
end = time.time()
print(f"The function took {end - start} seconds to execute.")
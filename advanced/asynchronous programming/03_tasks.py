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

    result1 = await task1
    result2 = await task2
    result3 = await task3

    task4 = asyncio.create_task(fetch_data(4, 2))
    result4 = await task4

    print(result1)
    print(result2)
    print(result3)
    print(result4)

start = time.time()
asyncio.run(main())
end = time.time()
print(f"The function took {end - start} seconds to execute.")
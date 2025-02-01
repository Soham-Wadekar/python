"""
Semaphores are similar to locks but while locks allow only 1 task to access the resource,
semaphores allow a specified number of tasks to access the shared resource concurrently
"""

import asyncio


async def access_shared_resource(semaphore, resource_id):
    async with semaphore:
        # Simulate accessing a limited resource
        print(f"Accessing resource: {resource_id}")
        await asyncio.sleep(2)
        print(f"Releasing resource: {resource_id}")


async def main():
    semaphore = asyncio.Semaphore(2)  # Allow 2 concurrent access
    await asyncio.gather(*(access_shared_resource(semaphore, i) for i in range(5)))


asyncio.run(main())

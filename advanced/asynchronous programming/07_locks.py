"""
Locks are used to prevent multiple tasks from accessing and modifying a shared resource simultaneously.
When a task acquires the lock, other tasks that try to acquire it must wait until the lock is released.
Once the task holding the lock finishes its operation and releases the lock, another waiting task can acquire it and proceed.
"""

import asyncio

# A shared variable
shared_resource = 0

# An Asyncio lock
lock = asyncio.Lock()


async def modify_shared_resource():
    global shared_resource
    async with (
        lock
    ):  # Checks whether no other coroutine is using the lock, only then will it proceed
        # Critical session starts
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1
        await asyncio.sleep(2)  # Simulate an IO operation
        print(f"Resource after modification: {shared_resource}")


async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))


asyncio.run(main())

import time 
import asyncio
# cpu bound tasks

count = 5000
def countfun(n):
    while n >= 0:
        print(n)
        n -= 1

start = time.time()
# countfun(count)
# print(f'time taken {time.time() - start}')


async def task_one():
    # time.sleep(3)
    await asyncio.sleep(3)
    print("task 1 execution completed......")

async def task_tow():
    await asyncio.sleep(1)
    print("task 2 completed")

async def main():
    task1 = asyncio.create_task(task_one())
    task2 = asyncio.create_task(task_tow())
    print("both tasks started")
    await task1
    await task2
    print("both tasks completed")

asyncio.run(main())

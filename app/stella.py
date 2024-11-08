import asyncio
from datetime import datetime as time
from collections import defaultdict

def execute():
    asyncio.run(run_tasks())   

async def run_tasks():
    result = defaultdict(int)
    for i in range(10):
        print(i)
        result[i] = asyncio.create_task(async_task())
        print(i*10)
    
    await asyncio.gather(*result.values())

def async_task():
    asyncio.sleep(1)
    return 1
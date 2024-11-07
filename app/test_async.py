import asyncio
from datetime import datetime as time
from collections import defaultdict

result_dict = defaultdict(tuple)
async def process_data(data):
    # Simulating some async processing
    await asyncio.sleep(0)
    processed_data = data.upper()
    return processed_data


async def main(task_num: int, processing_time: int=0): 
    # Some data to process
    data = "hello, world!"

    # Processing the data asynchronously
    processed_data = await process_data(data)
    # print(f"Processed data: {processed_data}, task number {task_num}, processing for {processing_time} seconds")

    await asyncio.sleep(processing_time)
    # print(f"Task {task_num} finished processing after {processing_time} seconds")
    result_dict[task_num] = (task_num, processing_time)
    print("result dict: ", result_dict)


# Running the main function
async def run_tasks():
    start_time = time.now()
    print("start at: ", start_time)
    await asyncio.gather(main(1,2), main(2,1), main(3,0),main(4,3),main(5,10))
    end_time = time.now()
    print("end at: ", end_time)
    print("total time: ", end_time - start_time)
    print("result dict: ", result_dict)
asyncio.run(run_tasks())


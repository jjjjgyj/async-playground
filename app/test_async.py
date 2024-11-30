# import asyncio
# from datetime import datetime as time
# from collections import defaultdict

# result_dict = defaultdict(tuple)
# async def process_data(data):
#     # Simulating some async processing
#     await asyncio.sleep(0)
#     processed_data = data.upper()
#     return processed_data


# async def main(task_num: int, processing_time: int=0): 
#     # Some data to process
#     data = "hello, world!"

#     # Processing the data asynchronously
#     processed_data = await process_data(data)
#     # print(f"Processed data: {processed_data}, task number {task_num}, processing for {processing_time} seconds")

#     await asyncio.sleep(processing_time)
#     # print(f"Task {task_num} finished processing after {processing_time} seconds")
#     result_dict[task_num] = (task_num, processing_time)
#     print("result dict: ", result_dict)


# # Running the main function
# async def run_tasks():
#     start_time = time.now()
#     print("start at: ", start_time)
#     await asyncio.gather(main(1,2), main(2,1), main(3,0),main(4,3),main(5,10))
#     end_time = time.now()
#     print("end at: ", end_time)
#     print("total time: ", end_time - start_time)
#     print("result dict: ", result_dict)
# asyncio.run(run_tasks())

'''
Async processing code in a stella structure
'''
import asyncio
from datetime import datetime as time
import time as real_time
from collections import defaultdict

def execute():
    print("test isinstance: ", isinstance(1, int))
    start_time = time.now()
    print("start at: ", start_time)
    result = asyncio.run(run_tasks())   
    print('result == ', result)
    end_time = time.now()
    print("end at: ", end_time)
    print("total time: ", end_time - start_time)

async def run_tasks():
    result = defaultdict(int)
    for i in range(10):
        # print(i)
        result[i] = asyncio.create_task(async_task(i))
        # print(i*10)
    
    deadline_seconds = 6
    try:
        await asyncio.wait_for(asyncio.gather(*result.values()), timeout=deadline_seconds)
    except:
        pass

    success_task_cnt = sum([v.result() for k, v in result.items() if not v.cancelled() and not v.exception()])
    return success_task_cnt

async def async_task(i):
    try:
        await asyncio.sleep(5)
        if i == 1:
            raise ValueError("This is a test error")
        return 1
    except Exception as e:
        print(f"Task {i} failed with error: {e}")
        return 0
if __name__ == '__main__':
    execute()

# '''
# Sync processing code in a stella structure
# '''

# import asyncio
# from datetime import datetime as time
# import time as real_time
# from collections import defaultdict

# def execute():
#     start_time = time.now()
#     print("start at: ", start_time)
#     result = asyncio.run(run_tasks())   
#     print('result == ', result)
#     end_time = time.now()
#     print("end at: ", end_time)
#     print("total time: ", end_time - start_time)
    
# async def run_tasks():
#     result = 0
#     for i in range(10):
#         # print(i)
#         result += sync_task(i)
#         # print(i*10)
    
#     return result

# def sync_task(i):
#     try:
#         real_time.sleep(5)
#         if i == 1:
#             raise ValueError("This is a test error")
#         return 1
#     except Exception as e:
#         print(f"Task {i} failed with error: {e}")
#         return 0
# if __name__ == '__main__':
#     execute()
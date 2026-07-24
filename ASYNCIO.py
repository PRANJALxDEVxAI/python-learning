import asyncio

# ------------------------------------------------------------------Coroutine function----------------------------------------------------------
# # async def main():
# #     print("Start of main coroutine")

# #define a coroutine that stimulates a time-consuming task   
# async def fetch_data(delay , id):
#     print("Fetching data...id:" , id)
#     await asyncio.sleep(delay)    #Stimulate an I/O operation with a sleep
#     print("Data Fetched ,id:" ,id)
#     return {"data" : "Some data" , "id":  id}       #Return some data


# #define another coroutine that calls the first coroutine
# async def main():
#     print("Start of main coroutine")
#     task1 = fetch_data(2 , 1)
#     task2 = fetch_data(2 , 2)
#     #Await the fetch_data coroutine , pausing execution of main until fetch_data completes 
#     result1 = await task1
#     print(f"recieved result: {result1}")
#     result2 = await task2
#     print(f"recieved result: {result2}")
#     print("End of the main coroutine")



# #Run the main coroutine
# asyncio.run(main())

#-------------------------------------------------------------TASKS----------------------------------------------------------

# async def fetch_data(id , sleept_time):
#     print(f"Coroutine {id} starting to fetch data.")
#     await asyncio.sleep(sleept_time)
#     return {"id": id , "data" : f"Sample sata from coroutine {id}"}


# async def main():
    # #Create tasks for running coroutines concurrently
    # task1 = asyncio.create_task(fetch_data(1,2))
    # task2 = asyncio.create_task(fetch_data(2,3))
    # result1 = await task1
    # result2 = await task2
    # task3 = asyncio.create_task(fetch_data(3,4))

    
    # result3 = await task3

    # print(result1 ,"\n",result2 ,"\n" ,result3)



# asyncio.run(main())

#------------------------------------------------------------------Gather Functions------------------------------------------------------------

# async def fetch_data(id , sleep_time):
#     print(f"Coroutine {id} starting to fetch data.")
#     await asyncio.sleep(sleep_time)
#     return {"id": id , "data" : f"Sample sata from coroutine {id}"}



# async def main():
#     #Run coroutines concurrently and gather their return values
#     results = await asyncio.gather(fetch_data(1,2) , fetch_data(2,1) , fetch_data(3,3))
#     #Process the results
#     for result in results:
#         print(f"Receiveed result: {result}")


# #Run the main coroutine
# asyncio.run(main())



#------------------------------------------------------------------TASK GROUP------------------------------------------------------------------

# async def fetch_data(id , sleep_time):
#     print(f"Coroutine {id} starting to fetch data.")
#     await asyncio.sleep(sleep_time)
#     return {"id": id , "data" : f"Sample sata from coroutine {id}"}

# async def main():
#     tasks = []
#     async with asyncio.TaskGroup() as tg:
#         for i , sleep_time in enumerate([2,1,3] , start = 1):
#             task = tg.create_task(fetch_data(i , sleep_time))
#             tasks.append(task)

#     #After the Task Group block , all tasks have completed 
#     results = [task.result() for tak in tasks]

#     for result in results:
#         print(f"Recieved result: {result}")


# asyncio.run(main())




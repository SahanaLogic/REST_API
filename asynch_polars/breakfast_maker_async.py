import asyncio
import time

async def prepare_coffee():
    print("Coffee brewing started")
    await asyncio.sleep(2)
    print("Coffee brewing finished")
    return "Your coffee is ready!"

async def toast_bread():
    print("Started toasing bread")
    await asyncio.sleep(3)
    print("Finished toasing bread")
    return "Your bread toast is ready!"

async def async_gather():
    start_time = time.time()
    batch = asyncio.gather(prepare_coffee(), toast_bread())
    res1,res2 = await batch
    end_time = time.time()
    print(f"Total time needed to prep is {end_time-start_time:.2f} s")

async def async_create_task():
    start_time = time.time()
    coffee = asyncio.create_task(prepare_coffee())
    toast = asyncio.create_task(toast_bread())
    res_coffee = await coffee
    res_toast = await toast
    print(res_coffee)
    print(res_toast)
    end_time = time.time()
    print(f"Total time needed to prep is {end_time-start_time:.2f} s")



def main():
    start_time = time.time()
    coffee = prepare_coffee()
    print(coffee)
    toast = toast_bread()
    print(toast)
    end_time = time.time()
    print(f"Total time needed to prep is {end_time-start_time}s")

if __name__ == "__main__":
    #main()
    #asyncio.run(async_gather())
    asyncio.run(async_create_task())
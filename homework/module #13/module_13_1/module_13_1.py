import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    i = 1
    for i in range(5):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i} шар')
        i += 1
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    first = asyncio.create_task(start_strongman('one', 2))
    second = asyncio.create_task(start_strongman('two', 4))
    third = asyncio.create_task(start_strongman('three', 8))
    await first
    await second
    await third

asyncio.run(start_tournament())

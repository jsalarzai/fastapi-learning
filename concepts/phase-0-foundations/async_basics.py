import asyncio


async def make_coffee():
    print("Starting Coffee...")
    await asyncio.sleep(5)
    print("Coffee is ready!")


async def make_toast():
    print("Starting toast...")
    await asyncio.sleep(1)
    print("Toast is ready!")


async def main():
    # await make_coffee()
    # await make_toast()

    await asyncio.gather(make_coffee(), make_toast())


asyncio.run(main())

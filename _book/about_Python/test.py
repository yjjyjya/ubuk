import aiofiles
import asyncio

async def write_to_file(filename, data):
    async with aiofiles.open(filename, 'w') as file:
        await file.write(data)

async def read_from_file(filename):
    async with aiofiles.open(filename, 'r') as file:
        return await file.read()

async def main():
    await write_to_file('example.txt', 'Hello, async file I/O!')
    data = await read_from_file('example.txt')
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
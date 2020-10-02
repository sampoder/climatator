import asyncio
from kasa import SmartPlug

async def main():
    p = SmartPlug("192.168.1.144")

    await p.update()
    print(p.is_on)

    await p.turn_off()


if __name__ == "__main__":
    asyncio.run(main())
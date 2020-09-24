import asyncio


async def main(n: int) -> None:
    for x in range(n):
        print(f'\rexecultando {n} vezes - atual = {x}', end='')
        x += 1
        await asyncio.sleep(.001)
    print(f'\nexecutado {n} vezes')

async def run():
    ini = loop.time()
    await asyncio.wait([
        main(100),
        main(80),
        main(4)
    ])
    fim = loop.time()
    print(f'tempo total {round(fim-ini, 3)} s')

loop = asyncio.get_event_loop()
loop.run_until_complete(run())

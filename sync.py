from time import sleep, time


def main(n: int) -> None:
    for x in range(n):
        print(f'\rexecultando {n} vezes - atual = {x}', end='')
        x += 1
        sleep(.001)
    print(f'\nexecutado {n} vezes')


if __name__ =='__main__':
    ini = time()
    main(100)
    main(80)
    main(4)
    fim = time()
    print(f'tempo total {round(fim - ini, 3)} s')
from time import sleep, time
import threading

def main(n: int) -> None:
    for x in range(n):
        print(f'\rexecultando {n} vezes - atual = {x}', end='')
        x += 1
        sleep(.001)
    print(f'\nexecutado {n} vezes')


if __name__ =='__main__':
    # Create new threads
    ini = time()
    thread1 = threading.Thread(target=main, args=(100,))
    thread2 = threading.Thread(target=main, args=(80,))
    thread3 = threading.Thread(target=main, args=(4,))
    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
    fim = time()
    print(f'tempo total {round(fim - ini, 3)} s')
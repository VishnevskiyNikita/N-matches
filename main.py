from random import randint


def nums():
    nofmatches = randint(15, 30)
    return [randint(2, nofmatches // 3), nofmatches, randint(0, 1)]


def main():
    t, n, first = nums()
    print(
        f'Number of matches: {n}, you can take from 1 to {t} matches, {"computer" if first == 0 else "player"} goes first')
    curr = 'c' if first == 0 else 'p'
    while n != 0:
        print('| ' * n, 'In total:', n)
        if curr == 'c':
            if n % (1 + t) == 0 and curr == 'c':
                hm = randint(1, t)
                print(f'Computer takes {hm} {"matches" if hm > 1 else "match"}')
                n -= 1
                curr = 'p'
                continue
            hm = n % (1 + t)
            print(f'Computer takes {hm} {"matches" if hm > 1 else "match"}')
            n -= hm
            curr = 'p'
            continue
        hm = int(input('How much matches do you want to take: '))
        while hm >= n or hm == 0:
            print('Incorrect input!')
            hm = int(input('How much matches do you want to take: '))
        n -= hm
        curr = 'c'
    print(f'{"Computer" if curr == "p" else "Player"} wins!')


main()

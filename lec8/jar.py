class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._cookies = 0
        if not int(capacity) >= 0:
            raise ValueError('cannot have negative capacity')

    def __str__(self):
        return self._cookies * '🍪'

    def deposit(self, n):
        self._cookies += n
        if self._cookies > self._capacity:
            raise ValueError('too many cookies')

    def withdraw(self, n):
        if n > self._cookies:
            raise ValueError('not enough cookies')
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies

def main():
    jar = Jar()
    dep = int(input('how many cookies would you like to add? '))
    draw = int(input('how many cookies would you like to eat? '))
    jar.deposit(dep)
    jar.withdraw(draw)

    print(f'there are {jar.size} cookies in the jar')


if __name__ == "__main__":
    main()

from tile import Tile, Suits, Values


def main():
    t1 = Tile(Suits.PIN, Values.ONE, True)
    print(t1.suit)
    print(t1.value)
    print(t1.red)

if __name__ == "__main__":
    main()
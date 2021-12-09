from tile import Tile, Suits


def main():
    t1 = Tile(Suits.PIN, 12)
    print(t1.suit)
    print(t1.value)
    print(t1.red)

if __name__ == "__main__":
    main()
import argparse
from .core import add, sub, mean, is_prime


def main() -> None:
    parser = argparse.ArgumentParser(prog="mini-calc", description="Prosty kalkulator CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_add = subparsers.add_parser("add", help="Dodawanie a + b")
    p_add.add_argument("a", type=float)
    p_add.add_argument("b", type=float)

    p_sub = subparsers.add_parser("sub", help="Odejmowanie a - b")
    p_sub.add_argument("a", type=float)
    p_sub.add_argument("b", type=float)

    p_mean = subparsers.add_parser("mean", help="Średnia z listy liczb")
    p_mean.add_argument("numbers", nargs="+", type=float)

    p_prime = subparsers.add_parser("prime", help="Sprawdź czy liczba jest pierwsza")
    p_prime.add_argument("n", type=int)

    args = parser.parse_args()

    if args.command == "add":
        print(add(args.a, args.b))
    elif args.command == "sub":
        print(sub(args.a, args.b))
    elif args.command == "mean":
        print(mean(args.numbers))
    elif args.command == "prime":
        print("YES" if is_prime(args.n) else "NO")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

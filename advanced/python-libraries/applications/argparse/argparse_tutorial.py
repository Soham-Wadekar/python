from argparse import ArgumentParser

add_choice = [10, 20]

parser = ArgumentParser()
group = parser.add_mutually_exclusive_group()

# Mandatory positional arguments
parser.add_argument("square", help="Squares the number", type=int, default=0, nargs="?")
parser.add_argument(
    "--add", help="Adds a given number", type=int, choices=add_choice, default=10
)

group.add_argument(
    "-v",
    "--verbose",
    help="Verbose description. Use -vv for extra verbose",
    action="count",
    default=0,
)
group.add_argument("-s", "--silence", help="Silent description", action="store_true")

args = parser.parse_args()

result = args.square**2

match args.add:
    case 10:
        result += 10
    case 20:
        result += 20

match args.verbose:
    case 0:
        print(result)
    case 1:
        print(f"Result = {result}")
    case 2:
        print(f"Calculating...")
        print(f"Result = {result}")
    case 3:
        print(f"Really? Okay...")
        print(f"Calculating...")
        print(f"Result = {result}")
    case _:
        print("That's it!!")
        for _ in range(args.verbose):
            print(f"Result = {result}")
        print("Happy??")

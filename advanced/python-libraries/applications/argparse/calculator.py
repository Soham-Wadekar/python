from argparse import ArgumentParser

operations = ["add", "sub", "mul", "div", "f_div", "exp"]


def compute(n1, n2, op):
    match op:
        case "add":
            return n1 + n2
        case "sub":
            return n1 - n2
        case "mul":
            return n1 * n2
        case "div":
            return n1 / n2 if n2 != 0 else "Invalid!"
        case "f_div":
            return n1 // n2
        case "exp":
            return n1**n2


parser = ArgumentParser()

parser.add_argument("num1", help="The first operand", type=int)
parser.add_argument("num2", help="The second operand", type=int)

# Operations
parser.add_argument(
    "--operation",
    help="Select the operation to perform",
    type=str,
    choices=operations,
    default="add",
)
parser.add_argument(
    "-r", "--reverse", help="Reverses the order of the operands", action="store_true"
)

args = parser.parse_args()

if args.reverse:
    result = compute(args.num2, args.num1, args.operation)
    print(f"The result is {result}")
else:
    result = compute(args.num1, args.num2, args.operation)
    print(f"The result is {result}")

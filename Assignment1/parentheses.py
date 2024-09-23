import sys


def evaluate(expr: str):
    opens = 0
    for c in expr:
        if c == '(':
            opens += 1
        elif c == ')':
            opens -= 1

    if opens == 0:
        return "yes"
    else:
        return "no"


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        raise Exception("Command line arguments invalid")
    else:
        print(evaluate(sys.argv[1]))


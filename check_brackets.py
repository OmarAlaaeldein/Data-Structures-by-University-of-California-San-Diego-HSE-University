# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            if are_matching(next,opening_brackets_stack[-1]):
                opening_brackets_stack.pop()
            # Process closing bracket, write your code here
            elif not are_matching(next,opening_brackets_stack[-1]):
                return i+1
    return True
            

def main():
    text = input()
    mismatch = find_mismatch(text)
    if type(mismatch)==bool:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()

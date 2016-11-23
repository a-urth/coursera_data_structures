# python3

import sys


class EmptyStackError(Exception):
    pass


class Stack:

    def __init__(self):
        self.__stack = []

    def push(self, value):
        self.__stack.append(value)

    def is_empty(self):
        return not self.size()

    def size(self):
        return len(self.__stack)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('Stack is empty, nothing to pop')
        return self.__stack.pop()

BRACKETS_MAP = {')': '(', '}': '{', ']': '['}

OPENING_BRACKETS = set(BRACKETS_MAP.values())
CLOSING_BRACKETS = set(BRACKETS_MAP.keys())


def _is_bracket(c):
    return c and c in BRACKETS_MAP


def _is_opening_bracket(c):
    return c and c in OPENING_BRACKETS


def _is_closing_bracket(c):
    return c and c in CLOSING_BRACKETS


def check_brackets(text):
    opening_brackets_stack = Stack()
    for i, c in enumerate(text, 1):
        if _is_opening_bracket(c):
            opening_brackets_stack.push((i, c))

        if _is_closing_bracket(c):
            try:
                _i, top_open = opening_brackets_stack.pop()
            except EmptyStackError:
                return i
            if top_open != BRACKETS_MAP[c]:
                return i

    if opening_brackets_stack.is_empty():
        return 'Success'
    return opening_brackets_stack.pop()[0]


if __name__ == "__main__":
    text = sys.stdin.read()

    print(check_brackets(text))

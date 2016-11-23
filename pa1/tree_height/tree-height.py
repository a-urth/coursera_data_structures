# python3

import sys
import threading

from collections import defaultdict

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size


def max_height(tree, h=0, current=-1):
    if current not in tree:
        return h
    return max(map(lambda node: max_height(tree, h + 1, node),
                   tree[current]))


def main():
    n, tree = map(lambda s: s.strip(), sys.stdin.readlines())
    tree_map = defaultdict(list)
    for k, v in zip(tree.split(), range(int(n))):
        tree_map[int(k)].append(v)
    print(max_height(tree_map))


threading.Thread(target=main).start()

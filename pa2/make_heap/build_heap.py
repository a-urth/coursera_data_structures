# python3


def swap(array, n, i):
    left_i, right_i, = i * 2 + 1, i * 2 + 2
    swap_l, swap_r = i, i
    if (
        left_i < n and
        array[swap_l] > array[left_i]
    ):
        swap_r = left_i
    if (
        right_i < n and
        array[swap_r] > array[right_i]
    ):
        swap_r = right_i
    if swap_l == swap_r:
        return
    array[swap_l], array[swap_r] = array[swap_r], array[swap_l]
    return swap_l, swap_r


def sift_down(array, n, i):
    swaps = []
    while 1:
        s = swap(array, n, i)
        if not s:
            return swaps
        swaps.append(s)
        i = s[1]


def build_heap():
    n, swaps = int(input()), []
    array = [int(s) for s in input().split()]
    assert n == len(array)
    for i in range(n // 2, -1, -1):
        ixs = sift_down(array, n, i)
        if ixs:
            swaps.extend(ixs)
    return swaps


if __name__ == '__main__':
    swaps = build_heap()
    print(len(swaps))
    if swaps:
        print('\n'.join(map(lambda s: '{} {}'.format(*s), swaps)))

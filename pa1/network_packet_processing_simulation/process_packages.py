# python3
from collections import deque, namedtuple

Package = namedtuple('Package', ['index', 'time_arrived', 'time_to_process'])


def _process_package(buffer, curr_time, results):
    package = buffer.popleft()
    if curr_time < package.time_arrived:
        curr_time = package.time_arrived
    results[package.index] = curr_time
    curr_time += package.time_to_process
    return curr_time


def _process_extra(buffer, x_buffer, curr_time, results):
    while x_buffer:
        x_package = x_buffer.popleft()
        if curr_time <= x_package.time_arrived:
            buffer.append(x_package)
            return

        results[x_package.index] = -1


def process_packages(packages, buff_size):
    curr_time, results = 0, [0 for _ in range(len(packages))]
    buffer = deque(packages[:buff_size])
    x_buffer = deque(packages[buff_size:])
    while buffer:
        curr_time = _process_package(buffer, curr_time, results)

        _process_extra(buffer, x_buffer, curr_time, results)
    return results


def load_packages(n):
    packages = []
    for i in range(n):
        time_arrived, time_to_process = map(int, input().strip().split())
        packages.append(Package(i, time_arrived, time_to_process))
    return packages


if __name__ == "__main__":
    buff_size, count = map(int, input().strip().split())
    packages = load_packages(count)
    # print(packages)
    for result in process_packages(packages, buff_size):
        print(result)

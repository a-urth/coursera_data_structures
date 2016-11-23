# python3

from heapq import heappop, heappush


def process_jobs(num_workers, jobs):
    workers, results = [], []
    for i in range(num_workers):
        heappush(workers, (0, i))

    for job_time in jobs:
        curr_time, worker = heappop(workers)
        results.append((worker, curr_time))
        heappush(workers, (curr_time + job_time, worker))

    return '\n'.join('{} {}'.format(*r) for r in results)


if __name__ == '__main__':
    n, m = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert m == len(jobs)

    print(process_jobs(n, jobs))

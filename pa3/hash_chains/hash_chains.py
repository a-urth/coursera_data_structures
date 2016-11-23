# python3


class HashTable:

    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.storage = [[] for _ in range(bucket_count)]
        self.buckets_num = bucket_count

    def add_s(self, s):
        _h = self._hash(s)
        if s in self.storage[_h]:
            return
        self.storage[_h].append(s)

    def find_s(self, s):
        _h = self._hash(s)
        if s in self.storage[_h]:
            return 'yes'
        return 'no'

    def del_s(self, s):
        _h = self._hash(s)
        for i, _s in enumerate(self.storage[_h]):
            if _s == s:
                del self.storage[_h][i]

    def check_s(self, i):
        return ' '.join(reversed(self.storage[int(i)]))

    def _hash(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.buckets_num


def process_queries(buckets, queries):
    res = []
    ht = HashTable(buckets)
    for query in queries:
        query, arg = query.split()
        r = getattr(ht, '{}_s'.format(query))(arg)
        if r is not None:
            res.append(r)
    return res


if __name__ == '__main__':
    buckets = int(input())
    n = int(input())
    queries = tuple(input() for _ in range(n))
    print('\n'.join(process_queries(buckets, queries)))

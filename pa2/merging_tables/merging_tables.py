# python3


class DisjointSetDB:

    def __init__(self, n, rows):
        self.rank = [0 for _ in range(n)]
        self.rows = rows
        self.tree = list(range(n))

    def find_root(self, i):
        steps, root = [], i
        while self.tree[root] != root:
            root = self.tree[root]
            steps.append(root)
        if len(steps) > 1:
            for s in steps:
                self.tree[s] = root
        return root

    def merge(self, d, s):
        s_root, d_root = self.find_root(s), self.find_root(d)

        if s_root == d_root:
            return -1

        new_rows = self.rows[d_root] + self.rows[s_root]
        if self.rank[d_root] >= self.rank[s_root]:
            self.tree[s_root] = d_root
            if self.rank[d_root] == self.rank[s_root]:
                self.rank[d_root] += 1
            self.rows[d_root], self.rows[s_root] = new_rows, 0
        else:
            self.tree[d_root] = s_root
            self.rows[s_root], self.rows[d_root] = new_rows, 0

        return new_rows


def merge_tables(lines, queries):
    _max, db, res = max(lines), DisjointSetDB(n, lines), []
    for d, s in queries:
        new_rows = db.merge(d - 1, s - 1)
        _max = new_rows if new_rows > _max else _max
        res.append(str(_max))
    return res


if __name__ == '__main__':
    n, m = map(int, input().split())
    lines = list(map(int, input().split()))
    queries = tuple(map(int, input().split()) for _ in range(m))
    print('\n'.join(merge_tables(lines, queries)))

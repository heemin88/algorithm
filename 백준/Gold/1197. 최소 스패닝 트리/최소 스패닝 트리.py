import heapq

v, e = map(int, input().split())
q = []
for i in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))  # (가중치, a정점,b정점)
uf = [x for x in range(v + 1)]  # UnionFind


def uf_connected(a, b):
    while a != uf[a]:
        a = uf[a]
    while b != uf[b]:
        b = uf[b]
    if a == b:
        return True  # 사이클 발생
    else:
        return False  # 사이클 미발생


def uf_union(a, b):
    while uf[a] != a:
        a = uf[a]
    while uf[b] != b:
        b = uf[b]
    uf[b] = a


result = 0
while q:
    w, a, b = heapq.heappop(q)
    # 사이클 체크
    if not uf_connected(a, b):
        uf_union(a, b)
        result += w
print(result)

def solution(n, lost, reserve):
  _reserve = [r for r in reserve if r not in lost]
  _lost = [r for r in lost if r not in reserve]

  for r in _reserve:
    f = r-1
    b = r+1

    if f in _lost:
      _lost.remove(f)
    if b in _lost:
      _lost.remove(b)
  return n - len(_lost)

# print(solution(5,	[2, 4],	[1, 3, 5]))
# print(solution(5,	[2, 4],	[3]))
# print(solution(3,	[3],	[1]))
# print(solution(5,	[4,2],	[3,5]))
print(solution(5, [1, 2], [2, 3]))
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2
# 5,	[4,2],	[5,3] 5
# 5, [1, 2], [2, 3] 4

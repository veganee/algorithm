def solution(answers):
  pattern={
    1:[ 1,2,3,4,5],
    2:[ 2,1,2,3,2,5,2,5],
    3:[ 3,3,1,1,2,2,4,4,5,5]
  }

  score={
    1:0,
    2:0,
    3:0
  }

  for key in score.keys():
    for idx, answer in enumerate(answers):
      if answer ==  pattern[key][idx]:
        score[key] += 1

  max = 0
  result = []
  for key, value in score.items():
      if max <= value:
        max = value

  # print(max)
  for key, value in score.items():
   if max == value:
    result.append(key)

  # print(result)
  return result

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]
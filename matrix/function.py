def matplus(A, B):
  res = []
  temp = []
  for i in range(len(A)):
    for j in range(len(A[0])):
      temp.append(A[i][j] + B[i][j])
    res.append(temp)
    temp = []

  return res



def matminus(A, B):
  res = []
  temp = []
  for i in range(len(A)):
    for j in range(len(A[0])):
      temp.append(A[i][j] - B[i][j])
    res.append(temp)
    temp = []

  return res



def matmul(A, B):
  res = []
  res_sub = []
  temp = 0
  for i in range(len(A)):
    for j in range(len(A[0])):
      for t in range(len(A)):
        temp += A[i][t] * B[t][j]
      res_sub.append(temp)
      temp = 0
    res.append(res_sub)
    res_sub = []

  return res



lst_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

lst_sub_data = []
for i in range(3):
  lst_sub_data.append([lst_data[i][0], lst_data[i][2]])

print(lst_sub_data)

A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [2, 4, 6],
    [1, 3, 5],
    [1, 0, 1]
]
print(matplus(A, B))
print(matminus(A, B))
print(matmul(A, B))

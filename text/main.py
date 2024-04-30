import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

corpus = [
    "Tôi thích môn Toán",
    "Tôi thích AI",
    "Tôi thích âm nhạc"
]

vector = []

for text in corpus:
  res = text.split(" ")
  for i in res:
    if i not in vector:
      vector.append(i)

print(vector)



token = [0 for i in range(len(vector))]
input = "Tôi thích AI thích Toán"
temp = input.split(" ")
for i in temp:
  token[vector.index(i)] += 1

print(token)
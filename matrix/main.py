import numpy as np
import tensorflow as tf
import torch
import random


random.seed(2024)

lst_data1 = [random.randint(-10, 10) for _ in range(12)]
lst_data2 = [random.randint(-10, 10) for _ in range(12)]

np_data1 = np.array(lst_data1).reshape((3, 4))
np_data2 = np.array(lst_data2).reshape((3, 4)).T

torch_data1 = torch.reshape(torch.tensor(lst_data1), (3, 4))
torch_data2 = torch.reshape(torch.tensor(lst_data2), (3, 4)).T

tf_data1 = tf.reshape(tf.convert_to_tensor(lst_data1), (3, 4))
tf_data2 = tf.reshape(tf.convert_to_tensor(lst_data2), (3, 4))
tf_data2 = tf.transpose(tf_data2)

print(np.matmul(np_data1, np_data2))
print(torch.matmul(torch_data1, torch_data2))
print(tf.linalg.matmul(tf_data1, tf_data2))


lst_data = [random.randint(-10, 10) for _ in range(9)]

np_data = np.array(lst_data).reshape((3, 3))
torch_data = torch.reshape(torch.tensor(lst_data), (3, 3))
tf_data = tf.reshape(tf.convert_to_tensor(lst_data), (3, 3))

print(np.sum(np_data, axis = 0))
print(np.sum(np_data, axis = 1))
print(torch.sum(torch_data, axis = 0))
print(torch.sum(torch_data, axis = 1))
print(tf.reduce_sum(tf_data, axis = 0))
print(tf.reduce_sum(tf_data, axis = 1))


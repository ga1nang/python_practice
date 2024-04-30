import numpy as np
import tensorflow as tf
import torch

lst = [data for data in range(0, 10)]

np_lst = np.array(lst)
print(np_lst, type(np_lst))
torch_lst = torch.tensor(lst)
print(torch_lst)
tf_lst = tf.convert_to_tensor(lst)
print(tf_lst)



lst_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


np_2d = np.array(lst_2d)
print(np_2d.shape)
print(np_2d.dtype)
print(type(np_2d))
print(np_2d)



torch_2d = torch.tensor(lst_2d)
print(torch_2d.shape)
print(torch_2d.dtype)
print(type(torch_2d))
print(torch_2d.device)
print(torch_2d)



tf_2d = tf.convert_to_tensor(lst_2d)
print(tf_2d.shape)
print(tf_2d.dtype)
print(type(tf_2d))
print(tf_2d.device)
print(tf_2d)
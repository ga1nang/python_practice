import numpy as np
import torch
import tensorflow as tf

shape = (3, 4)
print(np.zeros(shape))
print(torch.zeros(shape))
print(tf.zeros(shape))



print(np.ones(shape))
print(torch.ones(shape))
print(tf.ones(shape))



print(np.full(shape, 5))
print(torch.full(shape, 5))
print(tf.fill(shape, 5))
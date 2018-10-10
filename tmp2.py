# import collections
# import random
# import numpy as np
# import tensorflow as tf
# 
# 
# # Define a placeholder that expects a vector of three floating-point values,
# # and a computation that depends on it.
# x = tf.Variable(1)
# print('x: ', x) 
# with tf.Session() as sess:
#   sess.run(tf.global_variables_initializer())
#   
#   
#   a = x.value()
#   print(a )
#   
#   b = x.assign(3)
#   print('x.assign(3): ', b)
#   
#   y = x +1
#   print('y:', y)
#   print (sess.run(x.value()) )

class Foo:
  def __init__(self):
    self._attr = 0

  @property
  def attr(self):
      return self._attr

  @attr.setter
  def attr(self, value):
      self._attr = value

  @attr.deleter
  def attr(self):
      del self._attr
        


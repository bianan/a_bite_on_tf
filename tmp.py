# Define a function here.

"""
https://www.techbeamers.com/use-try-except-python/
"""
import sys
import tensorflow as tf
# Just disables the warning, doesn't enable AVX/FMA
# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

# def temp_convert(var):
#   try:
#     return int(var)
#   except ValueError as e:
#     print("The argument does not contain numbers\n", e)
#     print("errno: ", e.errno)
# 
# 
# # Call above function here.
# temp_convert("xyz")


# a = {}
# a[1] = 2
# a[2] = 3
# 
# keys = [1, 2, 3]
# 
# try:
#   vs = [ a[k] for k in keys  ]
# except KeyError as e:
#   sys.exit(e)


myvar = tf.get_variable('myvar', [2,2])

# with tf.variable_scope('myvars', reuse=tf.AUTO_REUSE):
#   my_local = tf.get_variable("my_local", shape=(),
#   collections=[tf.GraphKeys.LOCAL_VARIABLES], trainable=False)
#   
#   
# tf.add_to_collection("my_collection_name", my_local)
# 
# tf.get_collection('my_collection_name')
# 
# 
# with tf.device("/device:GPU:1"):
#   v = tf.get_variable("v", [1])
#   
# cluster_spec = {
#     "ps": ["ps0:2222", "ps1:2222"],
#     "worker": ["worker0:2222", "worker1:2222", "worker2:2222"]}
# with tf.device(tf.train.replica_device_setter(cluster=cluster_spec)):
#   v = tf.get_variable("v1", shape=[20, 20])  # this variable is placed
#                                             # in the parameter server
#                                             # by the replica_device_setter
                                            
sess = tf.Session()

print('myvar: ', myvar)

sess.run(myvar.initializer)                

print('myvar: ',sess.run (myvar) )

print(sess.run(tf.report_uninitialized_variables()))
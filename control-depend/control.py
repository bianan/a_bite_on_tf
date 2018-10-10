import tensorflow as tf

# We define our Variables and placeholders
x = tf.placeholder(tf.int32, shape=[], name='x')
y = tf.Variable(2, dtype=tf.int32)

# We set our assign op
assign_op = tf.assign(y, y + 1)

mul = tf.assign(y, 2*y )

# We build our multiplication, but this time, inside a control depedency scheme!
with tf.control_dependencies([assign_op, mul]):
    # Now, we are under the dependency scope:
    # All the operations happening here will only happens after 
    # the "assign_op" has been computed first
    out = x * y

with tf.Session() as sess:
  sess.run(tf.global_variables_initializer())
  
  for i in range(3):
    print('output:', sess.run(out, feed_dict={x: 1}))
import tensorflow as tf
TRAINING_STEPS = 10
LEARNING_RATE = 0.4
x = tf.Variable(tf.constant(5, dtype=tf.float32), name="x")
y = tf.square(x)

train_op = tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(y)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(TRAINING_STEPS):
        sess.run(train_op)
        x_value = sess.run(x)
        print("After %s iteration(s): x%s is %f."% (i+1, i+1, x_value))
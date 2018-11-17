import tensorflow as tf
from numpy.random import RandomState

# 1. 定义神经网络的参数，输入和输出节点。
batch_size = 10
w1 = tf.Variable(tf.random_normal([100, 100], stddev=1, seed=1))    # 建立100 * 100 权重矩阵
w2 = tf.Variable(tf.random_normal([100, 1], stddev=1, seed=1))
x = tf.placeholder(tf.float32, shape=(None, 100), name="x-input")
y_= tf.placeholder(tf.float32, shape=(None, 1), name="y-input")

# 2. 定义前向传播过程，损失函数及反向传播算法。
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)
y = tf.sigmoid(y)
cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0))  + (1 - y_) * tf.log(tf.clip_by_value(1 - y, 1e-10, 1.0)))

learning_rate = 0.001
train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)

# 3. 生成模拟数据集。
rmd = RandomState(1)
X = rmd.rand(1000, 100)

Y = [[int(x < X.mean())] for x in X.mean(axis=1)]

# 4. 创建一个会话来运行TensorFlow程序。
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)

    # 输出目前（未经训练）的参数取值。
    print("Weight before training")
    print('W1', sess.run(w1))
    print('W2', sess.run(w2))
    print("\n")

    # 训练模型。
    STEPS = 50000
    for i in range(STEPS):
        start  = (i * batch_size) % 100
        end = (i*batch_size) % 100 + batch_size
        sess.run([train_step, y, y_], feed_dict={x: X[start:end], y_: Y[start:end]})
        if i % 1000 == 0:
            total_cross_entropy = sess.run(cross_entropy, feed_dict={x: X, y_: Y})
            print("After %d training step(s), cross entropy on all data is %g" % (i, total_cross_entropy))

        # 输出训练后的参数取值。
    print("\nWeight after Training")
    print('W1', sess.run(w1))
    print('W2', sess.run(w2))
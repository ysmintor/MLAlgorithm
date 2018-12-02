import tensorflow as tf
import mnist_inference
import os
import pandas as pd
import numpy as np

DATA_SEMEION_DATA = '/Users/york/MasterCourse/数据分析工具实践/Assignments/第10次作业/data/semeion.data'

BATCH_SIZE = 100
LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99
REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 50000
MOVING_AVERAGE_DECAY = 0.99
MODEL_SAVE_PATH = "/Users/york/MasterCourse/数据分析工具实践/Assignments/第10次作业/data/MNIST_model/"
MODEL_NAME = "mnist_model"


def train(semeion):
    # 定义输入输出placeholder。
    x = tf.placeholder(tf.float32, [None, mnist_inference.INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, mnist_inference.OUTPUT_NODE], name='y-input')

    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    y = mnist_inference.inference(x, regularizer)
    global_step = tf.Variable(0, trainable=False)

    # 定义损失函数、学习率、滑动平均操作以及训练过程。
    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    variables_averages_op = variable_averages.apply(tf.trainable_variables())
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    loss = cross_entropy_mean + tf.add_n(tf.get_collection('losses'))
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,
        global_step,
        semeion.num_examples / BATCH_SIZE, LEARNING_RATE_DECAY,
        staircase=True)
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)
    with tf.control_dependencies([train_step, variables_averages_op]):
        train_op = tf.no_op(name='train')

    # 初始化TensorFlow持久化类。
    saver = tf.train.Saver()
    with tf.Session() as sess:
        tf.global_variables_initializer().run()

        for i in range(TRAINING_STEPS):
            xs, ys = semeion.next_batch(BATCH_SIZE)
            _, loss_value, step = sess.run([train_op, loss, global_step], feed_dict={x: xs, y_: ys})
            if i % 1000 == 0:
                print("After %d training step(s), loss on training batch is %g." % (step, loss_value))
                saver.save(sess, os.path.join(MODEL_SAVE_PATH, MODEL_NAME), global_step=global_step)

def main(argv=None):
    # 使用pandas 加载数据
    data = pd.read_csv(DATA_SEMEION_DATA, sep='\s+', header=None)
    feature_num = 256
    label_num = 10
    # 分离特征 和 标签
    train_data = data.iloc[:, range(feature_num)]
    label_data = data.iloc[:, range(-label_num, 0)]
    train_array = train_data.values
    label_array = label_data.values

    semeion = SEMEIONDATA(train_array, label_array)
    train(semeion)

"""
定义 semeion 数据集类，方便在多轮训练过程中对数据进行打乱，取一批数据喂入神经网络
"""
class SEMEIONDATA:
    def __init__(self, train, label):
        self._images = train
        self._labels = label
        self._num_examples = self._images.shape[0]
        self._epochs_completed = 0
        self._index_in_epoch = 0

    @property
    def num_examples(self):
        return self._num_examples

    def next_batch(self, batch_size):
        """Return the next `batch_size` examples from this data set."""
        start = self._index_in_epoch
        self._index_in_epoch += batch_size

        if self._index_in_epoch > self._num_examples:
            # 完成一轮所有数据喂入，设置完成数
            self._epochs_completed += 1
            # 打乱数据顺序
            perm = np.arange(self._num_examples)
            np.random.shuffle(perm)
            self._images= self._images[perm]
            self._labels = self._labels[perm]
            # 开始下一轮
            start = 0
            self._index_in_epoch = batch_size
            assert batch_size <= self._num_examples
        end = self._index_in_epoch
        return self._images[start:end], self._labels[start:end]

if __name__ == '__main__':
    main()
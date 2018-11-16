import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


# 数据集
features = []
labels = []
with open('iris.csv') as f:
    for line in f.readlines():
        line = line.strip().split(',')
        features.append([float(line[0]), float(line[1]), float(line[2]), float(line[3])])
        labels.append(float(line[4]))

features = np.array(features)
vmin = features.min()
vmax = features.max()
features = (features - vmin) / (vmax - vmin)
labels = np.array(labels)
# print(features)


learning_rate = 0.15
training_epoch = 100
display_step = 10
example_to_show = 10
n_input = 4
n_output = 4

data = tf.data.Dataset.from_tensor_slices((features, labels))

# tf Graph input
X = tf.placeholder("float", [None, n_input])
y = tf.placeholder('float', [None, n_output])

# 使用字典存储隐藏层参数
n_hidden_1 = 7
n_hidden_2 = 3
# 权重和偏置的变化 在解码层和编码层顺序是相逆的
# 权重参数矩阵大小是每层的 输入*输出
# 偏置参数矩阵维度为输出层的单元数
weights = {
      'encoder_h1': tf.Variable(tf.random.normal([n_input, n_hidden_1])),
      'encoder_h2': tf.Variable(tf.random.normal([n_hidden_1, n_hidden_2])),
      'decoder_h1': tf.Variable(tf.random.normal([n_hidden_2, n_hidden_1])),
      'decoder_h2': tf.Variable(tf.random.normal([n_hidden_1, n_output])),
}
biases = {
     'encoder_b1': tf.Variable(tf.random.normal([n_hidden_1])),
     'encoder_b2': tf.Variable(tf.random.normal([n_hidden_2])),
     'decoder_b1': tf.Variable(tf.random.normal([n_hidden_1])),
     'decoder_b2': tf.Variable(tf.random.normal([n_output]))
}

def encoder(x):
    '''
    编码器
    每一层结构都是 xW+b
    :param x:
    :return:
    '''
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']),
                                   biases['encoder_b1']))
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']),
                                   biases['encoder_b2']))
    return layer_2

def decoder(x):
    '''
    解码器
    :param x:
    :return:
    '''
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['decoder_h1']),
                                   biases['decoder_b1']))
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['decoder_h2']),
                                   biases['decoder_b2']))
    return layer_2


# 构建模型
encoder_op = encoder(X)
decoder_op = decoder(encoder_op)

# 预测
y_pred = decoder_op
y_true = X

# 定义代价函数和优化方法
# 最小二乘法
cost = tf.reduce_mean(tf.pow(y_true - y_pred, 2))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

    for epoch in range(training_epoch):
        _, c = sess.run([optimizer, cost], feed_dict={X: features})

        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch + 1), 'cost=', "{:.9f}".format(c))
    print("Optimization Finished")

    encode_decode = sess.run(
        y_pred, feed_dict={X: features}
    )

fig, axes = plt.subplots(2, 10)
for i in range(example_to_show):
    axes[0][i].imshow(np.reshape(features[14*i], (2, 2)))
    axes[1][i].imshow(np.reshape(encode_decode[14*i], (2, 2)))

for i in range(example_to_show):
    print(features[14*i], encode_decode[14*i], '\n')

plt.show()



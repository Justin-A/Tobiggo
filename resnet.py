import tensorflow as tf
import numpy as np
import tensorflow.contrib.slim as slim

class deep3():
    def __init__(self, game):
        self.board_x, self.board_y = game.getboardsize()
        self.actionsize = game.actionsize()
        self.total_layers = 5
        self.input_layer = tf.placeholder(shape=[None, self.board_x, self.board_y], dtype=tf.float32, name="input")


    def resUnit(self, input_layer, i):
        with tf.variable_scope("res_unit" + str(i)):
            part = slim.conv2d(tf.nn.relu(slim.batch_norm(input_layer, activation_fn=None)), 32, [3, 3],
                               activation_fn=None)
            part2 = slim.conv2d(tf.nn.relu(slim.batch_norm(part, activation_fn=None)), 32, [3, 3],
                               activation_fn=None)
            output = input_layer + part2
            return output

    def calculate_loss(self):
        self.target_pis = tf.placeholder("float", shape=[None, self.actionsize])
        self.target_vs = tf.placeholder("float", shape=[None])
        self.loss_pi = tf.losses.softmax_cross_entropy(self.target_pis, self.pi)
        self.loss_v = tf.losses.mean_squared_error(self.target_vs, tf.reshape(self.v, shape=[-1, ]))
        self.total_loss = self.loss_pi + self.loss_v
        update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
        with tf.control_dependencies(update_ops):
            self.train_step = tf.train.AdamOptimizer(0.001).minimize(self.total_loss)




layer1 = slim.conv2d(input_layer, 64, [3, 3], normalizer_fn=slim.batch_norm, scope='conv_' + str(0))
for i in range(5):
    for j in range(units_between_stride):
        layer1 = resUnit(layer1, j + (i * units_between_stride))
    layer1 = slim.conv2d(layer1, 64, [3, 3], stride=[2, 2], normalizer_fn=slim.batch_norm, scope='conv_s_' + str(i))

top = slim.conv2d(layer1, 10, [3, 3], normalizer_fn=slim.batch_norm, activation_fn=None, scope='conv_top')

output = slim.layers.softmax(slim.layers.flatten(top))

#loss = tf.reduce_mean(-tf.reduce_sum(label_oh * tf.log(output) + 1e-10, reduction_indices=[1]))

#trainer = tf.train.AdamOptimizer(learning_rate=0.001)
#update = trainer.minimize(loss)

#total_layers = 25  # Specify how deep we want our network
#units_between_stride = total_layers / 5

#def resUnit(input_layer, i):
#    with tf.variable_scope("res_unit" + str(i)):
#        part2 = tf.nn.relu(slim.batch_norm(input_layer, activation_fn=None))
#        part3 = slim.conv2d(part2, 64, [3, 3], activation_fn=None)
#        part4 = slim.batch_norm(part3, activation_fn=None)
#        part5 = tf.nn.relu(part4)
#        part6 = slim.conv2d(part5, 64, [3, 3], activation_fn=None)
#        output = input_layer + part6
#        return output

#tf.reset_default_graph()

#input_layer = tf.placeholder(shape=[None, 32, 32, 3], dtype=tf.float32, name='input')
#label_layer = tf.placeholder(shape=[None], dtype=tf.int32)
#label_oh = slim.layers.one_hot_encoding(label_layer, 10)

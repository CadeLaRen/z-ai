import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(10.0)

addition = a + b
multiplication = tf.mul(a ,b)

with tf.Session() as sess:
    ta = tf.convert_to_tensor(a)
    print(sess.run([addition, multiplication]))

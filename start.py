import tensorflow as tf
import numpy as np 

trainX = np.linspace(-1, 1, 101)
trainY = 3 * trainX + np.random.randn(*trainX.shape) * 0.33

 
X = tf.placeholder("float")
Y = tf.placeholder("float")

w = tf.Variable(0.0,name='weights')
y_model= tf.multiply(X,w)

cost= (tf.pow( Y - y_model,2))

train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

init_op=tf.global_variables_initializer()


with tf.Session() as sess :
     sess.run(init_op)
     for i in range(100):
          for (x,y)in zip(trainX ,trainY):
            sess.run(train_op , feed_dict={X:x , Y:y} )
     print(sess.run(w))
     
  
'''     
graph=tf.get_default_graph()
for op in graph.get_operations():
    print(op.name)
'''

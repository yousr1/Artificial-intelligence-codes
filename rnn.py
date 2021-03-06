import tensorflow as tf
from tensorflow.contrib import rnn 
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/" , one_hot=True)
# 10 classes ,0-9
hm_epochs=3
n_classes=10
batch_size=128

chunk_size=28
n_chunks=28
rnn_size=128

# height(gray)* width(28*28)
x=tf.placeholder('float',[None,n_chunks,chunk_size])
y=tf.placeholder('float')

def recurrent_neural_network_model(x):
    #(input_data *weights + biases)
   layer={ 'weights':tf.Variable(tf.random_normal([rnn_size,n_classes])),'biases':tf.Variable(tf.random_normal([n_classes])) }
   x=tf.transpose(x,[1,0,2])
   x=tf.reshape(x,[-1,chunk_size])
   x=tf.split(x,n_chunks,0)

   lstm_cell = rnn.BasicLSTMCell(rnn_size) 
   outputs, states = rnn.static_rnn(lstm_cell, x, dtype=tf.float32)
   output= tf.add( tf.matmul(outputs[-1] ,layer['weights']) , layer['biases'] )

   return output
def train_neural_network(x):
        prediction = recurrent_neural_network_model(x)
        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction,labels=y) )
        # learning rate=0.01
        optimizer=tf.train.AdamOptimizer().minimize(cost)
   

        with tf.Session() as sess :
                     
                     sess.run(tf.global_variables_initializer())
                     
                     for epoch in range(hm_epochs) :
                        epoch_loss=0
                        #how many cycles of images does it take for 1 epoch
                        for _ in range(int(mnist.train.num_examples/batch_size)):
                           #chunks the images into no of batches
                           epoch_x, epoch_y = mnist.train.next_batch(batch_size)
                           epoch_x=epoch_x.reshape((batch_size,n_chunks,chunk_size))
                           _,c = sess.run([optimizer,cost] , feed_dict = {x:epoch_x,y:epoch_y} )
                           epoch_loss+= c
                        print('epoch',epoch,'completed out of',hm_epochs,'loss:',epoch_loss)

                     
                     correct = tf.equal(tf.argmax(prediction,1),tf.argmax(y,1))
                     accuracy = tf.reduce_mean(tf.cast(correct,'float'))
                     print('accuracy',accuracy.eval({x:mnist.test.images.reshape((-1,n_chunks,chunk_size)),y:mnist.test.labels}))
                           
train_neural_network(x)
                     
                          
                         
                     
                     
  
                     
                     

                     



                 

 

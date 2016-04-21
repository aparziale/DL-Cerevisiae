import preprocess as p
import rbm
import tensorflow as tf
import numpy as np


input_matrix, labels = p.main()

print "Input matrix shape = ", input_matrix.shape[0]
print "labels shape = ", labels.shape[0]


print labels[0, 0:10]

#for row in input_matrix:
visible = input_matrix[0]
hidden = labels[0]
vis = tf.Variable(visible)
r = rbm.RBM("chr0.0",visible.shape[0], hidden.shape[0])

with tf.Session() as session:
        # Run the model
    #session.run(r)
    session.run(r.propup(vis))
    # Run just the variable y and print 
    #print(session.run(y))
    

#sess.Run(rbm 

#x = RBM("test", 
#rbm = tf.Variable(x+5, name = 'y')
#sess = tf.Session()
#sess.Run(

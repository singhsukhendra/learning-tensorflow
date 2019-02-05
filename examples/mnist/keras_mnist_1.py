
'''
Basic Keras Code for a multi-layer neural network
'''

# Training Parameters
epochs = 10

# Network Parameters
WIDTH = 28; HEIGHT = 28; 
NUM_OUTPUTS = 10 

import time
import tensorflow as tf
import matplotlib.pyplot as plt
mnist = tf.keras.datasets.mnist

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(HEIGHT, WIDTH)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(NUM_OUTPUTS, activation=tf.nn.softmax)
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.summary()

start = time.time();
history = model.fit(x_train, y_train, epochs=10, validation_split=0.2, shuffle=True)
evaluation = model.evaluate(x_test, y_test, verbose=1)
end = time.time()
print("Training Complete in " + "{0:.2f}".format(end - start) + " secs" )

# Plot Accuracy 
plt.plot(history.history["acc"]);
plt.plot(history.history["val_acc"]);
plt.ylabel("Accuracy")
plt.xlabel("Epochs")
plt.legend(["Train Accuracy", "Test Accuracy"], loc="upper left")
plt.show();

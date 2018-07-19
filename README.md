# Learning Tensorflow
This tutorial was created for learning tensorflow by example. Currently this repo contains examples for a simple single-layer neural network, a multi-layered perception neural network, and a convolutional neural network. Tensorflow implementations in this repo work with a variety of data sets. Keras implmentations are also included as a comparison for some cases. (Code tested with python 2.7/3.2 using tensorflow 1.3 and keras 2.0)

# Examples
Examples of tensorflow implementations for Classification, Segmentation, Regression and Modeling Fourier Transform

## Classification
A variety of neural network implementations for MNIST, and CFAR-10 datasets for classification

### MNIST
- Basic Neural Network ([tutorial](notebooks/mnist/0_Single_Layer_Network_Tutorial.ipynb), [tensorflow](examples/mnist/basic_net.py)) - A simple (single layer preception) network for classifying MNIST dataset 
- Multi-layer Neural Nework ([tensorflow](examples/mnist/mlp_net.py)) - A simple (multi-layer preception) network for classifying MNIST dataset 
- Convolutional Neural Nework ([tensorflow](examples/mnist/conv_net.py)) - A convolutional network for classifying MNIST dataset 

### CIFAR-10
- Basic Neural Network ([tensorflow](examples/cifar/basic_net.py), [keras](examples/cifar/keras_basic.py)) - A simple (single layer preception) network for classifying CIFAR-10 dataset 
- Multi-layer Neural Nework ([tensorflow](examples/cifar/mlp_net.py), [keras](examples/cifar/keras_mlp.py)) - A simple (multi-layer preception) network for classifying CIFAR-10 dataset 
- Convolutional Neural Nework ([tensorflow](examples/cifar/conv_net.py), [keras](examples/cifar/keras_conv.py)) - A convolutional network for classifying CIFAR-10 dataset
- Convolutional Neural Nework ([keras](examples/cifar/keras_nine_layer_conv.py)) - A convolutional network (6-conv, 3 max pool, 2 fully-connected layers) with Dropout for classifying CIFAR-10 dataset 
- VGG network ([keras](examples/cifar/keras_vgg.py), [paper](https://arxiv.org/pdf/1409.1556v6.pdf)) - A very deep convolutional network for large-scale image recongition

## Segmentation
Tensorflow implementation for simple color segmentation ([tensorflow](examples/color/segmentation.py))

## Regression
Neural network implementations for linear ([tensorflow](examples/regression/linear_regression.py)) and non-linear regressions ([tensorflow](examples/regression/non_linear_regression.py))

## Modeling Fourier Transform / FFT
Neural netowrk implementation for learning a fourier transform ([tensorflow](examples/fft/fft.py))


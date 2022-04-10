import keras
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical

#1导入mnist数据集
(train_images,train_labels),(test_images,test_labels)=mnist.load_data()

#2网络架构
network=models.Sequential()
network.add(layers.Dense(512,activation='relu',input_shape(28*28, )))
network.add(layers.Dense(10,activation='softmax'))
network.sumary()   #查看每层参数估计数量

#3编译步骤
network.compile(optimizer='rmsprop',
               loss='categorical_crossentropy',
               metrics=['accuracy'])

#4准备图像数据--预处理
train_images=train_images.reshape((60000,28*28))
train_images=train_astype('float32')/255

test_images=test_images.reshape((10000,28*28))
test_images=test_images.astype('float32')/255

#5准备标签
train_labels=to_categorical(train_labels)
test_labels=to_categorical(test_labels)

network.fit(train_images,train_labels,epochs=5,batch_size=128)
print(keras.__version__)


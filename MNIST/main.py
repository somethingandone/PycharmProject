from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPool2D
from keras.layers import Flatten
from keras.layers import Dense

# 进行数据的获取
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# 进行数据的规范化
train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))
# 将图片转化到（0， 1）通道上
train_images, test_images = train_images / 255.0, test_images / 255.0
# 建立顺序模型
model = Sequential()
# 第一层卷积层，指32个filter，大小为3*3，激活函数为relu，输入图片宽、高为28，深度为1
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
# 池化层filter，大小为2*2
model.add(MaxPool2D(2, 2))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPool2D(2, 2))
model.add(Conv2D(64, (3, 3), activation='relu'))
# 添加全连接层
model.add(Flatten())
# 第一个全连接层
model.add(Dense(128, activation='relu'))
# 输出层
model.add(Dense(10, activation='softmax'))
# 编译模型，需要损失值、识别精度、优化方法
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# 开始训练模型，epochs为训练轮数
model.fit(train_images, train_labels, epochs=10)
# 导入验证数据，并得出测试结果
test_loss, test_acc = model.evaluate(test_images, test_labels)
# 打印准确性
print("Test Accuracy: ", test_acc)

import tensorﬂow as tf
import numpy as np
from tensorﬂow.keras import Sequential
from tensorﬂow.keras.layers import Dense

# Layers configuration. 
# - Dense is a layer of fully connected neurons.
# - units indicate neurons, 1 ins this case.
# - input shape is 1, because the input is just X to guess Y
l0 = Dense(units=1, input_shape=[1])
model = Sequential([l0])

# Model compilation
# - Optimizer is Stochoastic Gradient Descent optimizer: Given values, previopus guess and 
# loss, it will try to minimize the loss in the next guess
# - Loss is mean squared error, which is the difference between the real value and the predicted value squared
model.compile(optimizer='sgd', loss='mean_squared_error')

# Data
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=ﬂoat)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=ﬂoat)

# Model training. Input data and repetitions
model.ﬁt(xs, ys, epochs=500)

# Predict the Y for X=10
print(model.predict([10.0]))
print("Here is what I learned: {}".format(l0.get_weights()))
# Deep Neural Networks

Neural networks is in the heart of Deep Learning. They are composed of perceptrons, that take inputs and outputs a value of one or zero.

Each perceptron has a boundary line with equation

$$w1x1 + w2x2 + b = 0$$

We can also simplify by calling W and x vectors W = (w1, w2) and  x = (x1, x2), so:

$$Wx + b = 0$$

This formula still works in higher dimensions, because W and x are a collection of all vectors (W = (w1, w2..., wn)).

Each training point has a label y that can be 0 or 1 that we are trying to predict. ŷ is the prediction, with formula:
 
$$\hat y = 1 \Rightarrow Wx + b \geq 1$$
$$\hat y = 0 \Rightarrow Wx + b \lt 1$$

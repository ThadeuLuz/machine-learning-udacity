# Deep Neural Networks

Neural networks is in the heart of Deep Learning. They are composed of perceptrons, that take inputs and outputs a value of one or zero.

Each perceptron has a boundary line with equation

$$w1x1 + w2x2 + b = 0$$

We can also simplify by calling W and x vectors W = (w1, w2) and  x = (x1, x2), so:

$$Wx + b = 0$$

This formula still works in higher dimensions, because W and x are a collection of all vectors (W = (w1, w2..., wn)).

Each training point has a label y that can be 0 or 1 that we are trying to predict. ŷ is the prediction, with formula:

$$
\hat y = \begin{cases}
   1 &\text{if } Wx + b \geq 1  \\
   0 &\text{if } Wx + b \lt 1
\end{cases}
$$

Perceptrons can be used for logical operations OR or AND on two inputs. It also can be used to more complex operations like Xor with two layers.
### Perceptron trick algorithm

1. Start with random weights
1. For every misclassified point:
  1. If prediction = 0:
    For i = 1 ...n
      change wi + xi * a (add the value of Xi times the learning rate)
  2. If prediction = 1:
    For i = 1 ...n
      change wi - xi * a (subtract the value of Xi times the learning rate)
    
We can also change the Activation function from a discreet step function (that returns only 0 or 1) to a continuous sigmoid function (that returns any number between 0 and 1). The sigmoid formula is:

$$\sigma (x) = \frac {1} {1+ e^{-x}} $$

and the new continuous prediction is 

$$ \hat y = \sigma(Wx + b)$$

which will return the chance of the lable being true


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

### Softmax

When we have a classification problem, the solution would be to apply a softmax function. For *Z1, ..., Zn* being the scores of the function, the softmax function is:

$$\hat y = \frac {e ^{Zi}} {e^{Z1} + ... + e^{Zn}}$$

### Maximum Likelihood

Maximum likelihood is the method of detecting the efficiency of a model by multiplying the probability of each event having the label it has. So for example:

A good model has a high Maximum Likelihood
$$ 0.7 * 0.9 * 0.8 * 0.6 = 0.3024$$ 

A bad model has a low Maximum Likelihood
$$ 0.6 * 0.2 * 0.1 * 0.7 = 0.0084$$ 

Our goal is to maximize the Maximum Likelihood.

### Cross Entropy

Instead of multiplying the probabilities of all points, it would be better to add them, and avoid getting stuck with very small numbers. Remember logs are just the inverse operations to exponential:

$$log_e(x) = y  \text{ as }  x = e^y$$

Since logs of numbers bellow 1 are negative, we can make them negative to end up with a positive number. For example, the cross entropy of the example above would be

A GOOD model has a LOW Cross Entropy
$$ -ln(0.7) - ln(0.9) - ln(0.8) - ln(0.6) = 1.2 $$ 

A BAD model has a HIGH Cross Entropy
$$ -ln(0.6) - ln(0.2) - ln(0.1) - ln(0.7) = 4.8 $$ 

Our goal is to minimize the Cross Entropy.









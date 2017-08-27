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

Natural logs are just logs of *e*, which is a constant (2.71828...):

$$ log_{2.71828...}(x) = log_e(x) = ln(x)$$

Since logs of numbers bellow 1 are negative, we can make them negative to end up with a positive number. For example, the cross entropy of the example above would be

A GOOD model has a LOW Cross Entropy
$$ -ln(0.7) - ln(0.9) - ln(0.8) - ln(0.6) = 1.2 $$ 

A BAD model has a HIGH Cross Entropy
$$ -ln(0.6) - ln(0.2) - ln(0.1) - ln(0.7) = 4.8 $$ 

Our goal is to minimize the Cross Entropy.

The final formula for cross entropy also encompasses the fact that we sould invert the probability of a label being positive if the outcome was negative. The formula is:

$$ \text{Cross Entropy} = - \sum_{i=1}^m y_iln(p_i) + (1-y_i)ln(1-p_i) $$

### Multi Class Cross Entropy

If we are trying to calculate the cross entropy for multiple clasess, the formula is:

$$ \text{Cross Entropy} = - \sum_{i=1}^n \sum_{j=1}^m y_{ij} ln(p_{ij}) $$

This works because $y_{ij}$ being 0 or 1 cancels the values of events that did not occur.

### Error Function

The only thing we have to do to get our final error function is to divide the Cross Entropy by the number of points. Also, our formula is calculated on the prediction ($\hat y$) instead of ($p$), the formula is:

$$ 
\text{Error Function} = - \frac 1 m \sum_{i=1}^m (1-y_i)(ln(1-  {\hat y}_i)) + y_iln({\hat y}_i) 
$$

To put the formula in terms of W and b:

$$ 
E(W, b) = - \frac 1 m \sum_{i=1}^m (1-y_i)(ln(1 -  \sigma(Wx^{(i)} + b))) + y_iln(\sigma(Wx^{(i)} + b))
$$

This is the formula for a binary classification problem. The formula for a multi-class classification formula in terms of W and b is:

$$ 
\text{Cross Entropy} = - \sum_{i=1}^n \sum_{j=1}^m y_{ij} ln(\sigma(Wx^{(ij)} + b)))
$$

### Minimizing errors

The first thing to do is to calculate the derivative of the error function.

$$
\sigma'(x) = \sigma(x)(1 - \sigma(x))
$$

Our goal is to calculate the gradient of $E$, at point $x = (x_1, ..., x_n)$, given by the parcial derivatives

$$
\nabla E = \begin{pmatrix}
  \frac \partial {\partial_{w1}} E, 
  ...,
  \frac \partial {\partial_{wn}} E, 
  \frac \partial {\partial_{b}} E
\end{pmatrix}
$$

To calculate $\frac \partial {\partial_{wj} } E$, we end up with:

$$
\frac \partial {\partial_{b} } E = \frac 1 m \sum^m_{i=1}(y_i - \hat y_i)
$$

This means that for a point with coordinates $(x_1, ..., x_n)$, label $y$, and prediction $\hat y$, the gradient of the error function at that point is $((y - \hat y)x_1, ..., (y - \hat y)x_n, (y - \hat y))$. In summary:

$$
\nabla E (W, b) = (y - \hat y)(x_1, ..., x_n, 1)
$$

### Gradient Descent

Pseudocode for gradient descent:

1. Start with random weights: $(w_1, ..., w_n, b)$
1. For every point $(x_1, ..., x_n)$:
    1. For $i = 1 ... n$
        1. Update $w'_i \longleftarrow w_i - \alpha (y- \hat y)x_i$ 
        1. Update $b' \longleftarrow b - \alpha (y- \hat y)$ 


### Deep Neural Networks

The word 'Deep' comes to neural networks when we add layers of perceptrons other then the ones directly connected to the input. These subsequent layers will have the outputs of the first layer as inputs, and they allow for more complex models. When we have classification problems we can add one node for each class on the output, and their values (after a softmax function) will correspond to the probability of each class being of that label.


## Supervised learning Tasks

Most of the content on this section was taken already from other courses, so I skipped most of it.

The term "regression" comes from the "regression to the mean", which means that in some contexts (like people's height) diferent mesurements tend to move closer to the mean. The term started being used to describe the action of finding a mathematical relationship  between several measurement points.

The test set is just a stand in for data we are going to see in the future. We are assuming that the test data is going to be representative of the data we are going to use the model in. Statisticians like to call it *Independent and Identically Distributed* it **IID** that is a *fundamental assumption* of a lot of the algorythims we are using.

The main difference between K nearest neighbor and kernel regression is that in KR the points are weighted in accordance to how distant they arem and on KNN they get an equal weight.

Parametric models have the goals of finding parameters, discard the data and then use the parameters to make predictions. KNN and KR are examples of nonparametric models, where we use the data to make predictions.

For parametric (biased) advantages
- Querying is fast
- Lighter (no data needs to be stored)
- Best for mathematically explainable data sets

For nonparametric (unbiased) advantages
- No training
- Can add new data easily
- Good for chaotic data sets

## Decision trees

Terms: 

- Instances - Vectors of atributes that define whatever the input space is (pixels, credit scores).
- Concepts - A concept is an idea that describes a set of things. In ML, concept the function that maps the inputs to it's membership to a set.
- Target Concept - The actual concept we are trying to find.
- Hypothesis Class - Or Hypothesis Class. These are all possible functions that we consider possible answers.
- Sample - The training set. The set of all inputs paired with their outputs.
- Candidate - The concept that you thing might be the target concept.
- Testing Set - Separate set which will be used to evaluate the functions.

Decision trees can represent boolean functions, like and OR function:

<img src='http://g.gravizo.com/g?
 digraph G {
   a [label="A"];
   t1 [label="True" shape=box];
   b [label="B"];
   t2 [label="True" shape=box];
   f1 [label="False" shape=box];
   a -> t1 [label=true]
   a -> b [label=false]
   b -> t2 [label=true]
   b -> f1 [label=false]
 }
'/>

Or a XOR function 

<img src='http://g.gravizo.com/g?
 digraph G {
   a [label="A"];
   b1 [label="B"];
   b2 [label="B"];
   t1 [label="True" shape=box];
   t2 [label="True" shape=box];
   f1 [label="False" shape=box];
   f2 [label="False" shape=box];
   a -> b1 [label=true]
   a -> b2 [label=false]
   b1 -> f1 [label=true]
   b1 -> t1 [label=false]
   b2 -> t2 [label=true]
   b2 -> f2 [label=false]
 }
'/>

The first tree grows linearly to the number of options. The second grows exponentially.

The way to maximize information gain is to decrease entropy after splititng the dataset.

ID3 is a top down learning algorithm that maximizes for entropy (uncertainty) to decide how to split the data.

## Artificial Neural Networks

ANN are made up of perceptrons. They look like this:

![Perceptron](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/ArtificialNeuronModel_english.png/600px-ArtificialNeuronModel_english.png)

`W` are the weights multiplying inputs. `θ` is the treshold for the output.

There are two different rules to figure out weights from examples: 

### Perceptron Rule 
Perceptron Rule  makes use of thresholded output. First it gets rid of the treshold (or better said, it always uses a threshold of 0) by modifying the weights account for it. To train the weights based on examples it basically loops throught the weights and compares the acual value to the value of the examples, then nudges the weight to the right direction by multiplying it to a *learning rate* variable. 

### Gradient descent/Delta rule 
Gradient descent makes use of unthresholded output. It is more robust to addres non linear-separability. It looks a lot like the perceptron rule, but instead of thesholding to figure out only the direction a weight should move, it moves by a factor of the error.

Usually the initial weights are small randomized values, to start simple and avoid getting stuck at the same local minimum multiple times when training different models.

[This series is awesome](https://www.youtube.com/watch?v=bxe2T-V8XRs)

## Support Vector Machines

Support vector machines is an algorithm that aims to find a hyperplane that separates the different labels of data and to maximize the distance between them. Support vectors are the closest points that interfere with the hyperplane. It may use a kernel trick, which will create a new similarity metric that can help to separate the data in other dimensions.

## Nonparametric Models

Instance Based learning are a different class of learning algorithms. Instead of deriving a function and discarding the data, it keeps the data and uses it directly. The term 'lazy-learners' (as opposed to 'eager-learners') is used to describe these algorythm that shift computation from the training step to the actual query.

### NN
Nearest neightbors algorythms is the simplest non-parametric model. You just store the data point in a database and query for 1 (1-NN) or K (K-NN) nearest points and make your guess based on their labels. If you have more than one answer, you can average (regression) or vote (classification) on the correct label. Their vote can be weightd by the distance. Distance can be euclidian, manhattan or whatever you decide.

## Bayesian Methods

Bayes Rule:

![](http://www.gaussianwaves.com/gaussianwaves/wp-content/uploads/2013/10/Bayes_theorem_1.png)


## Ensemble of Learners

Bagging is just generating regression polynomials from different subsets of data (randomly picked) and averaging out the results. It's remarkable that the results seem to do better than deriving an equation from the entire set (possibly because it avoids overfitting).

## Supervised Learning Project

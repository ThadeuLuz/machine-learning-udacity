
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

## Support Vector Machines

## Nonparametric Models

## Bayesian Methods

## Ensemble of Learners

## Supervised Learning Project

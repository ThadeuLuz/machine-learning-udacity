## Clustering

## Feature Engineering

### Feature Scaling

Feature scaling is just a step to normalize  to even out the importance of features. Use this formula:

> X' = (X - Xmin) / (Xmax - Xmin)

To use in in sklearn do

    import numpy as np
    from sklearn.preprocessing import MinMaxScaler

    weights = np.array([[115.], [140.], [175.]]) # data table
    scaler = MinMaxScaler()

    rescaled_weights = scaler.fit_transform(weights)
    print rescaled_weights

### Feature Selection

Feature selection is the process of choosing some of the features that will help the most in predictions. The reason for this is basically the *curse of dimensionality*.

There are usually two approaches to solve the problem:

- Filtering: Where you run the features on some sort of algorithm that maximizes a criteria, and then hands the features to the learning algorithm. The learning algorithm is trained once, after the features are selected.

- Wrapping:  Where the step of selecting the best features uses the learning algorithm itself to determine which features are the best. The learning algorithm is trained multiple times, as a step in choosing which features are the best ones.

Bayes Optimal Classifier (or B.O.C.) is the one that takes the weighted average of all hypotheses based on the probability of being the correct hypothesis given the data. The B.O.C. is the best model that you can possibly have on average. It is 'possible' to find an algorithm that computes the B.O.C., except that requires you to look at all possibly infinite number of hypotheses.  

#### The formal definition of Relevance is

- Xi is strongly relevant if it degrades the B.O.C. (that means that strongly relevant features have information that are not on any other features)

- Xi is weakly relevant if it is 
  - not strongly relevant and
  - if added to a subset of features, it improves the B.O.C.
  - (that means that the information on the feature is on other features but may be relevant if used in conjunction with a subset of features)

- Xi is irrelevant if it is not weakly or strongly relevant

#### The definition of Usefulness

Relevance is about information. Usefulness is about the effect on error. 

## Dimesionality Reduction

### PCA (Principal Component Analysis)

Measurable features are the ones you can just look up and measure on the real world, like square footage (of a house), number of rooms or neighborhood safety. Latent features are the ones that you can't measure directly but 'drive the phenomenon that you are measuring behind the scenes'.

Variance can be defined as

- ~~the willingness of an algorithm to learn~~ (ignore that definition for now) 
- technical term in statistics - roughtly the "spread" of a data distribution (similar to standard deviation)

The **principal component** of a dataset is the direction that has the largest variance.

Working Definitions

- PCA is a systematized way to transform input features into principal components
- Use Principal components as new features
- PCs are directions in data that maximize variance (minimizing information loss) when you project/compress down onto them
- The more variance of data along a PC, the higher that PC is ranked.
- most variance/most information => first PC. Second-most variance (without overlapping w first PC) => second PC
- Max number of PCs is number of features (which will work but have no benefits)

When to use PCA

- Latent featues driving the patterns (big shots at Enron)
- Dimensionality reduction
  - Visualize high dimensional data
  - reduce noise
  - Make other algorithms (regression, classification) work better b/c fewer inputs (eigenfaces)


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

- Filtering: Where you run the features on some sort of algorythm that maximizes a criteria, and then hands the features to the learning algorythm. The learning algorythm is trained once, after the features are selected.

- Wrapping:  Where the step of selecting the best features uses the learning algorythm itself to determine which features are the best. The learning algorythm is trained multiple times, as a step in choosing which features are the best ones.
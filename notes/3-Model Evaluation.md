## Statistical Analysis

Basic statistics and numerical tools.

- Mode (range that occurs the most)
- Mean (average)
- Median (item in the middle)

Quartiles are figured out when the data points are divided equally. Q2 is the median, Q1 is the median of lower half and Q3 is median of upper half. IQR (inter quartile range) is Q3-Q1.

Outliers formula 

- < Q1 - (1.5 * IQR)
- < Q3 - (1.5 * IQR)

## Data Modeling

Data types:

- Numeric or Quantitative Data: May be continuous discreete(integers).
- Categorical Data: Represents characteristics, numbers but mathematically meaningless, may have order
- Time series: Represents time

## Evaluation and Validation

Classification Metrics

## Managing Error and Complexiy

This is very helpful: http://scott.fortmann-roe.com/docs/BiasVariance.html

Error due to Bias: 
- Means the model (line or boundary) is too simple
- Means _underfitting_: model is not complex enough
- Low scores for test and training data

Error due to Variance
- Means the model is too complex
- Means _overfitting_: model is too complex
- High scores for training data, but test data will be lower

![](http://pingax.com/wp-content/uploads/2014/05/underfitting-overfitting.png)

## Model Evaluation and Validation Project

# Ad Click Prediction

In this exercise you should build a simple classifier that can predict whether
someone will Click / Buy from an advertisement. You are free 
to use any classifier you want but it is not necessary to use a neural network
(not even recommended).

Your data is split into two files (please do not rename them)
- `ads_traindata.csv` the training data
- `ads_testdata.csv` the test data

The `task.py` file contains three functions to be implemented:
- `transform()` perform any data transformation you want here, The function
should return the transformed data.
- `train()` perform any training you want here. The data will be pre-transformed by the `transform` function you implemented.
This function should return the trained model.
- `predict(model, sample)` perform a single prediction on a sample. We will
invoke this function given the model you return from `train()` and the test dataframe.
- `validate_help()` extracts labels from your dataset, depending on your `transform` function
you may want to change this function to extract a 1d flat array of labels from a dataset.

NOTE: Our solution checks requires `sklearn` and `pandas` to be installed.

> We will check the performance of your model based on false positives and
> false negatives! You will pass if the number of false positives and false
> negatives is below some threshold on the test dataset.

> Question: Many classifiers are initialized with some random state. Because of this, 
> the same classifier can give different results/performance on different runs.
> Thus, some models may sometimes pass and sometimes fail our tests. This is
> a practical problem in real world ML/Data Science applications. How would you
> mitigate this problem?

**As always, if you struggle with the problem, ask for help in Slack or join one of our 
co-working sessions throughout the track phase!**

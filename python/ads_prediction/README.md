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
- `train()` perform any training you want here, you should also load the data
in here. The function should return the trained model.
- `predict(model, sample)` perform a single prediction on a sample. We will
invoke this function given the model you return from `train()`.

NOTE: Our solution checks requires `sklearn` and `pandas` to be installed.

> We will check the performance of your model based on false positives and
> false negatives! You will pass if the number of false positives and false
> negatives is below some threshold on the test dataset.

**As always, if you struggle with the problem, ask for help in Slack or join one of our 
co-working sessions throughout the track phase!**

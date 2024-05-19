# Outliers

In this exercise, you will find a Jupyter Notebook `task.ipynb` and a dataset
`health_insurance.csv`. Your goal is to improve the performance of the
regression model implemented in the Notebook!

First, try to understand the dataset by exploring it. Then, implement the
`remove_bad_outliers` function in the notebook to remove potential bad
outliers. Use the last cell to evaluate your work and get your key.

## How we evaluate your work

We are using simple linear regression to model the relationship between
customer features and the amount of money spent on health insurance. We will first
fit the data without removing any outliers (the original dataset) and then again
with outliers removed (by evaluating your implemented function). You will pass the 
test, if your model (with outliers removed) performs better than the original
model (Mean Squad Error) on some test dataset.

For this exercise, we will need
- Jupyter Notebook
- Pandas
- sklearn

> Bonus Question: Was this (removing potential bad outliers) a good way to
> improve regression model performance in general? Why? Why not?


**As always, if you struggle with the problem, ask for help in Slack or join one of our 
co-working sessions throughout the track phase!**

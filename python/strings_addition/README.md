# Strings Addition

> We used to name this one `galactic_food` for some reason. Don't be confused
> by the naming.

The task of this exercise is to write a function that takes a list of
strings and returns a tuple with the highest valued string and the value. 

We value the string on this metric:

- each lowercase letter `a..z` is worth `1..26` points
- each uppercase letter `A..Z` is worth `-1..-26` points
- the total value of a string is the sum of the values of its characters

Let's see an example! Given the following list of strings

``` 
hjklAJUKNnjkncjsk
klfbjALjkwnjAJJnaL
kjwnuobownuFNDIacnA
```

We can calculate the value of each string e.g. starting with the first one
`hjklAJUKNnjkncjsk`:

- `h` is valued as `8` (it is the 8th lower case character in the alphabet)
- `j` is valued as `10`  (it is the 10th lower case character in the alphabet)
- ...
- `A` is valued as `-1` (it is the 1st capital letter in the alphabet)
- `J` is valued as `-10` (it is the 10th capital letter in the alphabet)
- ...
- The sum of all values of the string is `76`

Doing this for all strings in the list we will find out that `kjwnuobownuFNDIacnA` 
is the highest valued string with a value of `153`. Thus your function should 
return the tuple `("kjwnuobownuFNDIacnA", 153)`

Go a head and implement the `galactic_food` function in the `task.py` file!

**As always, if you struggle with the problem, ask for help in Slack or join one of our 
co-working sessions throughout the track phase!**

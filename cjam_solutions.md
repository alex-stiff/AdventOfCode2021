My attempts to learn cjam via AoC

# Day 1

## Part 1

### Solution:

```
q~]_1>.-Tf<:+
```
[Try it out!](http://cjam.aditsu.net/#code=q~%5D_1%3E.-Tf%3C&input=1%0A4%0A5%0A3%0A7)

### Explanation

For test input of 1 4 5 3 7:

* `q~` Read the input `1 4 5 3 7`
* `]` Into an array `[1 4 5 3 7]`
* `_` Duplicate the array `[1 4 5 3 7] [1 4 5 3 7]`
* `1>` Remove the 1st element from the 2nd array `[1 4 5 3 7] [4 5 3 7]`
* `.-` Element-by-element subtraction `[-3 -1 2 -4 7]`
* `Tf<` For each element, check if it's less than 0 (`T` initialises to `0`) `[1 1 0 1 0]`
* `:+` Sum this array up to get number of elements less than zero `3`
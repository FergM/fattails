# Five Star Reviews are Overrated
An algorithm for finding that *best rated* place by rescaling the ones without many reviews.

Sections
* [Problem](#Problem)
* [Solution](#Solution)
* [Explanation](#Explanation)

### Problem
Ever heard of *TooGoodToGo*? It's an app for saving surplus food. Think that bakery down the road, come 4pm they are closing up but have some amazing cinnamon buns left. With *TooGoodToGo* you can find these places near you and buy *surprise* bags at a discounted price.

Great, so what? Well one day I decided, lets find the ***best*** places in London on *TooGoodToGo*. I apply my location filter, then I sort by rating out of 5. *This* is the problem.

All the 5 star places have hardly any reviews. The result has only 15 reviews. Hmm but I just want the best of the best, probably a 4.8 star with >100 reviews. What I really want though is smarter ratings, can't they also include the number of reviews as a variable. So a 4.8 star with 250 reviews comes up before a 5 star with 15 only reviews.

Aha this looks like something that can be solved using *entropy*. I just need a mapping that rescales the *"average rating"* by factoring in how many reviews the place has. If there's only one *5 star* review the *true* rating lies somewhere between population avarage (say 3 star ) and observed (5 star).

### Solution
##### Binomial Problem
* See Marcos Slides
* See Nassim Blog
* See 2023-10-04 Wolfram Notebook
    * called `2023-10-04 BLOG DRAFT Five Star Reviews are Overrated.nb`
    * copy saved in this entropy directory on dropbox

Summary
* Given p, n and x (probability, number of samples, number of successes)
* We can define the cdf for X<=x_observed
* Set p such that the observed result is a median for the CDF

##### Binomial Solved as Multinomial
See 2023-10-04 Wolfram Notebook

Summary
* We want to know p1 & p2
* We know n
* We know mean(x)
    * `mean(x) := (1*x1 + 2*x2) / n`
    * So compared to the binomial problem
        * this time x1 gets 1 instead of 0 as a value
        * And 
        * this time x2 gets 2 instead of 1 as a value
        * So
        * Overall it should be the same just nominally different
        * And
        * With 2 variables we can still find x1 as a function of x2
* We set a threshold as follows
    * `P(observed_mean_x <= p_implied_mean_x) = 0.5` <- *Equation 2*

Next Steps
* We need to Maximise entropy of the p distribution
* Under the constraint of *Equation 2*

Checks
* The answer should be equivalent to the binomial solution
* If this works then we extend out to x1,x2,x3 and then generalise to any number of dimensions.

##### Trinomial Solved as Multinomial

##### Multinomial with n dimensions

### Explanation

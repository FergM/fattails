# Intuition for *Shannon Entropy*
Sections:
* 1. [Definition of Entropy](#1-definition-of-entropy)
* 2. [How Entropy Works](#2-why-does-entropy-work)
* 3. [Multiple Dimensions](#3-multiple-dimensions)
* [Appendix](#appendix)

## 1. Definition of Entropy
Definition of [*Shannon Entropy*](https://en.wikipedia.org/wiki/Entropy_(information_theory))
, for a discrete probability distribution:
  
  ![Shannon Entropy Definition](../images/2023-10-16%20Shannon%20Entropy.png)

As a convention I will use the term **"*summand function*"** for the expression which gets added. So for *Shannon Entropy* the *summand function* is this:

  ![Shannon Entropy Summand](../images/2023-10-16%20Shannon%20Entropy%20Summand.png)

How do you apply Shannon Entropy to probability distributions:
* Problem: You want to estimate what distribution you are dealing with
* Solution: Add whatever constraints you want and then choose a probability distribution (values for *p_i*) which maximises the Shannon Entropy.
* Result: The max entropy distribution can be seen as a best guess starting point which makes the least amount of assumptions.

## 2. *Why* does Entropy Work?
To understand why/how Shannon Entropy works, you need to understand the shape of the *summand function*.

### Visual Intuition:
* The image here below plots the *summand function*. The x-axis is *p* and the y-axis is the function applied to *p*.
* Suppose you have biased coin with probabilities `p_heads` and `p_tails`. The entropy is maximised by setting `p_heads = p_tails` and this happens *because* the shape is convex.
* Suppose `p_heads`=0.2 and `p_tails`=0.8. You can visually see from the plot that moving both to the average value (0.2+0.8)/2= 0.5 gives a greater entropy.
* ***Basically entropy uses Jensen's inequality to define a principle of non-discrimination***
* In fact, you can use any function *f(p)* for entropy as long as the term is concave on the interval 0<p<1
![Entropy Intuition Plot](../images/2023-10-16%20Entropy%20Intuition%20Plot.png)

### Engineering Intuition (Thermodynamics)
Maximum entropy is equivalent to thermal equilibrium
* The *passage of time* in thermodynamics is analogous to *loss of information* in information theory
* Thermodynamics: The more time that passes the closer your system gets to thermal equilibrium
* Information Theory: The less information you have the more you should assume equilibrium (i.e. all states equally likely)

### Other

Application
* So as an application, you add constraints which resemble the problem you want to solve
* Then you use entropy and look at the space of options which have not been excluded through constraints
* And you select amongst the remaining options using entropy
* Which really means, you select by picking the least descriminatory option(s), and Shannon Entropy (or any convex *summand function*) through it's concavity applies this *principle of non discrimination* mathematically

Mathematica Notebook:
* [2023-10-14 Entropy Intuition Visualisations.nb](https://www.wolframcloud.com/obj/5385d68a-17bc-4b69-b624-5ab9a15c106f)
* This notebook plots various things related to entropy for a binomial distribution (a coin toss)
* In particular look at houw the *summand function* is concave, and how you can change the *multiplier* away from the Shannon Entropy choice of -1*log(p) and yet entropy maximisation still works (still gives the same prioritisation of 50:50 odds as the max entropy and all points closer to 50:50 are greater entropy than those further, aaand [sic] the minimum entropy solution is p=0 or p=1)

* Want the `p_i == p_j` etc. solution to have the maximum entropy
* That is, the maximum entropy should happen when you assume you know nothing, therefore you cannot reasonably say that any index of p has a greater value than any other

What next
* You start applying constraints to the values of p you want to accept
* This restricts p and then from here you can look and see what available solution has the max entropy
* And within the available solutions you want to continue this logic of *"penalising discrimination"*

Conclusion
* Basically if your *summand function* is concave, then the average of two different points on the function is *"lower"* than the value of the function if you *"move"* the p_heads and p_tails values to equal oneanother
* More generally this concavity uses *Jensen's Inequality* to prioritise solutions which keep p_i and p_j apart from eachother


## 3. Multiple Dimensions
It extends relatively easily. Where it gets interesting is when you constrain the **p** space.

For an applied example see the **next section**:
* [Application: Food Reviews with a Small Sample  Size](./2023-10-04%20Five%20Star%20Reviews%20are%20Overrated.md)

Roughwork:
* In multiple dimensions, does the *summand function* still just need to be concave?
* Is there ever a case where the choice of concave *summand function* affects the result?

# Appendix
### Alternative Definitions of the *summand function*:
* We can define any generic function of p, say *f(p)* as long as the function is concave (negative second derivative)
* We can replace log(p) with any of the following and still get similar results
    * p
    * p^2 (or even p^n where n is any integer) **
    * e^p
    * r^p where r is a positive real number
    * p^r where r is a positive real number
* In fact typically the result will be the exact same, I need to check for constrained multidimensional cases where the choice of *summand function* affects the result

*\*\* Might also work for looser conditions*

### Constrained Entropy
Look at the plot above again for this;.
* Now let's you constrain the permitted values of *p*
* Suppose we have some insight telling us that `p_heads` cannot be greater than 0.4.
* Then we get maximum entropy under this constraint at `p_heads`=0.4 and `p_tails`=0.6.
* You can see this intuitively by observing that if we decrease `p_heads` (this requires us to increase `p_tails`) then `p_heads` and `p_tails` end up further apart and by jensen's inequality this gives a lower entropy. 

### Rough Notes
* Other kinds of entropy (Tsallis / Rényi)

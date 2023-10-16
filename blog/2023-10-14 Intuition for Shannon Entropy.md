# About
An article outlining the intuition behind Shannon Entropy and how it works for information theory.

Article Status: **Roughwork**

Sections
1. Definition of Shannon Entropy
2. Behaviour of the summand expression
3. Extension to more dimensions

## 1. Definition of Shannon Entropy
Definition of [Shannon Entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory))
:
  
  ![Shannon Entropy Definition](./images/2023-10-16%20Shannon%20Entropy.png)

* As a convention I will use the term **"*summand function*"** for the following expression:

    ![Shannon Entropy Summand](./images/2023-10-16%20Shannon%20Entropy%20Summand.png)
    
* **I will also propose alternative *summand functions*** which achieve the same outcome

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

## 2. Behaviour of the summand expression
This is the key part you need to understand.

1. What you want to do is plot the *summand function*
2. Then you'll see that you want a concave *summand function*

Why?
* Want the `p_i == p_j` etc. solution to have the maximum entropy
* That is, the maximum entropy should happen when you assume you know nothing, therefore you cannot reasonably say that any index of p has a greater value than any other

What next
* You start applying constraints to the values of p you want to accept
* This restricts p and then from here you can look and see what available solution has the max entropy
* And within the available solutions you want to continue this logic of *"penalising discrimination"*

Roughwork comment
* I'm going to be hand wavy here for now

Conclusion
* Basically if your *summand function* is concave, then the average of two different points on the function is *"lower"* than the value of the function if you *"move"* the p_heads and p_tails values to equal oneanother
* More generally this concavity uses *Jensen's Inequality* to prioritise solutions which keep p_i and p_j apart from eachother

Application
* So as an application, you add constraints which resemble the problem you want to solve
* Then you use entropy and look at the space of options which have not been excluded through constraints
* And you select amongst the remaining options using entropy
* Which really means, you select by picking the least descriminatory option(s), and Shannon Entropy (or any convex *summand function*) through it's concavity applies this *principle of non discrimination* mathematically

Mathematica Notebook:
* [2023-10-14 Entropy Intuition Visualisations.nb](https://www.wolframcloud.com/obj/5385d68a-17bc-4b69-b624-5ab9a15c106f)
* This notebook plots various things related to entropy for a binomial distribution (a coin toss)
* In particular look at houw the *summand function* is concave, and how you can change the *multiplier* away from the Shannon Entropy choice of -1*log(p) and yet entropy maximisation still works (still gives the same prioritisation of 50:50 odds as the max entropy and all points closer to 50:50 are greater entropy than those further, aaand [sic] the minimum entropy solution is p=0 or p=1)

## 3. Extension to more dimensions
It extends relatively easily. Where it gets interesting is when you constrain the **p** space. I want to explore this more and see whether the choice of *summand function*

# Other
Rough Notes
* Other kinds of entropy (Tsallis / Rényi)

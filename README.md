# distribution-sampler

So I'm doing a coding test! The test has three parts:

1. Functions
2. Object-oriented programming
3. Package building

This repo contains my solutions to the first two parts of these challenges.

## Part 1: Functions

**The challenge**  

*Write a function that will draw random numbers from a given distribution. The function should take one argument for the number of samples and a second argument which specifies the distribution (Normal, Poisson or Binomial). The function should be able to handle additional parameters depending on the distribution chosen, e.g., mean and sd for Normal samples.*

[My solution](http://nbviewer.jupyter.org/github/Tommo565/distribution-sampler/blob/master/1.%20Programming%20-%20Functions.ipynb)

## Part 2: Object-oriented programming

**The challenge**

*Construct an alternative to the above solution by using one or more classes instead of a single function.
Instances of this distribution class should store the distribution parameters as attributes, and also contain a draw method, which draws a fresh set of random numbers according to the distributions parameters, and a summarise method, which prints the min, max, mean, and standard deviation of the newly drawn sample.*

[My solution](http://nbviewer.jupyter.org/github/tommo565/distribution-sampler/blob/master/2.%20Programming%20-%20OOP.ipynb)

## Part 3: Package Building

**The challenge** 

*Build a package containing the functions and classes above. Use any tools as necessary. Include instructions on how the package can be installed.*

[Package repo available here](https://github.com/Tommo565/toms_dist_sampler) 


## To-do

* Unit Tests
* Delete main.py
* Maybe refactor DistributionSampler into smaller classes
* Improve the namespaces
* Upload to PyPi
* Detailled instructions for the README.md

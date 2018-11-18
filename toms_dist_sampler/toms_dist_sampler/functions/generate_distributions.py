import numpy as np


def generate_normal(size, mean, sd):
    '''
    Sub function for the distribution_sampler function. Generates samples from a normal 
    distribution based upon the size, mean and sd parameters.
     
    Returns the generated sample as s.
    '''
    s = np.random.normal(mean, sd, size)
    return s


def generate_poisson(size, lam):
    '''
    Sub function for the distribution_sampler function. Generates samples from a poisson 
    distribution based upon the size and lam parameters.
    
    Returns the generated sample as s.
    '''
    s = np.random.poisson(lam, size)
    return s


def generate_binomial(size, trials, prob):
    '''
    Sub function for the distribution_sampler function. Generates samples from a binomial 
    distribution based upon the size, trials and prob parameters.
    
    Returns the generated sample as s.
    '''
    s = np.random.binomial(trials, prob, size)
    return s
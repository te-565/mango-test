import numpy as np
from .validate_params import validate_params
from .generate_distributions import (
	generate_normal, generate_poisson, generate_binomial
)

def distribution_sampler(size, dist, mean=None, sd=None, lam=None, trials=None, prob=None):
    
    '''
    
    Selects a random sample from a given distribution, based upon the input parameters,
    and returns a numpy array object.
    
    Parameters
    ----------
    size : integer
    
    The number of samples to be selected from the distribution.
    
    distribution : string
    
    The type of distribution to be created. Applicable values are 'Normal', 
    'Poisson' or 'Binomial'.
    
    mean : float / int , optional
    
    Applicable to Normal distributions only. The mean value will dictate the 
    centre of the distribution.
    
    sd: float / int , optional
    
    Applicable to Normal distributions only. The sd (Standard Deviation) will
    dictate the spread or width of the distribution.
    
    lam : float / int , optional
    
    Applicable to Poisson distributions only. The lam (lambda) controls the mean 
    and variance of the sample.
    
    trials: float / int , optional
    
    Applicable to Binomial distributions only. The trials parameter is used to 
    dictate the number of trials to run in generating the sample
    
    prob: float / int , optional
    
    Applicable to Binomial distributions only. The prob parameter is used to dicitate
    the probability of a trial being successful.
    

    Returns
    -------

    s : A numpy array of samples based upon the input parameters.
    
    Notes
    -----

    The samples are generated using the numpy library, v1.15. For more details,
    check the API Reference material here: https://docs.scipy.org/doc/numpy-1.15.1/reference/

    Examples
    --------
    s = distribution_sampler(1000, 'Normal', mean=0, sd = 5)
    s = distribution_sampler(1000, 'Poisson', lam=5)
    s = distribution_sampler(1000, 'Binomial', trials=5, prob=0.5)    
    '''
    
    # Validate the parameters
    validate_params(size, dist, mean, sd, lam, trials, prob)
     
    # Generate the appropriate distribution sample
    if dist == 'Normal':
        s = generate_normal(size, mean, sd)
        
    elif dist == 'Poisson':
        s = generate_poisson(size, lam)
        
    elif dist == 'Binomial':
        s = generate_binomial(size, trials, prob)
    
    return s
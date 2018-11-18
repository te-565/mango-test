import warnings


def validate_params(size, dist, mean, sd, lam, trials, prob):
    '''
    Sub function for the distribution_sampler function to validate the 
    user input parameters. If the parameters are incorrect, a TypeError 
    is raised to alert the user to change the input parameters
    '''
    
    # Mandatory parameter error handling
    
    if dist not in ['Normal', 'Poisson', 'Binomial']:
        raise ValueError(
            "The dist parameter is mandatory and must equal 'Normal'",
            "'Poisson', or 'Binomial'"
        )
        
    if not isinstance(size, int):
        raise ValueError('The size parameter is mandatory and must be an integer.')
        

    # Distribution specific error handling and warnings
    
    if dist == 'Normal':
        # Raise an error if the mean or sd parameters aren't set
        if (mean == None) or (sd == None):
            raise NameError("The mean and sd parameters must be set where dist == 'Normal'")
            
        # Raise a warning if irrelevent parameters are provided
        elif (lam != None) or (trials != None) or (prob != None):
            warnings.warn(
                'The lam, trials and prob parameters are not used in the selection of a normal '
                'distribution. These parameters will be ignored.'
            )
            
    if dist == 'Poisson':
        # Raise an error if the lam parameter isn't set
        if lam == None:
            raise NameError("The lam parameter must be set where dist == 'Poisson'")
        
        # Raise a warning if irrelevent parameters are provided
        elif (mean != None) or (sd != None) or (trials != None) or (prob != None):
            warnings.warn(
                'The mean, sd, trials and prob parameters are not used in the selection of a ' 
                'poisson distribution. These parameters will be ignored.'
            )
            
            
    if dist == 'Binomial':
        # Raise an error if the trials or prob parameters aren't set
        if (trials == None) or (prob == None):
            raise NameError("The trials and prob parameters must be set where dist == 'Binomial'")
            
        # Raise a warning if irrelevent parameters are provided
        elif (mean != None) or (sd != None) or (lam != None):
            warnings.warn(
                'The mean, sd and lam parameters are not used in the selection of a binomial ' 
                'distribution. These parameters will be ignored.'
            )            

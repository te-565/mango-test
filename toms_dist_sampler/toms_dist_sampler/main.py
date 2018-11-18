from functions.distribution_sampler import distribution_sampler

s = distribution_sampler(1000, 'Normal', mean=0, sd = 5)
print(s)
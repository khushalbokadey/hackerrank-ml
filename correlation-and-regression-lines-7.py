#!/usr/bin/python
import math

def mean(nums):
    return float(sum(nums))/len(nums)

def variance(nums):
    m = mean(nums)
    variance = mean([abs(n - m)**2 for n in nums])
    return variance

def standard_deviation(nums):
    stdev = math.sqrt(variance(nums))
    return stdev

def center_data(X):
    m = mean(X)
    return [(x - m) for x in X]

def correlation(X, Y):    
    assert len(X) == len(Y)
    x = center_data(X)
    y = center_data(Y)
    top = sum([x[i]*y[i] for i in xrange(len(x))])
    bottom = math.sqrt(sum([n**2 for n in x])*sum([n**2 for n in y]))
    return float(top)/bottom    
    
physics = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
slope = correlation(physics, history)*standard_deviation(physics)/standard_deviation(history)
print slope

m = Σ(x - mean(x)) * (y - mean(y)) / Σ (x - mean(x))²
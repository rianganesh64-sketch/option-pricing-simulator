import numpy as np
from scipy.stats import norm

#Defining Variables
price_underlying = 100
strike_price = 100
time = 1
risk_free_rate = 0.05
annualized_volatility = 0.2
#Defining Helper Functions

def d_one(): #intermediate value
    return((np.log(price_underlying / strike_price) + time*(risk_free_rate + ((annualized_volatility**2)/2))) / (annualized_volatility * np.sqrt(time)))
print(d_one())
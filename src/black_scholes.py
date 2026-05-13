import numpy as np
from scipy.stats import norm

#Defining Variables: Tests for right now
price_underlying = 100
strike_price = 100
time = 1
risk_free_rate = 0.05
annualized_volatility = 0.2

#CALL OPTIONS: The right to purchase an asset a a specific strike price
#Defining Helper Functions
def d_one_call():
    return((np.log(price_underlying / strike_price)
            + time*(risk_free_rate + ((annualized_volatility**2)/2)))
            / (annualized_volatility * np.sqrt(time)))
rounded_d_one_call = round(d_one_call(), 2)
print(d_one_call())
print(rounded_d_one_call)

def d_two_call():
    return((np.log(price_underlying / strike_price)
            + time*(risk_free_rate - ((annualized_volatility**2)/2)))
            / (annualized_volatility * np.sqrt(time)))
rounded_d_two_call = round(d_two_call(), 2)
print(d_two_call())
print(rounded_d_two_call)

#Putting it all together with Black-Scholes 
def black_scholes_call():
    return((norm.cdf(d_one_call()) * price_underlying)
           - norm.cdf(d_two_call())
           * strike_price * (np.e**((-1 * risk_free_rate)
                                    * time)))
rounded_black_scholes_call = round(black_scholes_call(), 2)
print(black_scholes_call())
print(rounded_black_scholes_call)

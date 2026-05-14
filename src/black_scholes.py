import numpy as np
from scipy.stats import norm

#Defining Helper Functions
def d_one(S, K, T, r, sigma):
    """
    Calculates d1 used in the Black-Scholes formula.
    """
    if S < 0 or K < 0 or T <= 0 or sigma <= 0:
        raise ValueError("S, K, T, and sigma must be positive for BlackScholes")
    
    return((np.log(S / K)
            + T*(r + ((sigma**2)/2)))
            / (sigma * np.sqrt(T)))

def d_two(S, K, T, r, sigma):
    """
    Calculates d2 used in the Black-Scholes formula.
    """
    return((np.log(S / K)
            + T*(r - ((sigma**2)/2)))
            / (sigma * np.sqrt(T)))

#CALL OPTIONS: The right to purchase an asset a a specific strike price
#Putting it all together with Black-Scholes 
def black_scholes_call(S, K, T, r, sigma):
    """
    Calculates the Black-Scholes price of a European call option.
    """
    return((norm.cdf(d_one(S, K, T, r, sigma)) * S)
           - norm.cdf(d_two(S, K, T, r, sigma))
           * K * (np.e**((-r)
                                    * T)))



#PUT OPTIONS: The right to sell an assest at a specific strike price
def black_scholes_put(S, K, T, r, sigma):
    """
    Calculates Black-Scholes price of a European put option.
    """
    return(((K) * np.e**(-r * T)
            * norm.cdf(-d_two(S, K, T, r, sigma))
            - ((S) * norm.cdf(-d_one(S, K, T, r, sigma)))))


#Temporary test case
if __name__ == "__main__":
    S = 100 # current stock price
    K = 100 # current strike price
    T = 1 # time until expiration (in years)
    r = 0.05 # risk-free rate (convert to a percentage)
    sigma = 0.2 # annual volatility (covert to a precentage)

    print("d1:", round(d_one(S, K, T, r, sigma), 2))
    print("d2:", round(d_two(S, K, T, r, sigma), 2))
    print(
        "Call Price:",
        round(black_scholes_call(S, K, T, r, sigma), 2))
    print(
        "Put Price:",
        round(black_scholes_put(S, K, T, r, sigma), 2)
    )


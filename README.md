# Option Pricing Simulator

## Purpose

Option Pricing Simulator is a Python project that explores how financial options are valued. The project implements multiple pricing methods and stock-price simulations to help users understand the mathematics behind option pricing.

The goal of the project is to make advanced financial concepts more accessible by combining mathematical models, simulation techniques, and software engineering principles into a single educational tool.

---

## Current Status

Backend has been finished. Streamlit-based user interface is currently being worked on. This will feature interactive visualizations, tutorials, educational quizzes, and useful resources.

The following components are fully implemented:

- Black-Scholes option pricing
- Monte Carlo option pricing
- Geometric Brownian Motion (GBM) stock-price path generation
- Input validation
- Runtime measurement
- Error analysis
- Automated unit tests

---

## What the Program Accomplishes

The project can:

- Calculate European call option prices using the Black-Scholes model
- Calculate European put option prices using the Black-Scholes model
- Estimate option prices using Monte Carlo simulation
- Generate realistic stock-price paths using Geometric Brownian Motion
- Compare analytical and simulation-based pricing methods
- Measure execution time of different pricing methods
- Calculate absolute and percentage pricing errors
- Validate user inputs and handle invalid values safely

---

## Financial Concepts Used

### Black-Scholes Model

The Black-Scholes model is an analytical formula used to estimate the fair value of European options. It uses the current stock price, strike price, time to expiration, risk-free interest rate, and volatility.

### Monte Carlo Simulation

Monte Carlo simulation estimates option values by generating many possible future stock prices and averaging the resulting option payoffs.

### Geometric Brownian Motion (GBM)

Geometric Brownian Motion is a stochastic process commonly used to model stock prices. It combines deterministic growth with random market fluctuations.

---

## Inputs

The pricing models use the following variables:

| Variable | Meaning |
|----------|----------|
| `S` | Current stock price |
| `K` | Strike price |
| `T` | Time to expiration (years) |
| `r` | Risk-free interest rate |
| `sigma` | Stock volatility |
| `N` | Number of Monte Carlo simulations |

---

## How the Project Works

1. The user provides option parameters.
2. The Black-Scholes model calculates an analytical option price.
3. Monte Carlo simulation generates thousands of possible future stock prices.
4. Option payoffs are calculated for each simulated outcome.
5. The average discounted payoff is used to estimate the option's value.
6. Geometric Brownian Motion generates possible stock-price paths.
7. Utility functions compare results and measure performance.

---

## Project Structure

```text
option-pricing-simulator/
│
├── src/
│   ├── black_scholes.py
│   ├── monte_carlo.py
│   ├── gbm.py
│   ├── utils.py
│   └── __init__.py
│
├── tests/
│   ├── test_black_scholes.py
│   ├── test_monte_carlo.py
│   ├── test_gbm.py
│   └── test_utils.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Use the Current Version

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run All Tests

```bash
python -m pytest
```

### Run Individual Test Files

```bash
python -m pytest tests/test_black_scholes.py
python -m pytest tests/test_monte_carlo.py
python -m pytest tests/test_gbm.py
python -m pytest tests/test_utils.py
```

### Run Demonstration Code

```bash
python -m src.utils
```

The demonstration code executes examples of the implemented pricing models, simulations, and utility functions.

### For a deeper look into any of the functions, run individual files

```bash
python -m src.black_scholes
python -m src.gbm
python -m src.monte_carlo
```

### Run Streamlit Interface

```bash
streamlit run app.py
```
### Experimenting with the Models

Feel free to modify the input values in the demonstration code to observe how changes in stock price, volatility, time to expiration, or interest rates affect option prices and simulated stock paths!

---

# Option Pricing Simulator

An interactive Python simulator that compares **Black-Scholes** and **Monte Carlo** option pricing models while visualizing possible future stock price paths using **Geometric Brownian Motion (GBM)**.

This project is designed to make European option pricing easier to understand by combining financial math, simulation, and data visualization in a simple educational tool.

Project for FOCS SMCS 9 Class.

---

## Overview

Options are financial contracts whose value depends on the price of an underlying asset, such as a stock. This simulator allows users to enter option parameters and compare how different pricing methods estimate the value of a European call or put option.

The project currently focuses on:

- Black-Scholes option pricing
- Monte Carlo simulation
- Geometric Brownian Motion stock path simulation
- European call and put options
- Visual comparison of simulated stock paths
- Educational explanations of the results

---

## Features

- Calculates European call and put option prices using the Black-Scholes formula
- Estimates option prices using Monte Carlo simulation
- Simulates possible stock price paths using Geometric Brownian Motion
- Compares pricing results between analytical and simulation-based methods
- Displays graphs of simulated stock movement
- Includes input validation for unrealistic or invalid values
- Provides an educational interface for users learning about option pricing

---

## Financial Concepts Used

### Black-Scholes Model

The Black-Scholes model is a mathematical formula used to estimate the fair price of a European option. It assumes that stock prices follow a continuous-time stochastic process and uses inputs such as stock price, strike price, volatility, time to expiration, and risk-free interest rate.

### Monte Carlo Simulation

Monte Carlo simulation estimates an option price by generating many possible future stock prices, calculating the option payoff for each outcome, and averaging the discounted payoff.

### Geometric Brownian Motion

Geometric Brownian Motion is used to model possible future stock price paths. It includes both a deterministic trend and a random component to reflect uncertainty in the market.

---

## Inputs

The simulator uses the following inputs:

| Variable | Meaning |
|---|---|
| `S` | Current stock price |
| `K` | Strike price |
| `T` | Time to expiration in years |
| `r` | Risk-free interest rate |
| `sigma` | Volatility of the stock |
| `N` | Number of Monte Carlo simulations |

---

## Project Structure

```text
option-pricing-simulator/
│
├── src/
│   ├── black_scholes.py
│   ├── monte_carlo.py
│   ├── gbm.py
│   └── __init__.py
│
├── tests/
│   ├── test_black_scholes.py
│   ├── test_monte_carlo.py
│   └── test_gbm.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

# Portfolio Optimisation in python 

## Table of Contents
- [Overview](#overview)
- [Libraries-imported](#Libraries-imported)
- [Grabbing the Data](#Grabbing-the-data)
- [Calculating the Sharpe Ratio](#calculating-the-sharpe-ratio)
- [What is a good sharp ratio](#what-is-a-good-sharp-ratio)
- [For Monte-Carlo simulation](#For-Monte-Carlo-simulation)
- [Portfolio Optimisation: Monte Carlo](#portfolio-optimisation-monte-carlo)
- [Markowitz Efficient Portfolio Optimisation Technique  : Stock market analysis & Markowitz Efficient Frontier on Python](#markowitz-efficient-portfolio-optimisation-technique---stock-market-analysis--markowitz-efficient-frontier-on-python)
- [The Black-Litterman Model: (Active portfolio management)](#the-black-litterman-model-active-portfolio-management)
- [Bayesian approach and python implementation of Black-Litterman framework](#bayesian-approach-and-python-implementation-of-black-litterman-framework)
- [CAPM (Capital Asset Pricing Model)](#capm-capital-asset-pricing-model)
- [Setup](#setup)
- [Usage](#usage)

## Overview
**All the Jupyter Notebooks are present in the folder named - Portfolio_optimization_techniques.**
**You can Access the Handwritten Notes for Black-Litterman Model in the folder named - Handwritten Notes**

A simple python project where we use price data from the NASDAQ website to help optimize our portfolio of stocks using modern portfolio theory.

Optimising a portfolio for some kind of constraint. Risk adjusted returns - taking most amount of risk for a given amount of return (best return for the amount of risk taken). Different types of risks as well as financial dial instruments which gives you low and high returns based on the how much risk comes along with it. So we’re building a portfolio where we can maximise the returns for a give level of risk (service to a client so that he doesn’t take an unnecessary risk and return them their returns whatever mount or percentage is required with the level of risk involved with it).

We tune (fine tuning using optimisation formulae or Monte Carlo simulation) our portfolio, how much we own a particular asset and tune it in such a way that we optimise the level risk of return that we get.

## Libraries-imported:

1\. pathlib - to manage to manage file paths as file paths are very difficult to manage in different

operating system sometimes jumping between different operating systems can be a little bit

complicated, it tries to standardise that for us.

2\. numpy as np (alias) - for number crunching.

3\. pandas - taking numeric data and putting it into a data frame. It is a tabular format, on which we

can do data transformation and data calculation, combining columns and grouping data such as

pivoting and non-pivoting data. Great when working with large amount of data.

4\. mathplotlib.py as plt - plotting

5\. scipy.optimize as sci\_plt - scientific mathematical model for calculating the optimised values with

the help of the optimised package which basically allows us to use different mathematical

optimisation functions

6\. from pprint import pprint

7\. from sklearn.preprocessing import StadardScaler - for standardising data as well as pre-

processing of the data in order to get better results. 8. from pytopt.client import PriceHistory

## Grabbing the Data 

1\. Define the symbols/portfolio:

symbols = [‘APPL’, ...]

2\. Gen the number of stocks in our portfolio. - length of the symbols

3\. If we don’t have data grab it from NASDAQ. Initialise the price history and use the symbols variables for reference.

4\. Grab the data frame and dump it to a dev file. If not present then add to the csv file and then print the data frame header.

5\. If data present then load the csv file and then print the price data frame.head().

6\. Transform the data by reorganising the data frame. Grab the columns we need in the situation.

7\. Pivot the data frames to make the symbols the headers. We can define the index, columns and values with values - date, symbol, close respectively.

8\. Display the price\_data\_frame by pivoting the data so as to load the data.

## Calculating the Sharpe Ratio:

1\. For benchmarking and helping one find the best possible manager as per the performance.

2\. Comparisons on the basis of how return each of percentage return, as well as the risk taken.

3\. We can benchmark using Sharp ratio. In sharp ratio what we’re trying to do is to measure
    something called as - Risk Adjusted Return. One important metric additionally put in here is called the Risk Free rate.

4\. Risk free rates - rates that we can get by taking no risk. Example - the return rates on the US treasury, as it is never going to dissolve, so no risk to be taken. 

![WhatsApp Image 2024-10-05 at 03 18 29](https://github.com/user-attachments/assets/a6bd6322-a242-46fe-bdf5-df2877ce23ea)


    Return above risk free ratio = Return of Portfolio/Expected return (Rp) - Risk free rate (Rf) 

    Sharpe ratio (in %) = Risk above risk free ratio / Expected risk

There’s no point taking less return than the risk free rate allows us to do. 

To calculate the expected returns (how much does each individual asset take up my portfolio and the return associated to it, contributed to the total return of a portfolio), we use the formula :
![WhatsApp Image 2024-10-05 at 03 18 32](https://github.com/user-attachments/assets/bbeaed67-b1c0-402c-b040-f10541513eec)


 calculate the standard deviation of the portfolio (summation of the variance of change in the asset value of each asset price + the correlation coefficient between each of the assets as well) : 
![WhatsApp Image 2024-10-05 at 03 18 42](https://github.com/user-attachments/assets/1d8dd0be-2dd4-4c5d-99ff-a1a8e351d004)


Sharp ratio is used to compare one portfolio to another portfolio. 

## What is a good sharp ratio:

1. Anything below 1 isn’t considered as good. 1 is considered as suboptimal. One is considered as a benchmark. 
2. An excellent sharp ratio tends to be around 3. 
3. Higher sharp ratio -> better performing portfolio.

## For Monte-Carlo simulation 

-we calculate the Log(returns) - these are returns overtime, so the idea behind this is, when we take a percentage change, log is to calculate what re the changes overtime. (Refer the 4th cell) 

- What weights should we give to each of our assets in our portfolio ? 

  Randomly get the values for each symbol in the portfolio and run and iterate these random training dataset many times such that overtime, if we do enough iterations, we should be able to capture the variation aspect of the assets. (Under # Generating random weights)

- Random weights are then transformed to rebalanced weights because then it can actually be of value more than 1. All of them sum up to 1. (# Generate the rebalance weights) 

       Rebalance weights = random weights / sum(random weights)



- Now we calculate out expected returns:  

      Expected returns = sum((log\_returns.mean() \* rebalance weights ) \* 252 )
  (We do  (daily returns)\* 252 to annualise it ^^) 

- Calculating the expected volatility, annualised !! (if the asset price is moving up a lot or down): 

       Expected volatility = [ Transpose(rebalanced weights) . ((log\_returns.covariance() \* 252) . rebalance weights)] ^ 1/2 . 

- Calculating the sharp ratio:

      sharp ratio = (expected return - 0.1) / expected volatility 

- put all the data into two data frames by creating two data frames and calculate the sharp ratio for the overall trained dataset.

# **Portfolio Optimisation: Monte Carlo** 

Process: 1. Random weights -> 2. Expected return, volatility -> 3. Sharp Ratio 



1. Have a giant array of possible outcomes and random weights.
2. Grabbing the maximum sharp ratio so that the risk adjusted return and then additionally grabbing the minimum volatility.
3. Grabbing the portfolio with the lowest expected volatility and the highest sharp ratio. 

Coding steps:

1. Define the number of times we want to run the simulation (num\_of\_simulations = 3000 (num\_of\_portfolios) 
2. Store simulation in some type of array for each - weights, returns, volatility, sharp ratios with bunch of zeroes (all\_weights = np. zeros(num\_of\_portfolios, number\_of\_symbols),   Prep the returns array of numpy zeroes:  ret\_arr = np.zeroes(num\_of\_portfolios), same type of format for volatility as well as sharp ratio)

3. Start the simulation (in loop):

`          `1. First calculate the weights (no. of weights that match the number of symbols):

                weights = np.array(np.random.random(number_of_symbols)  
`         `2. The portfolio is 100% allocated :

                 weights = weights / np.sum(weights)

`         `3. Adding the weights to the weights array

`         `4. Calculate the expected log returns (using logs because it’s better for time series) 

`         `5.  Calculating the volatility and adding them to the volatility array:
           We want each price of our portfolio to contribute to the overall portfolio evenly, based on how much they actually represent if the portfolio.
          In simple words - how much volatility that particular instrument is contributing to the overall  portfolio. Also add the assets which are correlated with each other. 

`        `6. Calculating the Sharp ratio using the sharp array at the current index of the loop which we are on = (return\_array[i] - 0.01) / volatility\_array[i] 

`        `7. Combining all of this together outside the main loop: 

`              Simulations\_data  = [return\_array, volatility\_array, sharp\_array, all\_weights]

`        `8. Creating a data frame for our dataset ^^ (transposed dataset - simulations\_data) 

`        `9. Adding the column names 

`       `10. Making sure that all the data present in the data frame has the right data type using infer\_object() method

`       `11. Printing the result. 

## **Grabbing the important Metrics:**

1. Grab the max sharp ratio : find the location of the row inside the data frame where the sharp ratio is maximum.

                        max\_sharp\_ratio = simulation\_df.loc[simulations\_df[‘Sharp Ratio’].idmax()]

2. Return the minimum volatility from the Run:  

                       min\_volatility = simulation\_df.loc[simulations\_df[‘Volatility’].idmin()]

3. Printing the results 

Drawbacks of the Monte Carlo simulations is : the more number of iterations you want to run to get the simulations working the longer it takes and over a very large dataset, it isn’t that efficient. 

## **Plotting the results of the Monte Carlo Simulation:**

- using the mathplotlib library we do the plotting 
- On y-axis : Returns 
- On x-axis : Volatility
- Values to get for the graph : Sharp Ratios
  - Plotting the max sharp ratio using the red star. 
  - plotting min volatility with blue star 
  - print the plot (show)

## **Optimisation (using sci-py optimisation module)**

1. Write a function to pass through the optimisation module 
2. 1st function
     - get\_metrics: gets a list of weights from our particular list -> return a numpy array with weights :
     - convert the weights to a numpy array
     - calculate the returns (annualised):
                 **ret = np.sum(log\_mean() \* weights) \* 252**
      -  calculate the volatility by transposing the weights and multiplying them with the (dot product(covariance of returns (log) \* 252, weights)) in a dot product:
             **vol = np.sqtr(np.dot(weights.T, np.dot(log\_return.cov() \* 252, weights)))**
      - calculate the sharp ratio: sr = (ret - 0.01) / vol
      - return a numpy array back with array([ret, vol, sr])

**Note**: If we want to optimise based on the sharpe ratio we need to define a function that returns only the sharpe ratio. Since our optimisation function naturally seek to minimise, we can minimise one of the two quantities: The negative of the sharpe ratio. (or 1/(1+Sharpe Ratio). Accordingly, if the sharpe ratio increases both of these quantities will decrease. We'll chose the negative of sharpe for this example. 

We use the SLSQP (Sequential Lest Squares Programming) method to minimise the results.  

3. Next function - grab negative sharp ratio with weights as argument returning numpy array as a list datatype:
        - we’re trying to minimise the negative sharp ratio 
        - return get\_metrics(weights)[2] - 1

4. Define a function to grab volatility with parameter - weights and returns numpy array: return get\_metrics(weights)[1]

5.  Define a check sum function which makes sure the weights do not exceed a 100 %: you cannot have a 100% of your portfolio allocated. (we define constraints) 
6.   Define bounds using tuples in our optimisation process. 
7.   Defining the constraints (weights do not increase 100%) : type - equality constraint, function : check\_sum 
8. Define the initial guesses : number\_of\_symbols \* [1 / number\_of\_symbols] 
9. Perform the optimisation process : 


    ```python
    optimized_sharpe = sci_plt.minimize(
        grab_negative_sharpe,  # what we need to minimise
        init_guess,            # these are the initial weights
        method='SLSQP',
        constraints=constraints,
    )
    ```


10. Print optimised sharpe ratio. 

11. Grab the optimised sharpe ratio weights metrics and print that specifically. 
12. We repeat the same process for the volatility aspect (use grab\_volatility() function) - find the least volatility and optimise it. 



# **Markowitz Efficient Portfolio Optimisation Technique  : Stock market analysis & Markowitz Efficient Frontier on Python**

**Markowitz portfolio optimisation model** : 
The minimum variance is a graph of the lowest possible variance that can be attained for any given level of expected return. The global minimum variance portfolio is the portfolio of risky assets that has lowest variance of all risky assets portfolios. The efficient frontier is the range of all investments that are within the minimum-variance frontier and are above (have a higher return than) the global minimum variance portfolio.


## Returns: 

![WhatsApp Image 2024-10-05 at 03 30 33](https://github.com/user-attachments/assets/248d66ce-4b08-4af6-aa9f-f1fade77c06f)

The formula for returns is given by:
```{math}
:label: my-equation
r_{t} = \frac{p_t}{p_{t-1}}
```

Where:
- \( t \) is the time,
- \( p_t \) is the price at time \( t \).


# **The Black-Litterman Model: (Active portfolio management)**

The Black-litterman integrates various approaches for portfolio optmisation, like traditional with quantitative mangers. 

## Problems with Markowitz’s Model (mean variance optimisation):

1. Highly concentrated portfolios 
1. Portfolios very sensitive to small changes in expected returns

Sometimes we get STRANGE PORTFOLIOS with huge weights. Empirical evidences also indicate that a small change in expected returns can cause a drastic change in portfolio composition, so we get some weird portfolios sometimes. 

The black-litterman model proposed by Fischer Black and Robert litterman is represented as an asset allocation model but it is essentially a model to forecast expected returns. Once we know expected returns, we can use standard optimisation techniques to arrive at the optimal portfolio. They use REVERSE-OPTIMISATION in order to arrive at an estimate of implied equilibrium excess returns. They also allow us to incorporate our views about various assets or stocks that comprise our portfolio and also our confidence about our views to generate the expected return vector. 

## Notion of implied equilibrium excess returns: 

Investors utility function - refer (I) in the image notes attached 

Now rather than solving for optimal weights they argued that weights are already observed in the market and therefore we can compute the, using market capitalisation. They reversed the equation for maximised utility and solved for R(return). 

If we’re in agreement with the excess returns thus generated, we should hold the market portfolio, because in the absence of any other view, these returns would take us back to the market weights. 

Views about the stocks that comprise the portfolio. We can have absolute views like return on Google stock is 2%, in the near future. We can have relative views, for example, return on Amazon’s stock will be greater than Apple’s stock by 1%. In practice, relative views are more common and we will use them for our discussion. 

Example given in the notes attached - refer (II) in Handwritten Notes

     Implied Returns + Investor Views = Expected Returns 

The risk(uncertainty with the expected returns) is represented by using the variance covariance matrix (S). - refer (II) in Handwritten Notes

Measure of confidence about our expected implied equilibrium returns- S^(-1).

There is no one best way to compute the uncertainty matrix (omega), black, and litterman suggest, however, the elements of the omega matrix which are capturing the uncertainty of our views are calculated as a scaler which they write as - refer (III) 

Now we measure the confidence of our views as inverse of omega.

Black-litterman formula gives us the estimate of excess returns by calculating weighted average of two items. This paper is also trying to prove that the Bayesian formula for expected returns is true. 

![WhatsApp Image 2024-10-05 at 03 30 44](https://github.com/user-attachments/assets/148489ed-d51c-4206-9188-bf7e2e40628d)
![WhatsApp Image 2024-10-05 at 03 31 01](https://github.com/user-attachments/assets/cd3218d7-0130-4cd2-8c1f-852d984c0f97)



The 1st and the 2nd terms of the black-litterman formula are defined in (III) in notes attached. Refer part (IV) for the complete Black-Litterman formula. 

A simple demonstration is also attached in part (V) of the notes.  

Black-litterman has allowed us to have the freedom of having our own views reflected in our excess returns and then optimise the portfolio. 

## **Bayesian approach and python implementation of Black-Litterman framework:**
Alan Scowcroft and Stephen Satchell tried to explain this framework a bit more in detail. The framework explains the interrelationship between traditional managers and quantitative managers, it’s a unification of the two. 

![WhatsApp Image 2024-10-05 at 03 31 09](https://github.com/user-attachments/assets/e84b2a3f-6bcf-46ab-93be-c02f540c9a65)

Beta is less useful for long-term investments since a stock’s volatility can change significantly from year to year, depending upon the company’s growth stage and other factors. 

The given image bellow represents the forecast of manager/investor after updating for the information from the quantitative model : 
![WhatsApp Image 2024-10-05 at 03 31 19](https://github.com/user-attachments/assets/18db6be9-ee48-4524-9267-dbbda1de3035)


## Theorem 1 : q, omega are our Bayesian hyper parameters for k beliefs, P is k by n matrix 

The pdf of E(r) (expected return) given pi is given by a posterior probability density function where 1st term is the mean and 2nd term is the variance .

![WhatsApp Image 2024-10-05 at 03 31 28](https://github.com/user-attachments/assets/b15d9c5d-6274-42b0-9e16-07dcd2f03a0f)



## Theorem-2: 
![WhatsApp Image 2024-10-05 at 03 31 35](https://github.com/user-attachments/assets/e2e8f10c-cbc0-466b-8598-ee77ca243317)

**Implementation in python using pyportfolioopt. (Refer the file - black-litterman\_framework.ipynb)**

For prior, the **implied risk premium** is calculated as market’s excess return divided by it’s variance by using the formula :  
  ![WhatsApp Image 2024-10-05 at 03 31 42](https://github.com/user-attachments/assets/d420a8c7-0b2d-4edf-ab0a-e07acca09476)


 **Market implied returns vector**:  
  ![WhatsApp Image 2024-10-05 at 03 31 48](https://github.com/user-attachments/assets/0e7d7468-9480-49fe-9a62-fe5847bb535e)


# **CAPM (Capital Asset Pricing Model):**

Refer the file - **Capital\_Asset\_Pricing\_Model.ipynb**

The CAPM formula is used for calculating the expected returns of an asset. It is based on the idea of systematic risk (otherwise known as non-diversifiable risk) that investors need to be compensated for in the form of a risk premium. A risk premium is a rate of return greater than the risk-free rate.

The pieces of the CAPM formula are the risk-free rate (Rrf), investment beta (βa) and the market return (Rm – Rrf). The value of each piece is dynamic, so the CAPM calculation needs to be updated over time. The formula is represented symbolically as: Ra = Rrf + [βa \* (Rm – Rrf)], with Ra being the expected return.

## Assumptions when using CAPM model :

1. Market is 100% efficient all the time and correct 
2. The people who are buying into this market are risk adverse people and also they are rational people. 
3. The CAPM model does not take in consideration of the fluctuations or the volatility of the risk free rate. Volatility on that particular risk free instrument is not  very accurate and will definitely have a great effect on your expected return for a given company. 

The usage of this model is very subjective and can changes according at anytime which is its downside of using this particular model. 



## Setup

Right now, the library is not hosted on **PyPi** so you will need to do a local
install on your system if you plan to use it in other scrips you use.

First, clone this repo to your local system. After you clone the repo, make sure
to run the `setup.py` file, so you can install any dependencies you may need. To
run the `setup.py` file, run the following command in your terminal.

```console
pip install -e .
```

This will install all the dependencies listed in the `setup.py` file. Once done
you can use the library wherever you want.
Additional Libraries are installed in the jupyter notebooks 

## Usage

Here is a simple example of using the `pyopt` library to grab the index
files for specific quarter.

```python
import pandas as pd
from pyopt.client import PriceHistory

# Define the symbols
symbols = ['AAPL', 'MSFT', 'SQ']
number_of_symbols = len(symbols)

# Initialize the client.
price_history_client = PriceHistory(symbols=['AAPL','MSFT','SQ'])

# Dump it to a CSV file.
price_history_client.price_data_frame.to_csv(
    'stock_data.csv',
    index=False
)
pprint(price_history_client.price_data_frame)
```

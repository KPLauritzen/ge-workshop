# Great Expectations workshop
This is a starting repo for a workshop on `great_expectations`. 
The intention is that everyone in the audience have spent time with this before the workshop. 

It contains a very bare-bones example of getting data and doing some preprocessing on it. 
What you need to do is to set up some **expectations**. 
You should look at the data, imagine some use-case for it, and then decide what expectations will make sense. 
Feel free to complicate the data pipeline if you want to experiment more. 
## Setting up
```shell script
python -m venv venv/
venv/Scripts/activate
pip install -r requirements.txt
```

## Run pipeline
```shell script
doit
```

## Create expectations
Have a look at the `great-expectations` [documentation](https://docs.greatexpectations.io/en/latest/).
You can see some tutorials for getting up and running quickly [here](https://docs.greatexpectations.io/en/latest/guides/tutorials.html).

You can maybe use `pandas_profiling` to get an idea about what expectations to set up. 
See [documentation here](https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/).

After a suite of expectations have been created, it is possible to generate
a sort of documentation for the dataset from them. 
See [Data Docs](https://docs.greatexpectations.io/en/latest/reference/core_concepts/data_docs.html).
This could be useful for getting new people up to speed on a project. 

# Appendix
## Boston house prices dataset



**Data Set Characteristics:**  

    :Number of Instances: 506 

    :Number of Attributes: 13 numeric/categorical predictive. Median Value (attribute 14) is usually the target.

    :Attribute Information (in order):
        - CRIM     per capita crime rate by town
        - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
        - INDUS    proportion of non-retail business acres per town
        - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
        - NOX      nitric oxides concentration (parts per 10 million)
        - RM       average number of rooms per dwelling
        - AGE      proportion of owner-occupied units built prior to 1940
        - DIS      weighted distances to five Boston employment centres
        - RAD      index of accessibility to radial highways
        - TAX      full-value property-tax rate per $10,000
        - PTRATIO  pupil-teacher ratio by town
        - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
        - LSTAT    % lower status of the population
        - MEDV     Median value of owner-occupied homes in $1000's

    :Missing Attribute Values: None

    :Creator: Harrison, D. and Rubinfeld, D.L.

This is a copy of UCI ML housing dataset.
https://archive.ics.uci.edu/ml/machine-learning-databases/housing/


This dataset was taken from the StatLib library which is maintained at Carnegie Mellon University.

The Boston house-price data of Harrison, D. and Rubinfeld, D.L. 'Hedonic
prices and the demand for clean air', J. Environ. Economics & Management,
vol.5, 81-102, 1978.   Used in Belsley, Kuh & Welsch, 'Regression diagnostics
...', Wiley, 1980.   N.B. Various transformations are used in the table on
pages 244-261 of the latter.

The Boston house-price data has been used in many machine learning papers that address regression
problems.   
     
.. topic:: References

   - Belsley, Kuh & Welsch, 'Regression diagnostics: Identifying Influential Data and Sources of Collinearity', Wiley, 1980. 244-261.
   - Quinlan,R. (1993). Combining Instance-Based and Model-Based Learning. In Proceedings on the Tenth International Conference of Machine Learning, 236-243, University of Massachusetts, Amherst. Morgan Kaufmann.
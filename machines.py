import csv
import pandas as pd
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

#Reads in data from online source, updated daily
#Replace MFST with other stock symbol per desire
#data = data.head(20)


# Preparing Data

def recommend(l, n):
    buyr = 'Our statistical models predict that this stock should be bought, as it\'s price will rise'
    dbr = 'Our statistical models cannot provide proper substantiation for purchasing this stock.'
    buy = True

    for x in l:
        if x < n:
            buy = False
            break

    if buy:
        return buyr
    return dbr

#Use this function for pandas dataframes
def gd(dataframe):
    dfdates  = []
    dfprices = []
    i = 0.0
    while i < len(dataframe):
        a = dataframe.xs(i)
        #print(a)
        dfdates.append(i)
        #print(dates)
        dfprices.append(a[1])
        i += 1
    return [dfdates, dfprices]

#Use this function for raw local csv files
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)	# skipping column names
        i = 0.0
        for row in csvFileReader:
            csvdates.append(i)
            #print(dates)
            csvprices.append(float(row[1]))
            i += 1
    return

#input: dates, prices of length n for n days
#trains models, plots models, returns each model's prediction on day #x
def predict_prices(dates, prices, x):
    dates = np.reshape(dates,(len(dates), 1)) # converting to matrix of n X 1
    print('step 1 done')
    svr_lin = SVR(kernel= 'linear', C= 1e3)
    svr_poly = SVR(kernel= 'poly', C= 1e3, degree= 2)
    svr_rbf = SVR(kernel= 'rbf', C= 1e3, gamma= 0.1) # defining the support vector regression models
    print('step 2 done')
    svr_rbf.fit(dates, prices) # fitting the data points in the models
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    print('step 3 done')

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]


#parses in dataframe, creates dates and prices arrays, dates is just 1-n for calculation purposes


#reverses prices list, which was fed in reverse chronological order originally


#trains models, so far model not fast enough for >20 day inputs
def main(sName):

    sName = str(sName)

    data = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+sName+'&apikey=920LWVOAW4MCO2QD&datatype=csv')
    data = data.head(20)
    print('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+sName+'&apikey=920LWVOAW4MCO2QD&datatype=csv')



    dfdates, dfprices = gd(data)

    dfprices.reverse()

    predicted_price = predict_prices(dfdates, dfprices, 21)

    print(sName)
    print(predicted_price, dfprices[-1])
    return [predicted_price, recommend(predicted_price, dfprices[-1])]

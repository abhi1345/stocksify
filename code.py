import web
import csv
import pandas as pd
import numpy as np
from sklearn.svm import SVR
from machines import main, gd, predict_prices, recommend
import matplotlib.pyplot as plt

urls = (
'/(.*)','index'
)



class index:
    def GET(self, name=None):
        #first, sec, thir = h[0], h[1], h[2]
        x = name
        if x:
            output = main(x)
            h = output[1]
            plist = (', ').join([str(f) for f in output[0]])

            print(h)
            return render.index(x, h, plist)
        else:
            return render.index(None, None, None)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

render = web.template.render('templates/')

##create a nodel to estimate the relationship b/w x and y
##optimization model = OLS estimator

def ols(x,y):

    y_ = y.mean()
    x_ = x.mean()


    b1 = np.sum((y-y_)*(x-x_))/np.sum((x-x_)**2)
    b0 = y_- b1*x_
    return(b0,b1)

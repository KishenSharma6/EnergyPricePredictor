import numpy as np

from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error

def regression_metrics(y, y_hat):
    """Generate and return dictionary containing
     MSE, RMSE, MAE, & MAPE metrics for y  and y_hat

    Args:
        y (array): ground truth
        y_hat (array): predictions

    Returns:
        _type_: _description_
    """
    mse= mean_squared_error(y, y_hat)
    rmse= np.sqrt(mse)
    mae= mean_absolute_error(y, y_hat)
    mape= mean_absolute_percentage_error(y, y_hat)

    keys= ["mse", "rmse", "mae", "mape"]
    values= [mse, rmse, mae, mape]
    eval_metrics= {}
    for k, v in zip(keys, values):
        eval_metrics[k]= round(v,3)

    return eval_metrics
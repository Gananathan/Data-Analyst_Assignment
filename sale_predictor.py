import joblib
from utils import *
import pandas as pd
from tqdm import tqdm
t =tqdm(total=100)
# print(col_list)
x_scaler = joblib.load("x_scaler.joblib")  
y_scaler = joblib.load("y_scaler.joblib")
model = joblib.load("model.joblib")


def get_sale_price(X):
    """
    input X - dataframe
    output Y - numpy array
    """
    if("Id" in X.columns):
        X=X.drop(columns="Id")
    if("SalePrice" in X.columns):
        X=X.drop(columns="SalePrice")
    
    if(input_cols != list(X.columns)):
        raise Exception("Columns not found")

    t.update(25)
    X = pd.get_dummies(X)
    NX = X.reindex(columns = col_list, fill_value=0)
    t.update(50)
    scaled_x = x_scaler.transform(NX.values)
    y = model.predict(scaled_x)
    t.update(75)
    inv_scaled_y = y_scaler.inverse_transform(y.reshape(-1,1))
    t.update(100)
    return inv_scaled_y



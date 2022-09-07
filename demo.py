from sale_predictor import get_sale_price
import pandas as pd
if(__name__=="__main__"):
    try:
        data = pd.read_csv("dataset.csv")
        print(data.head()["SalePrice"])
        print(get_sale_price(data.head()))
    except Exception as e:
        print(e)
     
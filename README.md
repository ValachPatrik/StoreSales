# StoreSales
Time Series Forecasting

Source of the exersice:
https://www.kaggle.com/competitions/store-sales-time-series-forecasting/overview
Data sets:
kaggle competitions download -c store-sales-time-series-forecasting

After some figuring out what to include in the model, I tried linear regresion on the date, sales, store-nmbr. I got unsatistactory results and moved on to a different model. Even though it provided more realistic results it still was low points in the sumbition on Kaggle. I looked for others poeple solution and found one that used Regresion separately on each store and as it turns out it was a sound idea. I updated the code to work on my local machine and did some changes to the data cleanup. In the end the submition got score of 0.99949.

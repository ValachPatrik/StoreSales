# StoreSales
Time Series Forecasting

Source of the exersice:<br>
https://www.kaggle.com/competitions/store-sales-time-series-forecasting/overview

Data sets:<br>
kaggle competitions download -c store-sales-time-series-forecasting

First I got the feel of the data set, figured out if there are any missing values, what were the trends, etc..
My first attempt was to use linear regresion on the date, sales, and store-number after some thought about what to include in the model. I wasn't pleased with the results and switched to a different model. Even though it produced more realistic results, it was still ranked low on Kaggle. I looked for other people's solutions and discovered one that used regression separately on each store, which turned out to be a good idea. I made some changes to the data cleanup and updated the code to work on my local machine. Finally, the submission received a score of 0.99949.

Finally, I believe I have a better understanding of what data influences sales the most and what data is not as important in this case for forecasting.

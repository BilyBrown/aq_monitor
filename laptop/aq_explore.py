import datetime
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

df = pd.read_csv("../data/datalog_trial_0.csv", header=None)

#DATETIME ME
df[0] = pd.to_datetime(df[0])

# remove outliers
cleaned_df = df[(np.abs(stats.zscore(df[[1,2,3,4]])) < 3).all(axis=1)]

today_avg_df = cleaned_df.groupby(pd.Grouper(key=0, freq='1D')).mean().reset_index()
month_avg_df = cleaned_df.groupby(pd.Grouper(key=0, freq="1ME")).mean().reset_index()
week_avg_df = cleaned_df.groupby(pd.Grouper(key=0, freq="1W")).mean().reset_index()

current_co2 = cleaned_df.iloc[-1,2]
today_avg_co2 = today_avg_df[2].values[-1]
monthly_avg_co2 = month_avg_df[2].values[-1]
week_avg_co2 = week_avg_df[2].values[-1]

print("---------------")
print(f"Current CO2: {current_co2}")
print(f"Today's CO2 avg: {round(today_avg_co2, 2)}")
print(f"This week's CO2 avg: {round(week_avg_co2, 2)}")
print(f"This month's CO2 avg: {round(monthly_avg_co2, 2)}")

another_way = cleaned_df.set_index(0).copy()
weekly_mean = another_way[2].resample('W').mean()
weekly_mean = weekly_mean.fillna(0)
weekly_mean = weekly_mean[-5:]
max_value = weekly_mean.max()

print("----------------")
print("The past 5 week's averaged CO2 values:")
for week, value in weekly_mean.items():
    bar_length = int((value / max_value) * 50)
    print(f"{week.strftime('%m-%d')} : {'#' * bar_length} ({value:.2f})")

import csv, pandas as pd, matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D 

df = pd.read_csv('sensor_data.txt', sep="|", header = None, parse_dates = True, engine='python', names=["timestamp","temperature"])
#df.columns = ["timestamp","temperature"]

#print df['temperature']

plt.scatter(df.timestamp, df.temperature, s=10)



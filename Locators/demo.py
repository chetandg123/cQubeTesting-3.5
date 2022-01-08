
import pandas as pd

df = pd.read_csv('../../../enrollment-progress-state (3).csv')
size = len(df)
total_enrolled = df['Expected Enrollment'].sum()
avg_time = df['Net Enrollment'].sum()
n = len(pd.unique(df['Program Name']))


print(total_enrolled)
print(avg_time)
print('prgam ont',n)
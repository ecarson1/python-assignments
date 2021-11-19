import numpy as np
import pandas as pd

df = pd.read_csv('2_pandas_Salaries.csv')

#Question 1
print("QUESTION 1")
head = df.head()
print(head)

#Question 2
print("QUESTION 2")
df.info()

#Question 3
print("QUESTION 3")
average_bp = df.head(10000)["BasePay"].mean()
print(f"Average base pay for first 10000 entries: {average_bp}")

#Question 4
print("QUESTION 4")
max_tpb = df["TotalPayBenefits"].max()
print(f"Max total pay benefits: {max_tpb}")

#Question 5
print("QUESTION 5")
jd = df.loc[df['EmployeeName'] == 'JOSEPH DRISCOLL']
title = jd["JobTitle"].values[0]
print(f"Job title of JOSEPH DRISCOLL is: {title}")

#Question 6
print("QUESTION 6")
jd_tpb = jd["TotalPayBenefits"].values[0]
print(f"Total Pay w/ Benefits of JOSEPH DRISCOLL is: {jd_tpb}")

#Question 7
print("QUESTION 7")
most_paid = df.loc[df["TotalPayBenefits"] == max_tpb] #already found max_tpb so just plugged it in
mp_name = most_paid["EmployeeName"].values[0]
print(f"Employee with highest Total Pay w/ Benefits is: {mp_name}")

#Question 8
print("QUESTION 8")
min_tpb = df["TotalPayBenefits"].min()
least_paid = df.loc[df["TotalPayBenefits"] == min_tpb]
lp_name = least_paid["EmployeeName"].values[0]
print(f"Employee with lowest Total Pay w/ Benefits is {lp_name} with ${min_tpb}")
# What's strange is that their TPB is a negative amount

#Question 9
print("QUESTION 9")
by_year = df.groupby('Year').mean()
tp_by_year = by_year['TotalPay']
print(tp_by_year)

#Question 10
print("QUESTION 10")
num_titles = len(pd.unique(df['JobTitle']))
print(f"There are {num_titles} unique job titles")

#Question 11
print("QUESTION 11")
most_common = df['JobTitle'].value_counts()[:7]
print(most_common)

#Question 12
print("QUESTION 12")
job_cts = df['JobTitle'].value_counts()
num_jobs = len(job_cts[job_cts.eq(1)])
print(f"There are {num_jobs} job titles represented by only one person")

#Question 13
print("QUESTION 13")
num_chief = len(df[df['JobTitle'].str.contains("Chief", case=False)])
print(f"There are {num_chief} people with Chief in their job title")

#Question 14
print("Question 14")
df['TitleLength'] = df['JobTitle'].apply(len)
title_len = df['TitleLength']
salary = df['TotalPayBenefits']
corr = title_len.corr(salary)
print(f"Correlation between title length and salary: {corr}")
#Since the correlation value is so small (less than .1) it is safe to say there is no correlation
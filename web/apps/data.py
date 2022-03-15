import pandas as pd


df = pd.read_csv("apps/OlympicsLugeSinglesResults.csv")

###########################
##### Clean the data ######
###########################

#convert dates to date times
df["Run Date"] = pd.to_datetime(df["Run Date"])

#remove "=" from times and convert to float
df["Start Time (Rk)"] = df["Start Time (Rk)"].str.replace("=", " ").str.replace(" ", "").astype(float)
df["Interval 1 Time (Rk)"] = df["Interval 1 Time (Rk)"].str.replace("=", " ").str.replace(" ", "").astype(float)
df["Interval 2 Time (Rk)"] = df["Interval 2 Time (Rk)"].str.replace("=", " ").str.replace(" ", "").astype(float)
df["Interval 3 Time (Rk)"] = df["Interval 3 Time (Rk)"].str.replace("=", " ").str.replace(" ", "").astype(float)
df.loc[df["Finish Time (Rk)"].str.contains(":") == True, "Finish Time (Rk)"] = df.loc[df["Finish Time (Rk)"].str.contains(":") == True, "Finish Time (Rk)"].str.split(":", expand = True)[1]
df["Finish Time (Rk)"] = df["Finish Time (Rk)"].str.replace("=", " ").str.replace(" ", "").astype(float)
df.loc[df["Finish Time (Rk)"] < 3, "Finish Time (Rk)"] = df.loc[df["Finish Time (Rk)"] < 3, "Finish Time (Rk)"] + 60









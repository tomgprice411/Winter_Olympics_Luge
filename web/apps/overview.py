from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps.data import df


df_2018 = df.loc[df["Run Date"].dt.year == 2018].copy()

df_2018 = df_2018[["Name", "Gender", "Start Time (Rk)", "Interval 1 Time (Rk)", 
            "Interval 2 Time (Rk)", "Interval 3 Time (Rk)", "Finish Time (Rk)"]].groupby(["Name", "Gender"]).min("Finish Time (Rk)").reset_index()


fig = go.Figure()

for gender in df_2018["Gender"].unique():
    df_plot = df_2018.loc[df_2018["Gender"] == gender].copy()
    fig.add_trace(go.Scatter(x = df_plot["Finish Time (Rk)"],
                            y = df_plot["Gender"],
                            mode = "markers"))

fig.show()


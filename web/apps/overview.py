from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps.data import df


df_2018 = df.loc[df["Run Date"].dt.year == 2018].copy()

df_2018 = df_2018[["Name", "Gender", "Start Time (Rk)", "Interval 1 Time (Rk)", 
            "Interval 2 Time (Rk)", "Interval 3 Time (Rk)", "Finish Time (Rk)"]].groupby(["Name", "Gender"]).min("Finish Time (Rk)")




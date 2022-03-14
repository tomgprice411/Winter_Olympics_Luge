from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from apps.data import df


df_2018 = df.loc[df["Run Date"].dt.year == 2018].copy()

df_2018 = df_2018[["Name", "Gender", "Start Time (Rk)", "Interval 1 Time (Rk)", 
            "Interval 2 Time (Rk)", "Interval 3 Time (Rk)", "Finish Time (Rk)"]].groupby(["Name", "Gender"]).min("Finish Time (Rk)").reset_index()

df_2018.rename(columns = {"Start Time (Rk)": "Start", "Interval 1 Time (Rk)": "Interval 1", "Interval 2 Time (Rk)": "Interval 2", 
                        "Interval 3 Time (Rk)": "Interval 3", "Finish Time (Rk)": "Finish"}, inplace = True)

df_2018_m = df_2018.loc[df_2018["Gender"] == "M"].copy()
df_2018_f = df_2018.loc[df_2018["Gender"] == "F"].copy()

df_winner_m = df_2018_m.groupby("Gender").min("Finish")
df_winner_f = df_2018_f.groupby("Gender").min("Finish")

df_2018_m_t = df_2018_m.melt(id_vars = ["Name", "Gender"], value_vars = ["Start", "Interval 1", "Interval 2", "Interval 3", "Finish"],
            var_name = "Interval", value_name = "Time (s)")
df_2018_f_t = df_2018_f.melt(id_vars = ["Name", "Gender"], value_vars = ["Start", "Interval 1", "Interval 2", "Interval 3", "Finish"],
            var_name = "Interval", value_name = "Time (s)")



fig = go.Figure()

for gender in df_2018_t["Gender"].unique():
    df_plot = df_2018_t.loc[df_2018_t["Gender"] == gender].copy()
    fig.add_trace(go.Scatter(x = df_plot["Time (s)"],
                            y = df_plot["Gender"],
                            mode = "markers"))

fig.show()





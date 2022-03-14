import plotly.graph_objects as go

from apps.overview import WINNER_F


df = df_2018_f_t.copy()
winner = WINNER_F
gender = "F"
athlete = "GOUGH Alex"

def create_dot_plot(df, winner, gender, athlete):



    fig = go.Figure()

    #add in trace for the other athletes
    fig.add_trace(go.Scatter(x = df.loc[~df["Name"].isin([athlete, winner]), "Time (s)"],
                            y = df.loc[~df["Name"].isin([athlete, winner]), "Gender"],
                            mode = "markers"))

    #add in trace for the selected athlete
    fig.add_trace(go.Scatter(x = df.loc[df["Name"] == athlete, "Time (s)"],
                            y = df.loc[df["Name"] == athlete, "Gender"],
                            mode = "markers"))

    #add in trace for the winning athlete
    fig.add_trace(go.Scatter(x = df.loc[df["Name"] == winner, "Time (s)"],
                            y = df.loc[df["Name"] == winner, "Gender"],
                            mode = "markers"))

    fig.update_layout(height = 350,
                        width = 1300,
                        showlegend = False,
                        plot_bgcolor = "white")




    fig.show()
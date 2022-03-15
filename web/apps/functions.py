import plotly.graph_objects as go
import plotly.express as px
from apps.overview import WINNER_F


COLOR_WINNER = "#000000"
COLOR_PRIMARY = "rgb(0, 159, 61)"
COLOR_PRIMARY_FADED = "rgb(0, 159, 61, 0.1)"
COLOR_SECONDARY = "rgb(0, 133, 199)"
COLOR_SECONDARY_FADED = "rgba(0, 133, 199, 0.1)"

COLOR_GREY_MID_LIGHT = "#bfbfbf"
COLOR_FONT = "#8c8c8c"
COLOR_POSITIVE = "#00CC33"
COLOR_NEGATIVE = "#FF0000"
COLOR_TITLE = "#737373"

FONT_SIZE = 12
FONT_TITLE_SIZE = 16
WIDTH_SINGLE = 1500
HEIGHT_SINGLE = 350

FONT_FAMILY = "Franklin Gothic"





df = df_2018_f_t.copy()
winner = WINNER_F
gender = "F"
athlete = "GOUGH Alex"



def create_dot_plot(df, winner, gender, athlete):

    if gender == "M":
        COLOR = COLOR_PRIMARY
    elif gender == "F":
        COLOR = COLOR_SECONDARY

    fig = go.Figure()

    #add in trace for the other athletes
    fig.add_trace(go.Scatter(x = df.loc[~df["Name"].isin([athlete, winner]), "Time (s)"],
                            y = df.loc[~df["Name"].isin([athlete, winner]), "Gender"],
                            marker = dict(color = COLOR),
                            opacity = 0.5,
                            mode = "markers"))

    #add in trace for the selected athlete
    fig.add_trace(go.Scatter(x = df.loc[df["Name"] == athlete, "Time (s)"],
                            y = df.loc[df["Name"] == athlete, "Gender"],
                            marker = dict(color = COLOR),
                            mode = "markers"))

    #add in trace for the winning athlete
    fig.add_trace(go.Scatter(x = df.loc[df["Name"] == winner, "Time (s)"],
                            y = df.loc[df["Name"] == winner, "Gender"],
                            marker = dict(color = COLOR_WINNER),
                            mode = "markers"))

    fig.update_layout(height = HEIGHT_SINGLE,
                        width = WIDTH_SINGLE,
                        showlegend = False,
                        plot_bgcolor = "white",
                        font = dict(color = COLOR_FONT, size = FONT_SIZE))

    fig.show()



    df["Color"] = COLOR_WINNER
    if gender == "F":
        df.loc[df["Name"] == athlete, "Color"] = COLOR_SECONDARY
        df.loc[~df["Name"].isin([athlete, winner]), "Color"] = COLOR_SECONDARY_FADED

    #add in trace for the other athletes
    fig = px.strip(df.loc[~df["Name"].isin([athlete, winner])], 
                    x = "Time (s)",
                    y = "Gender",
                    orientation = "h",
                    stripmode = "overlay",
                    color = "Color",
                    color_discrete_map="identity")

    fig.update_traces(jitter = 0.3)

    #add in trace for the selected athlete
    fig2 = px.strip(df.loc[df["Name"] == athlete], 
                    x = "Time (s)",
                    y = "Gender",
                    orientation = "h",
                    stripmode = "overlay",
                    color = "Color",
                    color_discrete_map="identity")

    fig2.update_traces(jitter = 0)

    #add in trace for the winning athlete
    fig3 = px.strip(df.loc[df["Name"] == winner], 
                    x = "Time (s)",
                    y = "Gender",
                    orientation = "h",
                    stripmode = "overlay",
                    color = "Color",
                    color_discrete_map="identity")

    fig3.update_traces(jitter = 0)

    fig.add_trace(fig2.data[0])
    fig.add_trace(fig3.data[0])


    fig.update_layout(height = HEIGHT_SINGLE,
                        width = WIDTH_SINGLE,
                        showlegend = False,
                        plot_bgcolor = "white",
                        font = dict(color = COLOR_FONT, size = FONT_SIZE),
                        yaxis = dict(visible = False))

    fig.add_annotation(text = "Winner: {}".format(winner.title()),
                        xref = "paper",
                        yref = "paper",
                        x = 0,
                        y = 1,
                        align = "left",
                        xanchor = "left",
                        showarrow = False,
                        font = dict(color = COLOR_WINNER))


    fig.add_annotation(text = "Selected: {}".format(athlete.title()),
                        xref = "paper",
                        yref = "paper",
                        x = 0,
                        y = 0.92,
                        align = "left",
                        xanchor = "left",
                        showarrow = False,
                        font = dict(color = COLOR))

    for interval, time in zip(df.loc[df["Name"] == athlete, "Time (s)"], df.loc[df["Name"] == athlete, "Interval"]):
        fig.add_annotation(text = "{}: {}".format(athlete.title()),
                        xref = "paper",
                        yref = "paper",
                        x = 0,
                        y = 0.92,
                        align = "left",
                        xanchor = "left",
                        showarrow = False,
                        font = dict(color = COLOR))


    fig.show()


import plotly.graph_objects as go
import plotly.express as px


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


def create_dot_plot(df, winner, gender, athlete):

    if gender == "M":
        COLOR = COLOR_PRIMARY
        TITLE = "Men"
    elif gender == "F":
        COLOR = COLOR_SECONDARY
        TITLE = "Women"

    df = df.merge(df.loc[df["Name"] == winner, ["Interval", "Time (s)"]].rename(columns = {"Time (s)": "Winning Time"}), on =["Interval"])
    df["Variance"] = df["Winning Time"] - df["Time (s)"]
    df["Time Label"] = df["Time (s)"].round(3).astype(str) + "s"
    df["Variance Label"] = [str(round(x, 3)) + "s" if x < 0 else "+" + str(round(x, 3)) + "s" for x in df["Variance"]]


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
                        yaxis = dict(visible = False),
                        xaxis = dict(range = [0,55], tickvals = [0, 10, 20, 30, 40, 50]))

    for time, time_label, interval, variance_label in zip(df.loc[df["Name"] == athlete, "Time (s)"], df.loc[df["Name"] == athlete, "Time Label"], df.loc[df["Name"] == athlete, "Interval"], df.loc[df["Name"] == athlete, "Variance Label"]):
        fig.add_annotation(text = '{}: <span style="color:'.format(interval) + COLOR + '">{}</span> <span style="color:'.format(time_label) + COLOR_NEGATIVE + '">{}</span> vs W'.format(variance_label),
                        xref = "x",
                        yref = "paper",
                        x = time,
                        y = 0.7,
                        align = "left",
                        xanchor = "left",
                        showarrow = False,
                        font = dict(color = COLOR_FONT, size = FONT_SIZE-2))


    fig.add_annotation(text = "{}'s Luge Fastest Trial Performance".format(TITLE),
                        xref = "paper",
                        yref = "paper",
                        x = 0,
                        y = 1.15,
                        showarrow = False,
                        align = "left",
                        xanchor = "left",
                        font = dict(color = COLOR_TITLE, size = FONT_TITLE_SIZE))


    fig.add_annotation(text = '<span style="color:' + COLOR_WINNER + '">{} (W)</span> vs <span style="color:'.format(winner.title()) + COLOR + '">{}</span>'.format(athlete.title()),
                    xref = "paper",
                    yref = "paper",
                    x = 0,
                    y = 1.03,
                    align = "left",
                    xanchor = "left",
                    showarrow = False,
                    font = dict(color = COLOR_TITLE)
                    )


    return fig





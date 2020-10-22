import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc

# Initialize app
external_stylesheets = ['assets/style.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Load data
dataset = pd.read_csv("data/DataForGood2020_updated.csv")
YEARS = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

# Mapbox parameters
mapbox_access_token = "pk.eyJ1IjoibWFoZGlrYXJhYmliZW4iLCJhIjoiY2tmeWlnZzJqMXhyMzJ0czgzcWc3ejViNyJ9.MsvguTk0F7cxDBaV1Zlm_g"
mapbox_style = "mapbox://styles/plotlymapbox/cjvprkf3t1kns1cqjxuxmwixz"


def disaster_type_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return dcc.Dropdown(

        options=[
            {'label': 'Drought', 'value': 'Drought'},
            {'label': 'Flood', 'value': 'Flood'},
            {'label': 'Storm', 'value': 'Storm'}
        ],
        value='Drought'
    )


def region_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return dcc.Dropdown(
        options=[
            {'label': 'Asia', 'value': 'Asia'},
            {'label': 'Europe', 'value': 'Europe'},
            {'label': 'Middle East', 'value': 'Middle East'},
            {'label': 'North America', 'value': 'North America'},
            {'label': 'South America', 'value': 'South America'}
        ],
        value=['Asia', 'Europe']
    )


def repartition_cart():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Flood'},
                # {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Storm'},
                # {'x': [1, 2, 3], 'y': [6, 7, 8], 'type': 'bar', 'name': u'Drought'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )


# App layout
app.layout = html.Div(
    id="root",
    children=[
        html.Div(
            id="header",
            children=[
                html.Img(id="logo", src=app.get_asset_url("WB_logo.jpg")),
                html.H4(children="Financial impact of disasters per year"),
                html.P(
                    id="description",
                    children="Dashboard description / project presentation",
                ),
            ],
        ),
        html.Div(
            id="app-container",
            children=[
                html.Div(
                    id="left-column",
                    children=[
                        html.Div(
                            id="slider-container",
                            children=[
                                html.P(
                                    id="slider-text",
                                    children="Drag the slider to change the year:",
                                ),
                                dcc.Slider(
                                    id="years-slider",
                                    min=min(YEARS),
                                    max=max(YEARS),
                                    value=min(YEARS),
                                    marks={
                                        str(year): {
                                            "label": str(year),
                                            "style": {"color": "#7fafdf"},
                                        }
                                        for year in YEARS
                                    },
                                ),
                            ],
                        ),
                        html.Div(
                            id="heatmap-container",
                            children=[
                                html.P(
                                    "Heatmap of age adjusted mortality rates \
                            from poisonings in year {0}".format(
                                        min(YEARS)
                                    ),
                                    id="heatmap-title",
                                ),
                                dcc.Graph(
                                    id="county-choropleth",
                                    figure=dict(
                                        layout=dict(
                                            mapbox=dict(
                                                layers=[],
                                                accesstoken=mapbox_access_token,
                                                style=mapbox_style,
                                                center=dict(
                                                    lat=38.72490, lon=-95.61446
                                                ),
                                                pitch=0,
                                                zoom=3.5,
                                            ),
                                            autosize=True,
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    id="graph-container",
                    children=[
                        html.P(id="chart-selector", children="Select chart:"),
                        dcc.Dropdown(
                            options=[
                                {
                                    "label": "Histogram of total number of deaths (single year)",
                                    "value": "show_absolute_deaths_single_year",
                                },
                                {
                                    "label": "Histogram of total number of deaths (1999-2016)",
                                    "value": "absolute_deaths_all_time",
                                },
                                {
                                    "label": "Age-adjusted death rate (single year)",
                                    "value": "show_death_rate_single_year",
                                },
                                {
                                    "label": "Trends in age-adjusted death rate (1999-2016)",
                                    "value": "death_rate_all_time",
                                },
                            ],
                            value="show_death_rate_single_year",
                            id="chart-dropdown",
                        ),
                        dcc.Graph(
                            id="selected-data",
                            figure=dict(
                                data=[dict(x=0, y=0)],
                                layout=dict(
                                    paper_bgcolor="#F4F4F8",
                                    plot_bgcolor="#F4F4F8",
                                    autofill=True,
                                    margin=dict(t=75, r=50, b=100, l=50),
                                ),
                            ),
                        ),
                    ],
                ),
            ],
        ),
    ],
)


if __name__ == '__main__':
    app.run_server()

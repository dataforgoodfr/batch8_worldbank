import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

# Initialize app
external_stylesheets = ['assets/style.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Load data
df_input = pd.read_csv("data/DataForGood2020_updated.csv")
df_map_data = df_input[['Year',
                        'Disaster Group',
                        'Disaster Subgroup',
                        'Disaster Type',
                        'Continent',
                        'Region',
                        'Country',
                        'ISO',
                        'Total Deaths',
                        'No Injured',
                        'No Affected',
                        'No Homeless',
                        'Total Affected',
                        'latitude',
                        'longitude',
                        'name'
                        ]]
df_map_data = (df_map_data
               .groupby(['Year', 'Region', 'latitude', 'longitude'])
               .agg({'Total Deaths': 'sum',
                     'No Injured': 'sum',
                     'No Affected': 'sum',
                     'No Homeless': 'sum',
                     'Total Affected': 'sum',
                     'name': 'count'})
               .reset_index())
YEARS = [1900, 1920, 1940, 1960, 1980, 2000, 2020, 2040, 2060, 2080, 2100]

DEFAULT_OPACITY = 0.8

# Mapbox parameters
mapbox_access_token = "pk.eyJ1IjoibWFoZGlrYXJhYmliZW4iLCJhIjoiY2tmeWlnZzJqMXhyMzJ0czgzcWc3ejViNyJ9.MsvguTk0F7cxDBaV1Zlm_g"
mapbox_style = "mapbox://styles/mahdikarabiben/ckgzi4dac1jez19qlanqcpp5l"


def disaster_type_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return dcc.RadioItems(

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




@app.callback(
    Output("county-choropleth", "figure"),
    [Input("years-slider", "value")],
    [State("county-choropleth", "figure")],
)
def display_map():
    fig = go.Figure(
        go.Scattermapbox(
            lat=df_map_data["latitude"],
            lon=df_map_data["longitude"],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=df_map_data['name'],
                color=df_map_data['name'],
                showscale=True,
                colorbar={'title': 'Disasters', 'titleside': 'top', 'thickness': 4, 'ticksuffix': ' %'},
            ),
            customdata=np.stack(
                (pd.Series(df_map_data['Country']),
                 df_map_data['No Injured'],
                 df_map_data['No Affected'],
                 df_map_data['Total Affected']),
                axis=-1
            ),

            hovertemplate="""
      <extra></extra>
      <em>%{customdata[0]}  </em><br>
      🚨  %{customdata[1]}<br>
      🏡  %{customdata[2]}<br>
      ⚰️  %{customdata[3]}
      """,
        )
    )

    # Specify layout information
    fig.update_layout(
        mapbox=dict(
            accesstoken=mapbox_access_token,
            style=mapbox_style,
            center=go.layout.mapbox.Center(lat=45, lon=-73),
            zoom=1
        ),
        margin=dict(l=0, r=0, t=0, b=0)
    )
    return fig



# App layout
app.layout = html.Div(
    id="root",
    children=[
        html.Div(
            id="app-container",
            children=[
                html.Div(
                    id="graph-container",
                    children=[
                        html.Img(className="wb-logo", src=app.get_asset_url("WB_logo.jpg"),
                                 style={'textAlign': 'left'}),
                        html.Br(),
                        html.Label('Disaster Type'),
                        disaster_type_card(),
                        html.Br(),
                        html.Br(),
                        region_card()
                    ],
                ),
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
                                dcc.RangeSlider(
                                    id="years-slider",
                                    min=1900,
                                    max=2100,
                                    step=10,
                                    value=[1900, 1920],
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
                                    "Heatmap of disaster damages in year {0}".format(
                                        min(YEARS)
                                    ),
                                    id="heatmap-title",
                                ),
                                dcc.Graph(
                                    id="county-choropleth",
                                    figure=display_map()
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)


@app.callback(Output("heatmap-title", "children"), [Input("years-slider", "value")])
def update_map_title(year):
    return "Heatmap of disaster damages in year {0}".format(year)


if __name__ == '__main__':
    app.run_server()

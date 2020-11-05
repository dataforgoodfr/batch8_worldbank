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
    return html.Div(
              children=[
                        html.H6("Disaster Type"),
                        dcc.Dropdown(

                            options=[
                                {'label': 'Drought', 'value': 'Drought'},
                                {'label': 'Flood', 'value': 'Flood'},
                                {'label': 'Storm', 'value': 'Storm'}
                            ],
                            value='Drought'
                        )
                    ]


    )


def region_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
              children=[
                        html.H6("Region"),
                        dcc.Dropdown(
                            options=[
                                {'label': 'Asia', 'value': 'Asia'},
                                {'label': 'Europe', 'value': 'Europe'},
                                {'label': 'Middle East', 'value': 'Middle East'},
                                {'label': 'North America', 'value': 'North America'},
                                {'label': 'South America', 'value': 'South America'}
                            ],
                            value=['Asia', 'Europe']
                        )
              ]
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

def damage_type():
    return  html.Div(
                                    className="padding-top-bot",
                                    children=[
                                        html.H6("Damage Type"),
                                        dcc.RadioItems(
                                            id="chart-type",
                                            options=[
                                                {"label": " Human", "value": "box"},
                                                {
                                                    "label": " Dollars",
                                                    "value": "violin",
                                                },
                                            ],
                                            value="violin",
                                            labelStyle={
                                                "display": "inline-block",
                                                "padding": "12px 12px 12px 0px",
                                            },
                                        ),
                                    ],
                                )

def climate_scenario():

    return  html.Div(
                     children=[
                               html.H6("Climate scenario"),
                               dcc.RadioItems(
                                    id="cluster-ctl",
                                    options=[
                                        {"label": " 4", "value": "4"},
                                        {
                                            "label": " 3",
                                            "value": "3",
                                        },
                                        {
                                            "label": " 2",
                                            "value": "2",
                                        },
                                        {
                                            "label": " 1",
                                            "value": "1",
                                        },

                                    ],
                                    value="no-cluster",
                                ),
                            ]
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
                        html.Div(
                                children=[
                                html.Img(id="logo",src=app.get_asset_url("WB_logo.jpg")),
                                html.Span(

                                            html.H3(dcc.Markdown("**Disaster Economics Map Explorer**")),

                                    ),
                                ]
                        ),
                        html.Div(
                                className="pretty_container",
                                children=[disaster_type_card()]
                        ),
                        html.Br(),
                        html.Br(),
                        html.Div(
                                className="pretty_container",
                                children=[region_card()]
                        ),

                        html.Br(),
                        html.Div(
                                className="pretty_container",
                                children=[damage_type()]
                        ),

                        html.Br(),
                        html.Div(
                                className="pretty_container",
                                children=[climate_scenario()]
                        ),


                    ],
                ),

                html.Div(
                   className="pretty_container-2",
               #     children=[
               #         html.P(id="world", children="WORLD"),
               #         html.Br(),
               #         html.Br(),
               #         repartition_cart(),
                        #damage_type()
               #     ],
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

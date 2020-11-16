import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Initialize app
external_stylesheets = ['assets/style.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# load geojson
with open('data/un_subregion_contours.geojson') as json_data:
    regions_data = json.load(json_data)

# Load data
df_input = pd.read_csv("data/randominput.csv")
df_map_data = df_input[['Decade',
                        'UN_Geosheme_Subregion',
                        'Disaster_Type',
                        'RCP',
                        'Financial_Impact',
                        'Human_Impact',
                        '#LoDO',
                        '#MeDO',
                        '#HiDO',
                        '°C']]
df_map_data = df_map_data.sort_values(by=['UN_Geosheme_Subregion'])
# df_map_data = (df_map_data
#                .groupby(['Year', 'Region', 'Country', 'latitude', 'longitude'])
#                .agg({'Total Deaths': 'sum',
#                      'No Injured': 'sum',
#                      'No Affected': 'sum',
#                      'No Homeless': 'sum',
#                      'Total Affected': 'sum',
#                      'name': 'count'})
#                .reset_index())
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990,
         2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100]


DESASTER_TYPE = ["Drought", "Flood", "Storm"]
SCENARIO_SELECTOR = ["0°C","2°C","4°C"]


DEFAULT_OPACITY = 0.8


# Mapbox parameters
mapbox_access_token = "pk.eyJ1IjoibWFoZGlrYXJhYmliZW4iLCJhIjoiY2tmeWlnZzJqMXhyMzJ0czgzcWc3ejViNyJ9.MsvguTk0F7cxDBaV1Zlm_g"
mapbox_style = "mapbox://styles/mahdikarabiben/ckgzi4dac1jez19qlanqcpp5l"


def choropleth_map(df):
    return go.Figure(
        px.choropleth_mapbox(
            geojson=regions_data,
            locations=df['UN_Geosheme_Subregion'].tolist(),
            featureidkey="properties.subregion",
            color=df['Human_Impact'].tolist(),
            color_continuous_scale="Viridis",
            mapbox_style=mapbox_style,
            opacity=0.8,
            zoom=1,
            hover_name=df['UN_Geosheme_Subregion'].tolist())
    )


def disaster_type_card():
    """
     :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        children=[
            
            html.H5(dcc.Markdown("**Disaster Selector**")),
            dcc.RadioItems(

                options=[
                    {'label': 'Drought', 'value': 'Drought'},
                    {'label': 'Flood', 'value': 'Flood'},
                    {'label': 'Storm', 'value': 'Storm'}
                ],
                value='Drought',
                labelStyle={"display": "inline-block",
                            "margin-top": "20px",
                            "font-size": "16px",
                            "padding": "12px 12px 12px 0px",
                },
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
    return html.Div(
        className="padding-top-bot",
        children=[
            html.H5(dcc.Markdown("**Disaster Selector**")),
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
    return html.Div(
        children=[
            html.H6(dcc.Markdown("**Scenario Selector**")),
            html.Br(),
            dcc.RangeSlider(   min=0,
                               max=4,
                               step=1,
                               value=[0, 5],
                               marks={1: "2°C", 2: "3°C", 3: "4°C",},
                                          
                            ),

        ]
    )


'''@app.callback(
    Output("county-choropleth", "figure"),
    [Input("years-slider", "value")],
    [State("county-choropleth", "figure")],
)'''


def display_map(df):
    fig = choropleth_map(df)
    # Specify layout information
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        mapbox_accesstoken=mapbox_access_token
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
                    id="Rectangle_Menu",
                    children=[
                        html.Div(

                       children=[
                                html.Img(id="logo",src=app.get_asset_url("WorldBank_Logo@2x.png")),

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
                        html.Div(
                            className="pretty_container",
                            children=[
                                html.H6(dcc.Markdown("**Damage Selector**")),
                                html.Img( className="icon" , src=app.get_asset_url("IconHuman.svg")),
                                html.Img( className="icon",  src=app.get_asset_url("IconFinancial.svg")),
                                html.Img( className="icon",  src=app.get_asset_url("IconDisaster.svg")),
                            ]

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
                    # damage_type()
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
                                dcc.Slider(
                                    id="years-slider",
                                    min=1900,
                                    max=2100,
                                    step=10,
                                    value=1900,
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
                                    "Choropleth map of disaster damages in year {0}".format(
                                        min(YEARS)
                                    ),
                                    id="heatmap-title",
                                ),
                                dcc.Graph(
                                    id="county-choropleth",
                                    figure=display_map(df_map_data[df_map_data['Decade'] == 1900])
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


@app.callback(Output("county-choropleth", "figure"), [Input("years-slider", "value")])
def update_map(year):
    df_decade = df_map_data[df_map_data['Decade'] == year]
    return display_map(df_decade)


if __name__ == '__main__':

    app.run_server(debug=True, host="0.0.0.0", port=80)

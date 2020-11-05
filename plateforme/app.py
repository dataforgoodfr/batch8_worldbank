import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

#import utils.dash_reusable_components as drc
#import utils.figures as figs

# Initialize app
external_stylesheets = ['assets/style.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Load data
df_input = pd.read_csv("data/DataForGood2020_updated.csv")
YEARS = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

BINS = [
    "0-2",
    "2.1-4",
    "4.1-6",
    "6.1-8",
    "8.1-10",
    "10.1-12",
    "12.1-14",
    "14.1-16",
    "16.1-18",
    "18.1-20",
    "20.1-22",
    "22.1-24",
    "24.1-26",
    "26.1-28",
    "28.1-30",
    ">30",
]

DEFAULT_COLORSCALE = [
    "#f2fffb",
    "#bbffeb",
    "#98ffe0",
    "#79ffd6",
    "#6df0c8",
    "#69e7c0",
    "#59dab2",
    "#45d0a5",
    "#31c194",
    "#2bb489",
    "#25a27b",
    "#1e906d",
    "#188463",
    "#157658",
    "#11684d",
    "#10523e",
]

DEFAULT_OPACITY = 0.8

# Mapbox parameters
mapbox_access_token = "pk.eyJ1IjoibWFoZGlrYXJhYmliZW4iLCJhIjoiY2tmeWlnZzJqMXhyMzJ0czgzcWc3ejViNyJ9.MsvguTk0F7cxDBaV1Zlm_g"
mapbox_style = "mapbox://styles/plotlymapbox/cjvprkf3t1kns1cqjxuxmwixz"


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
                                    "Heatmap of disaster damages in year {0}".format(
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
            ],
        ),
    ],
)


@app.callback(
    Output("county-choropleth", "figure"),
    [Input("years-slider", "value")],
    [State("county-choropleth", "figure")],
)
def display_map(year, figure):
    cm = dict(zip(BINS, DEFAULT_COLORSCALE))

    data = [
        dict(
            lat=df_input["latitude"],
            lon=df_input["longitude"],
            text=df_input["Country"],
            type="scattermapbox",
            hoverinfo="text",
            marker=dict(size=5, color="white", opacity=1),
        )
    ]

    annotations = [
        dict(
            showarrow=False,
            align="right",
            text="<b>Disasters damage<br>per county per year</b>",
            font=dict(color="#2cfec1"),
            bgcolor="#1f2630",
            x=0.95,
            y=0.95,
        )
    ]

    for i, bin in enumerate(reversed(BINS)):
        color = cm[bin]
        annotations.append(
            dict(
                arrowcolor=color,
                text=bin,
                x=0.95,
                y=0.85 - (i / 20),
                ax=-60,
                ay=0,
                arrowwidth=5,
                arrowhead=0,
                bgcolor="#1f2630",
                font=dict(color="#2cfec1"),
            )
        )

    if "layout" in figure:
        lat = figure["layout"]["mapbox"]["center"]["lat"]
        lon = figure["layout"]["mapbox"]["center"]["lon"]
        zoom = figure["layout"]["mapbox"]["zoom"]
    else:
        lat = 38.72490
        lon = -95.61446
        zoom = 3.5

    layout = dict(
        mapbox=dict(
            layers=[],
            accesstoken=mapbox_access_token,
            style=mapbox_style,
            center=dict(lat=lat, lon=lon),
            zoom=zoom,
        ),
        hovermode="closest",
        margin=dict(r=0, l=0, t=0, b=0),
        annotations=annotations,
        dragmode="lasso",
    )

    base_url = "https://raw.githubusercontent.com/jackparmer/mapbox-counties/master/"
    for bin in BINS:
        geo_layer = dict(
            sourcetype="geojson",
            source=base_url + str(year) + "/" + bin + ".geojson",
            type="fill",
            color=cm[bin],
            opacity=DEFAULT_OPACITY,
            # CHANGE THIS
            fill=dict(outlinecolor="#afafaf"),
        )
        layout["mapbox"]["layers"].append(geo_layer)

    fig = dict(data=data, layout=layout)
    return fig


@app.callback(Output("heatmap-title", "children"), [Input("years-slider", "value")])
def update_map_title(year):
    return "Heatmap of disaster damages in year {0}".format(year)


if __name__ == '__main__':
    app.run_server()

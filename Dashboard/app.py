import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_daq as daq
import dash_core_components as dcc
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

DisasterTypes= df_input['Disaster_Type'].unique()
DEFAULT_OPACITY = 0.8

#Title App
def Title_App():
    return html.Div(
        className="pretty_container",
        children=[
            html.Img(id="logo",src=app.get_asset_url("WorldBank_Logo@2x.png")),
            html.Br(),
            dcc.Markdown("""
            ### Disaster Economics
            ### Map Explorer
            """),
            ],
    )

# Mapbox parameters
mapbox_access_token = "pk.eyJ1IjoibWFoZGlrYXJhYmliZW4iLCJhIjoiY2tmeWlnZzJqMXhyMzJ0czgzcWc3ejViNyJ9.MsvguTk0F7cxDBaV1Zlm_g"
mapbox_style = "mapbox://styles/mahdikarabiben/ckgzi4dac1jez19qlanqcpp5l"


def choropleth_map(df,disaster,impact, colorimpact):
    return go.Figure(
        px.choropleth_mapbox(
            geojson=regions_data,
            locations=df['UN_Geosheme_Subregion'].tolist(),
            featureidkey="properties.subregion",
            color=df[str(impact)].tolist(),
            color_continuous_scale= colorimpact,
            mapbox_style=mapbox_style,
            opacity=0.8,
            zoom=1,
            hover_name=df['UN_Geosheme_Subregion'].tolist(),
            )
    )


def disaster_type_card():
    """
     :return: A Div containing the 3 disaster options
    """
    return html.Div(
        children=[
            html.H5(dcc.Markdown("**Disaster Selector**")),
            dcc.RadioItems(
                id="Disaster-Selector",
                options=[
                {'label':i, 'value':i} for i in DisasterTypes
                ],
                value='Droughts',
                labelStyle={"display": "inline-block",
                            "margin-top": "0px",
                            "font-size": "16px",
                            "padding": "12px 12px 12px 0px",
                            },
                labelClassName="data-group-labels",)
                ]

    )

def climate_scenario():
    return html.Div(
        children=[
            html.H5(dcc.Markdown("**Scenario Selector**")),
            html.Br(),
            daq.Thermometer(
                    id='my-daq-thermometer',
                    min= 0,
                    max=8.5,
                    scale = {
                        'start' : 0,
                        'interval' : 8.5,
                        'labelInterval' : 2,
                        'custom' : {2 : 2.6,
                                    4 : 4.5,
                                    6 : 6.0 }
                        },
                    units="°C",
                    value= 0
                    )
        ]
    )


'''@app.callback(
    Output("county-choropleth", "figure"),
    [Input("years-slider", "value")],
    [State("county-choropleth", "figure")],
)'''


def display_map(df,disaster,impact, colorimpact):
    fig = choropleth_map(df,disaster,impact, colorimpact)

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
                        className="pretty-container",
                        children=[Title_App()]
                        ),
                        html.Div(
                            className="pretty_container",
                            children=[disaster_type_card()]
                        ),
                        html.Br(),
                        html.Div(
                            className="pretty_container",
                            children=[
                                html.H5(dcc.Markdown("**Impact Selector**")),
                                #html.Div(html.Img( className="icon" , src=app.get_asset_url("IconHuman.svg"))),
                                html.Div(
                                children=[
                                #html.Img(className="icon" , src=app.get_asset_url("IconHuman.svg")),
                                daq.ToggleSwitch(
                                    id='Impact-Selector',
                                    label=['Human','Financial'],
                                    value=False,
                                    style={
                                        'width':'100%' ,
                                        'marginTop': '30px',
                                        'marginBottom':'30px'},
                                    theme  =  {
                                        'dark': False,
                                        'detail': '#4525F2',
                                        'primary': '#4525F2',
                                        'secondary': '#F2F4F8',
                                        }
                                    ),
                                #html.Img(className="icon",  src=app.get_asset_url("IconFinancialBlack.svg")),
                                ],
                                ),
                            ],
                        ),
                        html.Br(),
                        html.Div(
                            className="pretty_container",
                            children=[climate_scenario()]
                        ),
                        html.Br(),
                        html.Div(
                            className="pretty_container-2",
                            children=[
                            html.Button('Expand World Figures', id='button.button-primary'),
                            ]
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
                    id="right-column",
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
                                    figure=display_map(df_map_data[df_map_data['Decade'] == 1900], 'Droughts', 'Human_Impact','reds')
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


# YEAR INPUT & IMPACT TYPE
@app.callback(
Output("county-choropleth", "figure"),
Input("years-slider", "value"),
Input("Disaster-Selector","value"),
Input("Impact-Selector", "value"))
def update_map(year,DisasterType,ImpactType):
    df_decade_disaster = df_map_data[(df_map_data['Decade'] == year) & (df_map_data['Disaster_Type'] == DisasterType)]
    df_disaster = ""
    if ImpactType == False:
        color= "reds"
        type ='Human_Impact'
        #df_impact = px.choropleth_mapbox(color= df_map_data['Human_Impact'].tolist())
        #df_color = px.choropleth_mapbox(color_continuous_scale= colorimpact)

    else:
        color = "purples"
        type = 'Financial_Impact'
        #df_impact = px.choropleth_mapbox(color= df_map_data['Financial_Impact'].tolist())
        #df_color = px.choropleth_mapbox(color_continuous_scale= colorimpact)
    return display_map(df_decade_disaster,df_disaster, type, color)


#    if value == 'False':
#        return px.choropleth_mapbox(color=df['Financial_Impact'].tolist()
 #else:
#px.choropleth_mapbox(color=df['Financial_Impact'].tolist()

if __name__ == '__main__':
    app.run_server(debug=True, host="127.0.0.1", port=8050)

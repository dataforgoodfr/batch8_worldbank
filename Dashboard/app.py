import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_daq as daq
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Initialize app
external_stylesheets = ['assets/style.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# load geojson
with open('data/un_subregion_contours.geojson') as json_data:
    regions_data = json.load(json_data)

# Load data
df_input = pd.read_csv("data/randominput.csv", decimal=".")
df_map_data = df_input[['Decade',
                        'UN_Geosheme_Subregion',
                        'Disaster_Type',
                        'RCP',
                        'Financial_Impact',
                        'Human_Impact',
                        'DO',
                        '°C']]
df_map_data = df_map_data.sort_values(by=['UN_Geosheme_Subregion'])

YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990,
         2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090]

DisasterTypes = df_input['Disaster_Type'].unique()
df_map_data["RCP"].fillna(value=0,inplace=True)
Degree = df_input['RCP'].unique()
DEFAULT_OPACITY = 0.8

# Mapbox parameters
mapbox_access_token = "pk.eyJ1IjoibWFoZGlrYXJhYmliZW4iLCJhIjoiY2tmeWlnZzJqMXhyMzJ0czgzcWc3ejViNyJ9.MsvguTk0F7cxDBaV1Zlm_g"
mapbox_style = "mapbox://styles/mahdikarabiben/ckgzi4dac1jez19qlanqcpp5l"


# Title App
def Title_App():
    return html.Div(
        className="pretty_container",
        children=[
            html.Img(id="logo", src=app.get_asset_url("WorldBank_Logo@2x.png")),
            html.Br(),
            dcc.Markdown("""
            ### Disaster Economics
            ### Map Explorer
            """),
        ],
    )


def choropleth_map(df, impact, colordisaster):
    return go.Figure(
        px.choropleth_mapbox(
            geojson=regions_data,
            locations=df['UN_Geosheme_Subregion'].tolist(),
            featureidkey="properties.subregion",
            color=df[str(impact)].tolist(),
            color_continuous_scale=colordisaster,
            mapbox_style=mapbox_style,
            opacity=0.8,
            zoom=1,
            hover_name=df['UN_Geosheme_Subregion'].tolist(),
            labels={"color": "damages"}
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
                    {'label': i, 'value': i} for i in DisasterTypes
                ],
                value='Droughts',
                labelStyle={"display": "inline-block",
                            "margin-top": "0px",
                            "font-size": "16px",
                            "padding": "12px 12px 12px 0px",
                            },
                labelClassName="data-group-labels", )
        ]

    )


def climate_scenario():
    return html.Div(
        children=[
            html.H5(dcc.Markdown("**Scenario Selector**")),
            html.Br(),
            dcc.Slider(
                        id="scenario-slider",
                        min=0,
                        max=10,
                        value=0,
                        step=None,
                       # marks={2.6: "2.6°C", 4.5: "4.5°C", 6.0: "6.0°C",8.5:"8.5°C"},
                        marks={
                                0: {'label': '0', 'style': {'color': '#77b0b1'}},
                                2.6: {'label': '2.6', 'style': {'color': '#77b0b1'}},
                                4.5: {'label': '4.5'},
                                6: {'label': '6.0'},
                                8.5: {'label': '8.5', 'style': {'color': '#f50'}}
                        },
                        disabled=False                        

                       )
        ]               
)


def display_map(df, impact, colordisaster):
    fig = choropleth_map(df, impact, colordisaster)

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
                                # html.Div(html.Img( className="icon" , src=app.get_asset_url("IconHuman.svg"))),
                                html.Div(
                                    children=[
                                        # html.Img(className="icon" , src=app.get_asset_url("IconHuman.svg")),
                                        daq.ToggleSwitch(
                                            id='Impact-Selector',
                                            label=['Human', 'Financial'],
                                            value=False,
                                            style={
                                                'width': '100%',
                                                'marginTop': '30px',
                                                'marginBottom': '30px'},
                                            theme={
                                                'dark': False,
                                                'detail': '#4525F2',
                                                'primary': '#4525F2',
                                                'secondary': '#F2F4F8',
                                            }
                                        ),
                                        # html.Img(className="icon",  src=app.get_asset_url("IconFinancialBlack.svg")),
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
                                dcc.RangeSlider(
                                    id="years-slider",
                                    min=1900,
                                    max=2090,
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
                                    "Choropleth map of disaster damages from {0} to {1}".format(
                                        min(YEARS), min(YEARS) + 20
                                    ),
                                    id="heatmap-title",
                                ),
                                dcc.Graph(
                                    id="county-choropleth",
                                    figure=display_map(
                                        df_map_data[(df_map_data['Decade'] >= 1900)
                                                    & (df_map_data['Decade'] <= 1920)
                                                    & (df_map_data['Disaster_Type'] == 'Droughts')
                                                    & (df_map_data['RCP'] == 2.6)],
                                        'Human_Impact', 'reds')
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
    return "Choropleth map of disaster damages from {0} to {1}".format(year[0], year[1])


# YEAR INPUT & IMPACT TYPE
@app.callback(
    Output("county-choropleth", "figure"),
    Input("years-slider", "value"),
    Input("Disaster-Selector", "value"),
    # Input("temp-slider","value"),
    # for callback : & (df_map_data['RCP'] == temp
    # def update_map(year,DisasterType,temp,ImpactType):
    Input("Impact-Selector", "value"),
    Input("scenario-slider","value")
    )
def update_map(year, DisasterType, ImpactType,RcpType):
    df_decade_disaster_temp = (df_map_data[
        ((df_map_data['Decade'] >= year[0]) & (df_map_data['Decade'] <= year[1]) & (
                df_map_data['Disaster_Type'] == DisasterType)& (df_map_data['RCP']== RcpType))]
    )

    if DisasterType == "Droughts":
        color= "YlOrRd"
        DisasterType ='Droughts'
       
    elif DisasterType == "Storms":
        color = "RdPu"
        DisasterType = 'Storms'
       
    elif DisasterType == "Floods":
        color = "Blues"
        DisasterType = 'Floods'



    if not ImpactType:
        #color = "reds"
        impact_type = 'Human_Impact'
    else:
        #color = "purples"
        impact_type = 'Financial_Impact'
    df_decade_disaster_temp = (df_decade_disaster_temp
                               .groupby(['UN_Geosheme_Subregion'])[impact_type]
                               .sum()
                               .reset_index())
    
    return display_map(df_decade_disaster_temp, impact_type, color)


def hide_slider(year):
    if year[0] >= 2020:

        return "Choropleth map of disaster damages from {0} to {1}".format(year[0], year[1])


if __name__ == '__main__':
    app.run_server(debug=True, host="127.0.0.1", port=8050)

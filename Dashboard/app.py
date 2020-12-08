# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This software was firstly designed during the batch #8 of Data For Good sessions.
# Its main aim is to explore ways of displaying KPI for the World Bank in order to help
# decision makers in their prospective analysis. Especially about natural disasters impacts on
# humans and economies around the world till the end of the century.
#
# Main functions:
# - Launch a Dash server
# - Display a HTML page on the dash server, populated with controls and graphs
# - Connect to precalculated data and display graphs and choropleth maps
#
# Contributors:
# Madhi Karabiden, Marc Alencon, Morgan Davidson, Alexis de Pampelonne, Nicolas Piquemal
#
# TODO list:
# - be able to display regions in grey even when no data available, with a dedicated legend
# - find a way to keep the same min/max scale on the map for a tuple of (disaster,feature) when changing decades
# - avoid using the strings displayed on the UI as names for the variables (disaster, magnitude)
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~ MODULES

import pandas as pd
import json
# Graph library
import plotly.express as px
import plotly.graph_objects as go
# Dashboard
import dash
import dash_html_components as html
# import dash_daq as daq
import dash_core_components as dcc
from dash.dependencies import Input, Output

# ~~~~~ INITIALISATION

# Style

external_stylesheets = ['assets/style.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Import Geodata

with open('data/un_subregion_contours.geojson') as json_data:
    regions_data = json.load(json_data)

# Import dataset to display

df = pd.read_csv("data/input.csv", decimal=".")
dict_dataset_labels = {
    "UN_Geosheme_Subregion": "UN subregion",
    "Disaster_Type": "Type of disaster",
    "RCP": "Climate prospective scenario",
    "Financial_Impact": "Total cost $US",
    "Human_Impact": "Affected people",
    "DO": "Nb of events",
    "°C": "Average temperature (°C)",
    "Rain": "Rainfall",
}
list_disasters = df['Disaster_Type'].unique()
list_features = ['Number of Occurrences', 'Financial impact', 'Human impact']
list_rcp = df['RCP'].unique()
YEARS = list(df.Decade.drop_duplicates())
dict_dataset_aggregation_method = {
    "Financial_Impact": "sum",
    "Human_Impact": "sum",
    "DO": "sum",
    "°C": "mean",
    "Rain": "mean",
}

# Data preparation

df_map_data = df.sort_values(by=['UN_Geosheme_Subregion'])
df_map_data["RCP"].fillna(value=0, inplace=True)

# Mapbox credentials

mapbox_access_token = "pk.eyJ1IjoibWFoZGlrYXJhYmliZW4iLCJhIjoiY2tmeWlnZzJqMXhyMzJ0czgzcWc3ejViNyJ9.MsvguTk0F7cxDBaV1Zlm_g"
mapbox_style = "mapbox://styles/mahdikarabiben/ckgzi4dac1jez19qlanqcpp5l"

# Choropleth color settings to display features on the map
dict_feature_colors = {
    "Droughts": "YlOrRd",
    "Storms": "RdPu",
    "Floods": "Blues",
}


# ~~~~~ FUNCTIONS

# Title & Logo

def Title_App():
    return html.Div(
        className="pretty_container",
        children=[
            html.Img(id="logo", src=app.get_asset_url("WorldBank_Logo@2x.png")),
            html.Br(),
            dcc.Markdown("""
        ### Natural Disasters Map
        """),
        ],
    )


# Build the choropleth map from data in dataframe and regional contours in geojson

def choropleth_map(df, impact, colordisaster):
    return go.Figure(
        px.choropleth_mapbox(
            data_frame=df,
            geojson=regions_data,
            locations='UN_Geosheme_Subregion',
            featureidkey="properties.subregion",
            color=impact,
            color_continuous_scale=colordisaster,
            mapbox_style=mapbox_style,
            opacity=0.8,
            zoom=1,
            hover_name='UN_Geosheme_Subregion',
            labels=dict_dataset_labels,
        )
    )


# Display the map

def display_map(df, impact, colordisaster):
    fig = choropleth_map(df, impact, colordisaster)

    # Specify layout information
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        mapbox_accesstoken=mapbox_access_token
    )
    return fig


# Disaster selector

def disaster_type_card():
    """
     :return: A Div containing the 3 disaster options
    """
    return html.Div(
        children=[
            html.H5(dcc.Markdown("**Select a Disaster**")),
            dcc.RadioItems(
                id="Disaster-Selector",
                options=[{'label': i, 'value': i} for i in list_disasters],
                value='Droughts',
                labelStyle={"display": "inline-block",
                            "margin-top": "0px",
                            "font-size": "16px",
                            "padding": "12px 12px 12px 0px",
                            },
                labelClassName="data-group-labels",
            )
        ]

    )


# Magnitude selector

def magnitude_type_card():
    """
     :return: A Div containing the 3 magnitude options
    """
    return html.Div(
        children=[
            html.H5(dcc.Markdown("**Select a Magnitude**")),
            dcc.RadioItems(
                id="Magnitude-Selector",
                options=[{'label': i, 'value': i} for i in list_features],
                value='Number of Occurrences',
                labelStyle={  # "display": "inline-block",
                    "margin-top": "0px",
                    "font-size": "16px",
                    "padding": "12px 12px 12px 0px",
                },
                labelClassName="data-group-labels",
            )
        ]

    )


# RCP selector

def climate_scenario():
    return html.Div(
        children=[
            html.H5(dcc.Markdown("**Select a RCP**")),
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


def display_graph():
    fig = px.bar(df_map_data, x="UN_Geosheme_Subregion", y="Financial_Impact",
                 color="Disaster_Type", barmode="group")
    return fig

    # ~~~~~ MAIN HTML LAYOUT

    # Specify layout information


# Layout

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
                            className="pretty_container-3",
                            children=[magnitude_type_card()]
                        ),
                        html.Br(),
                        html.Div(
                            className="pretty_container",
                            children=[climate_scenario()]
                        ),
                        html.Br(),
                        html.Div(
                            className="pretty_container-2",
                            children=[html.Button('Expand World Figures', id='button.button-primary')]
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
                                    children="Drag the slider to choose the decade(s)",
                                ),
                                dcc.RangeSlider(
                                    id="years-slider",
                                    min=1900,
                                    max=2090,
                                    step=10,
                                    value=[1900, 1920],
                                    marks={
                                        str(year): {"label": str(year), "style": {"color": "#7fafdf"}} for year in YEARS
                                    },
                                ),
                            ],
                        ),
                        html.Div(
                            id="heatmap-container",
                            children=[
                                html.P(
                                    "Choropleth map of disaster damages from {0} to {1}".format(min(YEARS),
                                                                                                min(YEARS) + 20),
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
                        html.Div(
                            className="pretty_container-2",
                            children=[
                                dcc.Graph(
                                    id="bar-chart",
                                    figure=display_graph()
                                ),
                            ]
                        )
                    ],
                ),
            ],
        ),
    ],
)


# ~~~~~ CALLBACKS TO UPDATE THE DASHBOARD BASED ON USER ACTIONS

# Update map title according to selected decades

@app.callback(
    Output("bar-chart", "figure"),
    [Input("county-choropleth", "clickData"),
     Input("years-slider", "value"),
     Input("Disaster-Selector", "value"),
     Input("Magnitude-Selector", "value"),
     Input("scenario-slider", "value")
     ])
def update_bar_chart(map_input, years, disaster, impact, scenario):
    if map_input:
        location = map_input.get('points')[0].get('location')
    else:
        location = 'Western Europe'

    df_decade_disaster_temp = (df_map_data[
        ((df_map_data['UN_Geosheme_Subregion'] == location) & (df_map_data['Decade'] >= years[0])
         & (df_map_data['Decade'] <= years[1]) & (df_map_data['Disaster_Type'] == disaster)
         & (df_map_data['RCP'] == scenario))]
    )
    fig = px.bar(df_decade_disaster_temp, x="Decade", y="Financial_Impact",
                 color="Disaster_Type", barmode="group")
    return fig


@app.callback(Output("heatmap-title", "children"), [Input("years-slider", "value")])
def update_map_title(year):
    return "Choropleth map from the beginning of the {0}s to the end of the {1}s".format(year[0], year[1])


# Update the data selection sent to the map - period, magnitude, impact

@app.callback(
    Output("county-choropleth", "figure"),
    Input("years-slider", "value"),
    Input("Disaster-Selector", "value"),
    # Input("temp-slider","value"),
    # for callback : & (df_map_data['RCP'] == temp
    # def update_map(year,DisasterType,temp,MagnitudeType):
    Input("Magnitude-Selector", "value"),
    Input("scenario-slider", "value")
)
def update_map(year, DisasterType, MagnitudeType, RcpType):
    '''
    Update the map according to the parameters selected by the user
    '''
    # Selection of the slice of data to send to the map
    df_decade_disaster_temp = df_map_data[
        (df_map_data['Decade'] >= year[0])
        & (df_map_data['Decade'] <= year[1])
        & (df_map_data['Disaster_Type'] == DisasterType)
        & (df_map_data['RCP'] == RcpType)].copy()

    # Get the color scale settings to display the choropleth
    color = dict_feature_colors[DisasterType]

    # Select the feature in the dataset
    if MagnitudeType == "Number of Occurrences":
        magnitude_type = 'DO'
    elif MagnitudeType == "Financial impact":
        magnitude_type = 'Financial_Impact'
    elif MagnitudeType == 'Human impact':
        magnitude_type = 'Human_Impact'

    # Select the feature and aggregate its data on the selected decades
    if dict_dataset_aggregation_method[magnitude_type] == 'sum':
        df_decade_disaster_temp = (df_decade_disaster_temp
                                   .groupby(['UN_Geosheme_Subregion'])[magnitude_type]
                                   .sum()
                                   .reset_index())
    elif dict_dataset_aggregation_method[magnitude_type] == 'mean':
        df_decade_disaster_temp = (df_decade_disaster_temp
                                   .groupby(['UN_Geosheme_Subregion'])[magnitude_type]
                                   .mean()
                                   .reset_index())

    return display_map(df_decade_disaster_temp, magnitude_type, color)


# Not in used anymore

# def hide_slider(year):
#    if year[0] >= 2020:
#        return "Choropleth map of disaster damages from {0} to {1}".format(year[0], year[1])


# ~~~~~ MAIN - when file executed as a standalone application

if __name__ == '__main__':
    app.run_server(debug=True, host="127.0.0.1", port=8050)

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
# Mahdi Karabiben, Marc Alencon, Morgan Davidson, Alexis de Pampelonne, Nicolas Piquemal
#
# TODO list:
# - be able to display regions in grey even when no data available, with a dedicated legend
# - find a way to keep the same min/max scale on the map for a tuple of (disaster,feature) when changing decades
# - avoid using the strings displayed on the UI as names for the variables (disaster, magnitude)
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~~~~~~~
#       MODULES
# ~~~~~~~~~~~~~~~~~~~

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
from dash.dependencies import Input, Output, State
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc

# ~~~~~~~~~~~~~~~~~~~
#   INITIALIZATION
# ~~~~~~~~~~~~~~~~~~~

# Style

external_stylesheets = ["assets/style.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Import Geodata

with open("data/un_subregion_contours.geojson") as json_data:
    regions_data = json.load(json_data)

# Import data from datasets

df_disasters = pd.read_csv("data/input-magnitude.csv", decimal=".").rename(
    {"DO": "Number of Occurrences"}, axis=1
)
df_extra = pd.read_csv("data/input-extra.csv", decimal=".")

# Preparation of global variables

dict_dataset_labels = {
    "UN_Geosheme_Subregion": "UN Subregion",
    "Disaster_Type": "Type of Disaster",
    "RCP": "Climate Prospective Scenario",
    "Financial_Impact": "Total Cost ($US)",
    "Human_Impact": "Affected People",
    "Number of Occurrences": "Nb of events",
    "°C": "Average temperature (°C)",
    "Rain": "Rainfall",
}
list_disasters = df_disasters["Disaster_Type"].unique()
list_features = ["Number of Occurrences", "Financial Impact", "Human Impact"]
list_rcp = df_disasters["RCP"].unique()
YEARS = list(df_disasters.Decade.drop_duplicates())
dict_dataset_aggregation_method = {
    "Financial_Impact": "sum",
    "Human_Impact": "sum",
    "Number of Occurrences": "sum",
    "°C": "mean",
    "Rain": "mean",
}
dict_magnitude_types = {
    "Number of Occurrences": "Number of Occurrences",
    "Financial Impact": "Financial_Impact",
    "Human Impact": "Human_Impact",
}

# Preparation of main dataframes

# Sorting values and filling the empties
df_disasters = df_disasters.sort_values(by=["UN_Geosheme_Subregion"])
df_disasters["RCP"].fillna(value=0, inplace=True)
df_extra = df_extra.sort_values(by=["UN_Geosheme_Subregion"])
df_extra["RCP"].fillna(value=0, inplace=True)

# Mapbox credentials

mapbox_access_token = "pk.eyJ1IjoibWFoZGlrYXJhYmliZW4iLCJhIjoiY2tmeWlnZzJqMXhyMzJ0czgzcWc3ejViNyJ9.MsvguTk0F7cxDBaV1Zlm_g"
mapbox_style = "mapbox://styles/mahdikarabiben/ckgzi4dac1jez19qlanqcpp5l"

# Choropleth color settings to display features on the map
dict_feature_colors = {
    "Droughts": "YlOrRd",
    "Storms": "RdPu",
    "Floods": "Blues",
}


# ~~~~~~~~~~~~~~~~~~~
#      FUNCTIONS
# ~~~~~~~~~~~~~~~~~~~


# Build the choropleth map from data in dataframe and regional contours in geojson


def choropleth_map(df, impact, colordisaster):
    return go.Figure(
        px.choropleth_mapbox(
            data_frame=df,
            geojson=regions_data,
            locations="UN_Geosheme_Subregion",
            featureidkey="properties.subregion",
            color=impact,
            color_continuous_scale=colordisaster,
            mapbox_style=mapbox_style,
            opacity=0.8,
            center={"lat": 10.190, "lon": 64.709},
            zoom=1.15,
            hover_name="UN_Geosheme_Subregion",
            labels=dict_dataset_labels,
            # range_color=[0, 6500]
        )
    )


# Display the map


def display_map(df, impact, colordisaster):
    fig = choropleth_map(df, impact, colordisaster)

    # Specify layout information
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0}, mapbox_accesstoken=mapbox_access_token
    ),
    fig.update_layout(
        coloraxis=dict(
            colorbar_x=0,
            colorbar_xanchor="left",
            colorbar_y=0.25,
            colorbar_len=0.5,
            colorbar_bordercolor="#ffffff"
            # colorbar_thickness=20
        )
    ),
    fig.update_coloraxes(colorbar_bgcolor="white")

    return fig


def slice_data_on_decades(df_source, rcp_type, decade_start, decade_end):
    """
    Return the slice of the dataframe, on selected decades only
    """
    df = pd.concat(
        [
            df_source[  # historical data
                (df_source["Decade"] >= decade_start)
                & (df_source["Decade"] <= min(decade_end, 2010))
                & (df_source["RCP"] == 0)
            ],
            df_source[  # predicted data, selected on one of the RCP's scenario
                (df_source["Decade"] >= max(2020, decade_start))
                & (df_source["Decade"] <= decade_end)
                & (df_source["RCP"] == rcp_type)
            ],
        ],
        axis=0,
    )
    return df


# ~~~~~~~~~~~~~~~~~~~
#    HTML BLOCKS
# ~~~~~~~~~~~~~~~~~~~

# Title & Logo
def Title_App():
    return html.Div(
        # className="pretty_container-3",
        children=[
            #            html.Img(id="logo", src=app.get_asset_url("WorldBank_Logo@2x.png")),
            html.Img(id="logo", src=app.get_asset_url("logo.png")),
            html.Br(),
            dcc.Markdown(
                """
        ### Natural Disasters Map
        """
            ),
        ],
    )


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
                options=[{"label": i, "value": i} for i in list_disasters],
                value="Floods",
                labelStyle={  # "display": "inline-block",
                    "margin-top": "0px",
                    "font-size": "16px",
                    "padding": "12px 12px 12px 0px",
                },
                labelClassName="data-group-labels",
            ),
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
                options=[{"label": i, "value": i} for i in list_features],
                value="Number of Occurrences",
                labelStyle={  # "display": "inline-block",
                    "margin-top": "0px",
                    "font-size": "16px",
                    "padding": "12px 12px 12px 0px",
                },
                labelClassName="data-group-labels",
            ),
        ]
    )


# RCP selector


def climate_scenario():
    return html.Div(
        children=[
            html.H5(dcc.Markdown("**Select* a RCP**")),
            html.H6(dcc.Markdown("*Only effective from 2020")),
            html.Br(),
            dcc.Slider(
                id="scenario-slider",
                min=0,
                max=10,
                value=2.6,  # default value
                step=None,
                # marks={2.6: "2.6°C", 4.5: "4.5°C", 6.0: "6.0°C",8.5:"8.5°C"},
                marks={
                    # 0: {'label': '0', 'style': {'color': '#77b0b1'}},
                    2.6: {"label": "2.6", "style": {"color": "#77b0b1"}},
                    4.5: {"label": "4.5"},
                    6: {"label": "6.0"},
                    8.5: {"label": "8.5", "style": {"color": "#f50"}},
                },
                disabled=False,
            ),
        ]
    )


# ~~~~~~~~~~~~~~~~~~~
#  STACK BAR GRAPHS
# ~~~~~~~~~~~~~~~~~~~

colors = {"background": "#111111", "text": "#7FDBFF"}

# Add sidebar
SIDEBAR_STYLE = {
    # "position": "fixed",
    "top": 0,
    "left": 0,
    "width": "30vw",
    "overflow": "scroll",
    "maxHeight": "100rem",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "30rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    className="pretty_container-3",
    children=[
        html.Div(dcc.Graph(id="bc_DOHI", config={"displayModeBar": False}),),
        html.Div(
            dcc.Graph(id="bc_ImpactDisasterType", config={"displayModeBar": False}),
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

# Add collapses
collapses = html.Div(
    # className="pretty_container-3",
    # children=
    [dbc.Collapse(sidebar, id="collapse",),]
)

# ~~~~~~~~~~~~~~~~~~~
#  MAIN HTML LAYOUT
# ~~~~~~~~~~~~~~~~~~~

# Layout

app.layout = html.Div(
    id="root",
    children=[
        html.P(
            className="warning",
            children=dbc.Alert(
                "WARNING : Work in progress, prediction is not accurate to take any decision !",
                color="info",
            ),
        ),
        html.Div(
            id="app-container",
            children=[
                html.Div(
                    id="Rectangle_Menu",
                    className="pretty_container-3",
                    children=[
                        html.Div(
                            # className="pretty-container-3",
                            children=[Title_App()]
                        ),
                        html.Br(),
                        html.Div(
                            # className="pretty_container-3",
                            children=[disaster_type_card()]
                        ),
                        html.Br(),
                        html.Div(
                            # className="pretty_container-3",
                            children=[magnitude_type_card()]
                        ),
                        html.Br(),
                        html.Div(
                            # className="pretty_container-3",
                            children=[climate_scenario()]
                        ),
                        html.Br(),
                        html.Div(
                            children=[
                                html.Button(
                                    "Display Charts",
                                    id="collapse-button",
                                    style={"display": "block"},
                                ),
                                html.Button(
                                    "Hidden Charts",
                                    id="collapse-button2",
                                    style={"display": "None"},
                                ),
                            ]
                        ),
                    ],
                ),
                html.Div(collapses),
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
                                    value=[1960, 2010],
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
                                        df_disasters[
                                            (df_disasters["Decade"] >= 1900)
                                            & (df_disasters["Decade"] <= 1920)
                                            & (
                                                df_disasters["Disaster_Type"]
                                                == "Floods"
                                            )
                                            & (df_disasters["RCP"] == 2.6)
                                        ],
                                        "Human_Impact",
                                        "reds",
                                    ),
                                    config={
                                        "modeBarButtonsToRemove": [
                                            "toImage",
                                            "toggleSpikelines",
                                            "pan2d",
                                            "select2d",
                                            "lasso2d",
                                            "hoverClosestCartesian",
                                        ]
                                    },
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)


# ~~~~~~~~~~~~~~~~~~~
#      CALLBACKS
# ~~~~~~~~~~~~~~~~~~~
# TO UPDATE THE DASHBOARD BASED ON USER ACTIONS

# Update charts
@app.callback(
    Output("bc_DOHI", "figure"),
    Output("bc_ImpactDisasterType", "figure"),
    [
        Input("county-choropleth", "clickData"),
        Input("years-slider", "value"),
        Input("Disaster-Selector", "value"),
        Input("scenario-slider", "value"),
        Input("Magnitude-Selector", "value"),
    ],
)
def update_bar_chart(map_input, years, disaster, scenario, impact):
    if map_input:
        location = map_input.get("points")[0].get("location")
    else:
        location = ""  # No selected region so display worldwide figures

    # Select decades and RCP
    df = slice_data_on_decades(df_disasters, scenario, years[0], years[1])
    df_temperatures = slice_data_on_decades(
        df_extra[["Decade", "UN_Geosheme_Subregion", "RCP", "°C"]],
        scenario,
        years[0],
        years[1],
    )

    # Prepare data to display
    df_figs = df.copy()

    # Map the text of selected impact with the label of the corresponding dataframe column
    impact_type = dict_magnitude_types[impact]
    # Number of bars
    bins = int((int(years[1]) - int(years[0])) / 10)

    # In case we want to force all colors:
    # color_codes= ['#CCFFFF','#CCCCFF','#CC99FF','#009999','#0033FF','#003333',
    # '#9900CC','#FFFF33','#339966','#CC6666','#996633','#009900','#6666FF','#330033',
    # '#FF3333','#FFCCFF','#33FF99','#33FF99','#9999FF','#CC3300','#3300CC','#9999FF']
    # color={}
    # for i in range(21):
    #    color[i] = color_codes[i]

    # Chart 1: Region X Disaster X Magnitude VS Temperatures
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Prepare data
    df_chart1 = df_figs.copy()
    # Keep only occurrences
    # df_chart1.drop(columns=['Financial_Impact','Human_Impact'], inplace=True)
    # Region selection
    if location:
        to_drop = df_chart1[~(df_chart1["UN_Geosheme_Subregion"] == location)].index
        df_chart1.drop(to_drop, inplace=True)
    # Disaster selection
    to_drop = df_chart1[~(df_chart1["Disaster_Type"] == disaster)].index
    df_chart1.drop(to_drop, inplace=True)
    # Compute temperatures
    if location:  # Get temperatures for the selected region only
        df_temp_to_merge = df_temperatures[
            df_temperatures["UN_Geosheme_Subregion"] == location
        ]
    else:  # Compute the world mean of temperatures by decade (beware that no weighting with region area has been done)
        df_temp_to_merge = (
            df_temperatures.groupby(["Decade"])["°C"].mean().reset_index()
        )
    df_chart1.loc[:, "Temperature"] = df_chart1.Decade.map(
        df_temp_to_merge.set_index("Decade")["°C"]
    )

    # Sorting and reordering
    df_chart1 = df_chart1.sort_values(by=["Decade"])

    # Make figure
    subfig1 = make_subplots(specs=[[{"secondary_y": True}]])
    fig2 = px.histogram(
        df_chart1,
        x="Decade",
        y=impact_type,
        template="plotly",
        color="Disaster_Type",
        color_discrete_map={
            "Floods": "#C5EBFD",
            "Storms": "#B561F4",
            "Droughts": "#FFAE5D",
        },
        nbins=bins,
    )

    fig3 = px.line(
        df_chart1, x="Decade", y="Temperature", labels={"°C": "Average Temperature"}
    )
    fig3.update_traces(
        yaxis="y2", showlegend=True, name="Temperatures", line_color="black"
    )

    subfig1.add_traces(fig2.data + fig3.data)
    subfig1.layout.title = "<b>{0}</b>: {1} {2} vs °C".format(
        (location if location else "World"), disaster, impact
    )
    subfig1.update_xaxes(type="category")
    subfig1.layout.xaxis.title = "Decades"
    subfig1.layout.yaxis.title = "{0}".format(impact)
    subfig1.layout.yaxis2.title = "Average Temperatures"
    subfig1.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    # Chart 2: World X Magnitude VS Temperatures
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Prepare data
    df_chart2 = df_figs[
        ["Decade", "UN_Geosheme_Subregion", "Disaster_Type", impact_type]
    ].copy()
    df_chart2 = df_chart2.groupby(["Decade", "Disaster_Type"]).sum().reset_index()
    # Compute the world mean of temperatures by decade (beware that no weighting with region area has been done)
    df_temp_to_merge = df_temperatures.groupby(["Decade"])["°C"].mean().reset_index()
    df_chart2.loc[:, "Temperature"] = df_chart2.Decade.map(
        df_temp_to_merge.set_index("Decade")["°C"]
    )

    # Make figure
    subfig2 = make_subplots(specs=[[{"secondary_y": True}]])
    fig4 = px.histogram(
        df_chart2,
        x="Decade",
        y=impact_type,
        template="plotly",
        color="Disaster_Type",
        color_discrete_map={
            "Floods": "#C5EBFD",
            "Storms": "#B561F4",
            "Droughts": "#FFAE5D",
        },
        nbins=bins,
    )

    fig5 = px.line(
        df_chart2, x="Decade", y="Temperature", labels={"°C": "Average Temperature"}
    )
    fig5.update_traces(
        yaxis="y2", showlegend=True, name="Temperatures", line_color="black"
    )

    subfig2.update_layout(
        barmode="stack", xaxis={"categoryorder": "category ascending"}
    )
    subfig2.add_traces(fig4.data + fig5.data)
    subfig2.layout.title = "<b>World</b>: {0} per Disaster Type vs °C".format(impact)
    subfig2.update_xaxes(type="category")
    subfig2.layout.xaxis.title = "Decades"
    subfig2.layout.yaxis.title = "{0}".format(impact)
    subfig2.layout.yaxis2.title = "Average Temperatures"
    subfig2.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    return subfig1, subfig2


# Update map title according to selected decades
@app.callback(Output("heatmap-title", "children"), [Input("years-slider", "value")])
def update_map_title(year):
    return "Choropleth map from the beginning of the {0}s to the end of the {1}s".format(
        year[0], year[1]
    )


# Update the data selection sent to the map - period, magnitude, impact
@app.callback(
    Output("county-choropleth", "figure"),
    Input("years-slider", "value"),
    Input("Disaster-Selector", "value"),
    Input("Magnitude-Selector", "value"),
    Input("scenario-slider", "value"),
)
def update_map(year, DisasterType, MagnitudeType, RcpType):
    """
    Update the map according to the parameters selected by the user
    """

    # Selection of the slice of decades to keep
    df = slice_data_on_decades(df_disasters, RcpType, year[0], year[1]).copy()
    # Selection of the disaster to keep
    to_drop = df[~(df["Disaster_Type"] == DisasterType)].index
    df.drop(to_drop, inplace=True)

    # Get the color scale settings to display the choropleth
    color = dict_feature_colors[DisasterType]

    # Select the feature in the dataset
    magnitude_type = dict_magnitude_types[MagnitudeType]

    # Select the feature and aggregate its data on the selected decades
    if dict_dataset_aggregation_method[magnitude_type] == "sum":
        df = df.groupby(["UN_Geosheme_Subregion"])[magnitude_type].sum().reset_index()
    elif dict_dataset_aggregation_method[magnitude_type] == "mean":
        df = df.groupby(["UN_Geosheme_Subregion"])[magnitude_type].mean().reset_index()

    return display_map(df, magnitude_type, color)


# Display left side panel when clicking on button
@app.callback(
    Output("collapse", "style"),
    Output("right-column", "style"),
    Output("collapse-button", "style"),
    Output("collapse-button2", "style"),
    [Input("collapse-button", "n_clicks")],
    [Input("collapse-button2", "n_clicks")],
    [State("right-column", "style")],
    [State("collapse", "style")],
    [State("collapse-button", "style")],
    [State("collapse-button2", "style")],
)
def callback(n_clicks, nh_clicks, style_map, style, btn1, btn2):
    if style is None or "display" not in style:
        style = {"display": "none"}
        style_map = {"width": "66vw"}
        btn1 = {"display": "block"}
        btn2 = {"display": "none"}
    else:
        if style["display"] == "none":
            style["display"] = "block"
            style_map["width"] = "33vw"
            btn1["display"] = "none"
            btn2["display"] = "block"
        else:
            style["display"] = "none"
            style_map["width"] = "66vw"
            btn1["display"] = "block"
            btn2["display"] = "none"

    return style, style_map, btn1, btn2


# ~~~~~~~~~~~~~~~~~~~
#        MAIN
# ~~~~~~~~~~~~~~~~~~~
# when file executed as a standalone application

if __name__ == "__main__":
    app.run_server(debug=True, host="127.0.0.1", port=8050)

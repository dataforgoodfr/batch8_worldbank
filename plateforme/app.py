### Lib required for dashboard ### 
import pandas as pd 
import plotly.express as px
import requests
import plotly.graph_objects as go 
import dash
import dash_html_components as html
import dash_core_components as dcc


# Initialize app
external_stylesheets = ['assets/style.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Load data
dataset= pd.read_csv("data/DataForGood2020_updated.csv")
YEARS = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]


# Fonction card 
def DisasterType_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return dcc.Dropdown(
                          id='description',
                          options=[
                                     {'label': 'Drought', 'value': 'Drought'},
                                     {'label': 'Flood', 'value': 'Flood'},
                                     {'label': 'Storm', 'value': 'Storm'}
                                  ],
                          value='Drought'
                        )
           
def Region_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return dcc.Checklist(
                             options=[
                                       {'label': 'Asia', 'value': 'Asia'},
                                       {'label': 'Europe', 'value': 'Europe'},
                                       {'label': 'Middle East', 'value': 'Middle East'},
                                       {'label': 'North America', 'value': 'North America'},
                                       {'label': 'South America', 'value': 'South America'}
                                    ],
                            value=['Asia', 'Europe']
                          )                 
                                                     

# App layout
app.layout = html.Div(
                        id="root",
                        children=[
                                    html.Div(
                                        id="header",
                                        children=[html.Img(id="logo",src=app.get_asset_url("WB_logo.jpg"))
                                                  ],
                                    ),
                                    
                                    html.Div(
                                              id='app-container',
                                              className="row twelve columns",
                                              children=[
                                                        html.Div(
                                                                    id="left-column",
                                                                    children=[
                                                                    DisasterType_card(),
                                                                    Region_card()
                                                                    ]
                                                                 ),
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
                                                                    
                                                                    children=[
                                                                        html.P(
                                                                                children="MAP",
                                                                        ),
                                                                        
                                                                    ],
                                                                ),
                                                        ]

                                                
                                                         
                                    )

                                     
                                  #  html.Div(
                                  #              id="left-column",
                                  #              children=[html.H1('MAP')]
                                  #  ),
                                  #  html.Div(id='right-column',children=['test'])



                        ]  
             )
             
                    


        


if __name__ == '__main__':
    app.run_server()



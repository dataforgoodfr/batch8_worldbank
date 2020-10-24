### Lib required for dashboard ### 
import pandas as pd 
import plotly.express as px
import requests
import plotly.graph_objects as go 
import dash
import dash_html_components as html
import dash_core_components as dcc


# Initialize app
external_stylesheets =['assets/style.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Load data
dataset= pd.read_csv("data/DataForGood2020_updated.csv")
dataset.head()
YEARS = [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]


# Fonction card 
def DisasterType_card():
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
           
def Region_card():
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

def Repartition_cart():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return dcc.Graph(
                        id='example-graph',
                        figure={
                            'data': [
                                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Flood'},
                                #{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Storm'},
                                #{'x': [1, 2, 3], 'y': [6, 7, 8], 'type': 'bar', 'name': u'Drought'},
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
                                          className="header",
                                          children=[
                                                     html.Div(className='leftcolumn',
                                                              children=[
                                                                          html.Img(id="logo",src=app.get_asset_url("WB_logo.jpg"))
                                                                          
                                                                        ]
                                                             ),
                                                      html.Div(className='leftcolumn',
                                                              children=[
                                                                        html.H2('WORLD')
                                                                        ]
                                                             ),
                                                      html.Div(
                                                                    #id="slider-container",
                                                                    className='rightcolumn',
                                                                    children=[
                                                                        html.P(
                                                                            #id="slider-text",
                                                                            children="Drag the slider to change the year:",
                                                                        ),
                                                                        dcc.Slider(
                                                                            #id="years-slider",
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
                                                    ] 

                                          ),

                                 html.Div(className="row",
                                          children=[html.Div(className='leftcolumn',
                                                             children=[
                                                                            html.Div(className='card',
                                                                                    children=[
                                                                                                DisasterType_card(),
                                                                                                html.Br(),
                                                                                                html.Br(),
                                                                                                Region_card()
                                                                                             ]
                                                                            
                                                                            
                                                                                    ),
                                                                      ]
                                                                        
                                                            ),
                                                    html.Div(className='leftcolumn',
                                                             children=[
                                                                            
                                                                        html.Div(className='card',
                                                                                 children=[
                                                                                                
                                                                                                Repartition_cart(),
                                                                                                html.Br(),
                                                                                                html.Br(),
                                                                                                
                                                                                            ]
                                                                            
                                                                            
                                                                                ),
                                                                      ]
                                                                        
                                                            ),
                                                    #Map     
                                                    html.Div(className='rightcolumn',
                                                             children=[html.Div(className='card',
                                                                                children=[html.H2('MAP'),
                                                                                                
                                                                                          html.Div(className='fakeimg',
                                                                                                   children=['Map']
                                                                                                
                                                                                                ),
                                                                                            
                                                                                        ]
                                                                            
                                                                                    ),
                                                                 ]
                                                        ), 
                                                     ]
                                         )



                                ]
                )
if __name__ == '__main__':
    app.run_server()



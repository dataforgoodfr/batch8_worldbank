import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots

df = pd.read_csv("../data/input-magnitude.csv", decimal=".")
dfe = pd.read_csv("../data/input-extra.csv", decimal=".")
disaster = df["Disaster_Type"].unique()
YEARS = df["Decade"].unique()

external_stylesheets = ['https://codepen.io/anon/pen/mardKv.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in disaster],
        value=disaster[0],
        clearable=False,
        style={'backgroundColor': 'black'}
    ),
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
                value=[1900, 1950],
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
        ],
    ),
    html.Br(),
    html.Div(
        dcc.Graph(id="histogram"),
    ),
    html.Div(
        dcc.Graph(id="bc_DOHI"),
    ),
    html.Div(
        dcc.Graph(id="bc_ImpactDisasterType"),
    ),
])


@app.callback(
    Output("histogram", "figure"),
    Output("bc_DOHI", "figure"),
    Output("bc_ImpactDisasterType", "figure"),
    Input("dropdown", "value"),
    Input("years-slider", "value"),
    Input("Impact-Selector", "value")
)
def update_charts(disaster, year, ImpactType):
    c = dfe.groupby(['Decade'])['°C'].mean().reset_index()
    df['Temperature'] = df.Decade.map(c.set_index('Decade')['°C'])
    is_disaster = df["Disaster_Type"] == disaster
    df_disaster = df[is_disaster]
    if not ImpactType:
        # color = "reds"
        impact_type = 'Human_Impact'
    else:
        # color = "purples"
        impact_type = 'Financial_Impact'
    # Si on veut définir toutes les couleurs une par une nous même:
    # color_codes= ['#CCFFFF','#CCCCFF','#CC99FF','#009999','#0033FF','#003333',
    # '#9900CC','#FFFF33','#339966','#CC6666','#996633','#009900','#6666FF','#330033',
    # '#FF3333','#FFCCFF','#33FF99','#33FF99','#9999FF','#CC3300','#3300CC','#9999FF']
    # color={}
    # for i in range(21):
    #    color[i] = color_codes[i]
    df_fig = df_disaster.query('Decade >=@year[0] and Decade <@year[1]')
    bins = int((int(year[1]) - int(year[0])) / 10)
    fig = px.histogram(df_fig,
                       x="Decade",
                       y=impact_type,
                       color="UN_Geosheme_Subregion",
                       # color_discrete_sequence = color,
                       template='plotly',
                       nbins=bins,
                       # barmode="stack",
                       title='Evolution of {0} caused by {1} per Regions'.format(impact_type, disaster),
                       # animation_frame="Decade",
                       labels={'x': 'Decade', 'y': 'Total Financial Impact', 'color': 'Region'},
                       )
    # fig.update_xaxes(type='category')
    fig.update_layout(xaxis={'categoryorder': 'total descending'})

    subfig = make_subplots(specs=[[{"secondary_y": True}]])
    fig2 = px.histogram(df_fig,
                        x="Decade",
                        y="DO",
                        template='plotly',
                        # barmode="stack",
                        color_discrete_sequence={0: '#CC0000'},
                        nbins=bins,
                        title='Evolution of disaster occurence and human impact worldwide',
                        # animation_frame="Decade", #ne autoscale pas malheureusement
                        labels={'Decade': 'Decade', 'DO': 'Disaster Occurence'},
                        )
    fig2.update_xaxes(type='category')

    fig3 = px.line(df_fig, x="Decade", y="Temperature", labels={'°C': 'Average Temperature'})
    fig3.update_traces(yaxis="y2", showlegend=True, name='Temperatures', line_color='black')

    subfig.add_traces(fig2.data + fig3.data)
    subfig.update_xaxes(type='category')
    subfig.layout.xaxis.title = "Decades"
    subfig.layout.yaxis.title = "Occurences"
    subfig.layout.yaxis2.title = "Temperatures"
    subfig.layout.title = "{0} Occurence vs Temperature".format(disaster)

    fig4 = px.histogram(df.query('Decade >=@year[0] and Decade <@year[1]'),
                        x="Decade",
                        y=impact_type,
                        color="Disaster_Type",
                        color_discrete_sequence={0: '#FFAE5D', 1: '#C5EBFD', 2: '#B561F4'},
                        template='plotly',
                        nbins=bins,
                        title='Total {0} per Disaster Type'.format(impact_type),
                        # animation_frame="Decade",
                        labels={'x': 'Decade', 'y': 'Total Financial Impact', 'color': 'Disaster Type'},
                        )
    fig4.update_xaxes(type='category')

    return fig, subfig, fig4


if __name__ == '__main__':
    app.run_server(debug=True, host="127.0.0.1", port=8050)

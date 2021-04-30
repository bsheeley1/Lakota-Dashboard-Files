#ask me if you have any questions about this code, there is a test file with data from a youtube video 
#if you want to see this template filled out

import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ---------- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("")

df = df.groupby([''])[['']].mean()
df.reset_index(inplace=True)
print(df[:5])

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "", "value": },
                     {"label": "", "value": },
                     {"label": "", "value": },
                     {"label": "", "value": }],
                 multi=False,
                 value=,
                 style={'width': ""}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='', figure={})

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    dff = dff[dff[""] == ""]

    # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locationmode='USA-states',
        locations='state_code',
        scope="",
        color='',
        hover_data=['', ''],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'': ''},
        template='plotly_dark'
    )

    # Plotly Graph Objects (GO)
    fig = go.Figure(
         data=[go.Choropleth(
             locationmode='USA-states',
             locations=dff['state_code'],
             z=dff[""].astype(float),
             colorscale='Reds',
         )]
     )
    
    fig.update_layout(
         title_text="COVID 19 Dashboard",
         title_xanchor="center",
         title_font=dict(size=24),
         title_x=0.5,
         geo=dict(scope=''),
     )

    return container, fig
###this return here returns the output component not the final return

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
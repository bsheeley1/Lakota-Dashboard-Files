# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:29:21 2020

@author: Jharp
"""

#Modules and Libraries

#Dash Modules for Dashboard in Browser
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import COVID_READER as CV

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import datetime
import plotly.express as px
import pandas as pd
import lidar
#Matplotlib for plotting graphs and charts
#Numpy for mathematical operations
#Datetime for date formatting
file = 'C:/Users/bbshe/OneDrive - purdue.edu/Desktop/School/School Work/Spring 2021/EPICS121/prot 4/Data/Copy of USGS_LPC_SD_NRCS_Fugro_B2_2017_13TFK240260_LAS_2019.laz'
lidar.myFunc(file)

#------------------------------------------------------------------------------
#define colors
colors = {
    'backstage': 'rgb(150,15,35)',
    'background': 'rgb(203,213,222)',
    # 'text': '#999999',
    'text': 'rgb(0,0,0)',
    # 'text': 'rgb(0,0,255)',
    # 'text': '#d62728'
}

#------------------------------------------------------------------------------
#Covid lists:
     
x_dates_confirmed,y_amount_confirmed,x_dates_deaths,y_amount_deaths,dates,confirmed_percentage,death_percentage,confirmed_cases,death_toll = CV.main()



#------------------------------------------------------------------------------


#Declare the dashboard app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash("Covid Dashboard", external_stylesheets=external_stylesheets)



#------------------------------------------------------------------------------
#Covid figure structure
df6 = pd.DataFrame({
        "Dates_confirmed": x_dates_confirmed,
        "Cases": y_amount_confirmed,
})
fig6 = px.line(df6,x="Dates_confirmed", y="Cases", title = "New Known Cases per day")

fig6.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )
    
df5 = pd.DataFrame({
        "Dates_deaths": x_dates_deaths,
        "Amount_deaths": y_amount_deaths,
})
fig5 = px.line(df5, x="Dates_deaths", y="Amount_deaths", title = "New Known Deaths per day")

fig5.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )
df4 = pd.DataFrame({
        "Dates": dates,
        "Confirmed_Percentage": confirmed_percentage,
})
fig4 = px.line(df4,x="Dates", y="Confirmed_Percentage", title = "Confirmed Cases % by Total Population")

fig4.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )
df3 = pd.DataFrame({
        "Dates": dates,
        "Death_Percentage": death_percentage,
})
fig3 = px.line(df3, x="Dates", y="Death_Percentage", title = "Death % by Total Population")

fig3.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )
df2 = pd.DataFrame({
        "Dates": dates,
        "Confirmed_Cases": confirmed_cases,
})
fig2 = px.line(df2, x="Dates", y="Confirmed_Cases", title = "Cumulative Confirmed Cases in Oglala Lakota County")
 
fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )
df1 = pd.DataFrame({
        "Dates": dates,
        "Death_Toll": death_toll,
})
fig1 = px.line(df1, x="Dates", y="Death_Toll", title = "Cumulative Death Count in Oglala Lakota County")

fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )

#------------------------------------------------------------------------------






tab_style = {
    'borderBottom': '1px dashed rgb(255,255,255)',
    'backgroundColor': 'rgb(0,0,0)',
    'padding': '6px',
    'fontWeight': 'bold',
    'color': 'white',
}

tab_selected_style = {
    'borderTop': '3px solid rgb(255,255,255)',
    # 'borderBottom': '2px dash rgb(255,255,255)',
    'backgroundColor': 'rgb(200,200,200)',
    'color': 'black',
    'padding': '6px'
}

#------------------------------------------------------------------------------



#Create the layout, declare how many tabs will be used
#One tab per each plot, with its identifying name
app.layout = html.Div(style={'backgroundColor': colors['backstage']}, children = [
    dcc.Tabs(id='tabs', value='tab-1', children=[
         dcc.Tab(label='Cumulative Death Count in Oglala Lakota County', value='tab-1',style=tab_style, selected_style = tab_selected_style),
         dcc.Tab(label='Cumulative Confirmed Cases in Oglala Lakota County', value='tab-2',style=tab_style, selected_style = tab_selected_style),
         dcc.Tab(label = 'Map', value= 'tab-3', style =tab_style , selected_style = tab_selected_style),
         ]),
    html.Div(id='tab-content')
])

#App callback is used to alternate between tabs and populate each one with a plot
@app.callback(Output('tab-content', 'children'),
              [Input('tabs', 'value')])

def TabsFunction(tab):
    if tab == 'tab-1': #tab 1 layout
        return html.Div([
          html.Div([
            html.H1(children='COVID Dashboard'), #tab 1 header string
      dcc.Graph(
          id='example',
          figure = fig6
          )
      ], className = 'row'),
    
          html.Details([
            html.H1(children='COVID Dashboard'), #tab 1 header string  
        
      dcc.Graph(
          id='graph2',
          figure = fig2
          ),
      dcc.Graph(
          id='graph2',
          figure = fig4
          ),
      ], className = 'row'),
    ]),
  
    elif tab == 'tab-2' : 
        return html.Div([
            html.H1(children='COVID Dashboard'), #tab 2 header string
    dcc.Graph(
        id='graph2',
        figure = fig5
        )
    ])
    elif tab == 'tab-3':
        return html.Div([
            html.Img(src=app.get_asset_url('Test.png'))
    ])
        
    
#Main function, here we call the dashboard app to run on server
#Please check the console for the printout of the server location
if __name__ == '__main__':
    app.run_server(debug=False)

        

            
# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px


# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
             ### Can you predict which water pumps are faulty?
             Using data from Taarifa and the Tanzanian Ministry of Water, can you predict which pumps are functional, which need some repairs, and which don't work at all? 
             Predict one of these three classes based on a number of variables about what kind of pump is operating, when it was installed, and how it is managed. 
             *A smart understanding of which waterpoints will fail can improve maintenance operations and ensure that clean, potable water is available to 
             communities across Tanzania.*
             
            """
        ),
        dcc.Link(dbc.Button('Predict your pumps status', color='primary'), href='/predictions')
    ],
    md=3,
)


train = pd.read_csv('./notebooks/train.csv')
fig1 = px.pie(train, values='population', names='status_group', title='Population around different waterpumps')
fig2 = px.scatter(train, x="longitude", y="latitude", color="status_group", opacity=0.4)


column2 = dbc.Col([
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2)])


layout = dbc.Row([column1, column2])
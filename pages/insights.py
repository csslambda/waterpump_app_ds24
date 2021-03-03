# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
import pandas as pd
import plotly.express as px

train = pd.read_csv('./notebooks/train.csv')
fig1 = px.scatter(train, x="construction_year", y="population", color="status_group")
fig2 = px.bar(train, x="water_quality", y="amount_tsh", color="status_group")
# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Insights
            """
        ),
        dcc.Graph(
            figure=fig1),
        dcc.Markdown(
            """
            """
        ),
        dcc.Graph(
            figure=fig2)

    ],
)

layout = dbc.Row([column1])
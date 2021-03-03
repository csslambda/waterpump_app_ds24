# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Process
            ##### Can you predict which water pumps are faulty?

            Using data from Taarifa and the Tanzanian Ministry of Water, can you predict which pumps are functional, 
            which need some repairs, and which don't work at all? This is an intermediate-level practice competition. 
            Predict one of these three classes based on a number of variables about what kind of pump is operating, 
            when it was installed, and how it is managed. A smart understanding of which waterpoints will fail can improve 
            maintenance operations and ensure that clean, potable water is available to communities across Tanzania.



            """
        ),

    ],
)

layout = dbc.Row([column1])
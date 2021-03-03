# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
from joblib import load
import pandas as pd
pipeline = load('notebooks/pipeline.joblib')


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

quantity_value_list = ['insufficient', 'enough', 'dry', 'seasonal', 'unknown']
water_point_type_list = ['communal standpipe', 'hand pump', 'other', 'communal standpipe multiple', 'improved spring', 'cattle trough', 'dam']
extraction_type_class_list = ['gravity', 'handpump', 'other', 'motorpump', 'submersible', 'rope pump', 'wind-powered']

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Choose the parameters for your pump

            """
        ),
        dcc.Markdown(
            """
            ##### amount_tsh
            """),
        dcc.Slider(
            id='amount_tsh_slider_input',
            min=0,
            max=350000,
            marks={i*50000:'{}k'.format(i*5) for i in range(0, 8)},
            value=0,
            className='mb-2'
            ),
        dcc.Markdown('', id='my-output-amount'),
        dcc.Markdown(
            """
            ##### latitidue
            """),
        dcc.Slider(
            id='longitude_slider_input',
            min=29.607122,
            max=40.344301,
            step=0.5,
            marks={i: '{}'.format(i) for i in range(28, 42)},
            value=29.607122,
            className='mb-2'),
        dcc.Markdown('', id='my-output-longitude'), 
        dcc.Markdown(
            """
            ##### quantity
            """),
        dcc.Dropdown(
            id='quantity_input',
            options=[
                {'label': i, 'value': i} for i in quantity_value_list
                ],
                value='insufficient',
                className='mb-4'),
        dcc.Markdown(
            """
            ##### water_point
            """),
        dcc.Dropdown(
            id='water_point_input',
            options=[
                {'label': i, 'value': i} for i in water_point_type_list
                ],
                value='hand pump',
                className='mb-4'),
        dcc.Markdown(
            """
            ##### extraction_type_class_ 
            """),
        dcc.Dropdown(
            id='extraction_type_class_input',
            options=[
                {'label': i, 'value': i} for i in extraction_type_class_list 
                ],
                value='gravity',
                className='mb-4'),
        dcc.Markdown('',id='prediction-content', style={
        'textAlign': 'center',
        'font-size':30})
            ])

# https://dash.plotly.com/dash-core-components


@app.callback(
    Output(component_id='my-output-amount', component_property='children'),
    [Input(component_id='amount_tsh_slider_input', component_property='value')]
)
def update_output_div(input_value):
    return 'The amount_tsh is {}'.format(input_value)

@app.callback(
    Output(component_id='my-output-longitude', component_property='children'),
    [Input(component_id='longitude_slider_input', component_property='value')]
)
def update_output_div(input_value):
    return 'The longitude is {}'.format(input_value)


@app.callback(
    Output('prediction-content','children'),
    [ Input('quantity_input', 'value'),
      Input('amount_tsh_slider_input', 'value'),
      Input('water_point_input', 'value'),
      Input('extraction_type_class_input', 'value'),
      Input('longitude_slider_input', 'value')
     ])

def predict(quantity,amount_tsh,waterpoint_type,extraction_type_class,longitude):
    df = pd.DataFrame(columns=['quantity','amount_tsh','waterpoint_type','extraction_type_class','longitude'], 
    data=[[quantity,amount_tsh,waterpoint_type,extraction_type_class,longitude]])
    y_pred = pipeline.predict(df)[0]
    return "The waterpump is {}!".format(y_pred)

layout = dbc.Row([column1])
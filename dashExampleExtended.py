# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = dash.Dash()
        
app.layout = html.Div(children=[
        
        #Saying hello to everyone
        html.H1('1. Hello Klop'),
        
        html.H2('1.1 Table state'),
        
            dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
        
        #First statistical talbe
        dash_table.DataTable(
        id='datatable',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("rows")
        ),
        
        html.H2('1.2 Exclusions and DQ checks'),
        
        #Example of drop down
        dcc.Dropdown(
        id='ColInput',      
        options = [{'label': i, 'value': i} for i in df.columns],
        value=''
        ),
    
        #Comparison of drop down
        dcc.Dropdown(
        options=[
            {'label': 'Equal to (=)', 'value': 'NYC'},
            {'label': 'Greater than (>)', 'value': 'MTL'},
            {'label': 'Greater than or equal to (>=)', 'value': 'GTET'},
            {'label': 'Less than (<)', 'value': 'SF'},
            {'label': 'Less than or equal to (<=)', 'value': 'LTET'},
            {'label': 'In list', 'value': 'IL'},
            {'label': 'Between (Not including)', 'value': 'BNI'},
            {'label': 'Between (Including)', 'value': 'BI'}
        ],
        value='MTL'
        ),
                
        #Example input with output
        dcc.Input(
        id='inputBox',
        placeholder='Enter a value...',
        type='text',
        value=''
        ),
        
        #Second filtered table
        dash_table.DataTable(
        id='dataTable2',
        columns=[{"name": i, "id": i} for i in df.columns]
        )
        
])
        
@app.callback(
    Output(component_id='dataTable2', component_property='data'),
    [Input(component_id='inputBox', component_property='value'),
     Input(component_id='ColInput', component_property='value')]
)

def update_outputDiv(inputBoxValue,ColInputValue):
    df1 = df[df[ColInputValue] == int(inputBoxValue)]
    data=df1.to_dict("rows")
    return data

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
 
    

    
    
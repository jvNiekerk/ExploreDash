# -*- coding: utf-8 -*-
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)
app = dash.Dash(__name__, server=server, url_base_pathname='https://dashtestdq.azurewebsites.net',external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
        
    #Example of html header     
    html.H1(children='Hello Dash'),

    #Example of low level html row
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    
    #Example of Bar Graph
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization Check'
            }
        }
    ),

    #Example of low level html row
    html.Div(children='''
        Example of a drop down box
    '''),

    #Example of drop down
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
   ),
    
    #Example of low level html row
    html.Div(children='''
        Example of a drop down box - multiple selection
    '''),
    
    #Example of drop down - multiple
    dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    multi=True,
    value="MTL"
),
    
    #Example of low level html row
    html.Div(children='''
        Example of input box
    '''),
     
    dcc.Input(
    placeholder='Enter a value...',
    type='text',
    value=''
),
    
    #Example of low level html row
    html.Div(children='''
        Example of check box
    '''),
             
    dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF']
)
])

@server.route("/dash")
def MyDashApp():
    return app.index()

from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('intro_bees.csv')


app.layout = html.Div([
    
    html.H1("Dashboard using dash  "),
    dcc.P("This is a dropdown with a single choice option"),
    dcc.Dropdown(['Option 1', 'Option 2', 'Option 3']),
    
    html.P("This is a dropdown with multiple choices available"),
    dcc.Dropdown(['Option 1', 'Option 2', 'Option 3'], multi = True)
    ])



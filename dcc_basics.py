from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv('intro_bees.csv')


app.layout = html.Div([
    
    html.H1("Dashboard using dash  "),
    html.P("This is a dropdown with a single choice option"),
    dcc.Dropdown(['Option 1', 'Option 2', 'Option 3'], value = 'Option 1', id='Single Dropdown'),
    
    html.P("This is a dropdown with multiple choices available"),
    dcc.Dropdown(['Option 1', 'Option 2', 'Option 3'], value='Option 2', multi=True, id='Multi Dropdown'),
    
    html.P("This is a slider with a default value"),
    dcc.Slider(min=1, max=10, step=1, value=3, id='Trial Slider'),
    
    html.P("This is an input field"),
    dcc.Input(id='Inputfield', value='eg'),
    
    html.P("This is a checklist"),
    dcc.Checklist(['Checkbox 1', 'Checkbox 2', 'Checkbox 3'], value='Checkbox1'),
    
    html.P("These are Radio items"),
    dcc.RadioItems(['Checkbox 1', 'Checkbox 2', 'Checkbox 3'], value='Checkbox1', inline=False),
    
    html.Br(),
    # Now, on to what might be the most important feature of DCC: Graphs
    # Any Plotly figure can be added as a Graph in a Dashboard.
    
    dcc.Graph(figure = px.scatter(x=[0, 1, 2, 3, 4], 
                                  y=[0, 1, 4, 9, 16]
                                  ))
    ])


if __name__ == '__main__':
    app.run_server(debug= False)
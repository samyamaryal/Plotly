from dash import Dash, html

# Initialize the Dash app using the Dash constructor
app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World')
])

#Used to run the app
if __name__ == '__main__':
    app.run_server(debug= False)
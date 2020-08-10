import numpy as np


import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
from components.plot_histogram import render_histogram
from components.input_boxes import  render_input_boxes

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

input_boxes = render_input_boxes()


app.layout = html.Div([
    html.H1("Plot Normal Distributions"),
    input_boxes,
    dbc.Button("Submit",
               id="submit-button",
               color="primary",
               n_clicks=0,
               style={"margin-left": "20px",
                      "margin-top": "20px",
                      "margin-bottom": "20px"}),
    html.Div(id="histogram-container"),
])


@app.callback(Output("histogram-container", "children"),
              [Input("submit-button", "n_clicks")],
               state=[State("input-mean", "value"),
                      State("input-std", "value")])
def update_histogram(n_clicks, mu, std):
    histogram = render_histogram(mu, std)
    return histogram


if __name__=="__main__":
    app.run_server('localhost', debug=True)
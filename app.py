import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from components.input_group import render_input_group
from components.plot_histogram import render_histogram

external_stylesheets = [dbc.themes.FLATLY]

# create your dash app object
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change the tab title of the app
app.title="HistoGrammies"

server = app.server  # this creates a server from our app.server

# this defines the entire app
# step 1 let's add some input boxes into our app
# things we add to our app are called components
# what type of object is this component?

input_group = render_input_group()
button = dbc.Button("Submit", id="submit-button", color="info", n_clicks=0)

app.layout = html.Div([
    html.H1("Hello World!"),
    input_group,
    button,
    html.Div(id="message-box")
])


# to make this reactive we need to do callbacks
@app.callback(Output(component_id="message-box", component_property="children"), # points to where the return is going to go
              [Input("submit-button", "n_clicks")], # this triggers the callback
              state=[State(component_id="input-mean", component_property="value"), # state grabs specific information from components in the app
                     State(component_id="input-std", component_property="value")])
def render_histogram_component(n_clicks, mu, std):
    histogram = render_histogram(mu, std)
    return histogram


if __name__ == "__main__":
    # this runs the app
    app.run_server('localhost', debug=True)

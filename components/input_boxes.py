import dash_bootstrap_components as dbc
import dash_html_components as html


def render_input_boxes():
    input_group = html.Div(
        id='input-boxes',
        children= [
            dbc.InputGroup(
                [dbc.InputGroupAddon("Mean", addon_type="prepend"),
                 dbc.Input(id="input-mean", value=0, type='number')],
                size="lg",
            ),
            html.Br(),
            dbc.InputGroup(
                [dbc.InputGroupAddon("Std. Dev.", addon_type="prepend"),
                 dbc.Input(id="input-std", value=1, type='number')],
                size='lg',
            )
        ],
        style={"margin-left": "20px", "margin-right": "200px"}
    )
    return input_group
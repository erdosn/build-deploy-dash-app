import dash_html_components as html
import dash_bootstrap_components as dbc


def render_input_group():
    input_group = html.Div(
        [
            dbc.InputGroup(
                [dbc.InputGroupAddon("Mean", addon_type="prepend"),
                 dbc.Input(id='input-mean', value=0, type='number')],
            ),
            html.Br(),
            dbc.InputGroup(
                [dbc.InputGroupAddon("Std. Dev.", addon_type="prepend"),
                 dbc.Input(id='input-std', value=1, type='number')]
            ),
        ]
    )
    return input_group
import numpy as np
import pandas as pd
import plotly.express as px
import dash_core_components as dcc

def render_histogram(mu=0, std=1):
    x0 = np.random.normal(mu, std, 1000)
    df = pd.DataFrame(x0, columns=['data'])
    fig = px.histogram(df, x='data', marginal='box')

    # this is our app component
    histogram = dcc.Graph(figure=fig)
    return histogram
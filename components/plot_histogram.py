import dash_core_components as dcc
import plotly.express as px
import numpy as np
import pandas as pd


def render_histogram(mu=0, std=1):
    x = np.random.normal(loc=mu, scale=std, size=1000)
    df = pd.DataFrame(data=x, columns=['data'])
    fig = px.histogram(df, x='data', marginal='box')
    histogram = dcc.Graph(figure=fig)
    return histogram
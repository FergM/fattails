import dash
from dash import dcc, html
import numpy as np
import pandas as pd
import plotly.graph_objs as go

import hidden_moments as hide

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# FUNCTIONS

def get_data(n_max, meta_n, moment, source='new'):

    if source=='new':
        # GENERATE DATA
        # Speed Note: Takes a minute to run for n_max=40, meta_n=50, moment=0
        print("STARTING TO GENERATE DATA")
        hidden_moment_values = hide.make_hidden_moment_convergence_data(n_max=40, meta_n=50, moment=moment)
        print("FINISHED GENERATING DATA")

    elif source=='pickle':
        hidden_moment_values = pd.read_pickle('hidden_moment_samples.pkl')

    else:
        # Simplified Dataset
        hidden_moment_values = {'a': [1,2,3], 'b': [4,5,6]}

    return hidden_moment_values


def make_plots(hidden_moment_values):
    """ 
    
    hidden_moment_values : 
    """

    # Calculate Average Values
    average_values = {key: np.mean(value) for key, value in hidden_moment_values.items()}

    # ------------------------------------------------------------------------------------
    # MAKE TRACES
    
    # Line Traces
    average_trace = go.Scatter(x=list(average_values.keys()), y=list(average_values.values()), mode='lines+markers', name='Average')
    
    # Point Traces
    # Format the raw datapoints as traces
    raw_data_traces = []
    for key, values in hidden_moment_values.items():
        raw_data_traces.append(go.Scatter(x=[key] * len(values), y=values, mode='markers', name=key))

    plots = [dcc.Graph(
                      id='average-plot',
                      figure={
                          'data': [average_trace,]
                                  + raw_data_traces,
                          'layout': go.Layout(
                              title='Convergence of the Average',
                              xaxis=dict(title='Sample Size'),
                              yaxis=dict(title=f'Hidden Moment: {moment}'),
                          )
                      }
                     ),

             dcc.Graph(
                       id='scatter-plot',
                       figure={
                           'data': raw_data_traces,
                           'layout': {
                               'title': 'Raw Data For Each Sample Size',
                               'xaxis': {'title': 'Sample Size'},
                               'yaxis': {'title': f'Hidden Moment: {moment}'}
                           }
                       }
                      ),
            ]

    return plots

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# SETUP
moment = 0

hidden_moment_values = get_data(n_max=40, 
                                meta_n=50, 
                                moment=moment,
                                source='pickle')

plots = make_plots(hidden_moment_values)

# Run the app
if __name__ == '__main__':

    # Create Dash app
    app = dash.Dash(__name__)

    # ------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------
    # LAYOUT

    app.layout = html.Div(
                          plots,
                         )

    app.run_server(debug=True)

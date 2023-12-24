import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

import hidden_moments as hide

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# FUNCTIONS

def get_data(n_max=None, meta_n=None, moment=None, source='new'):

    if source=='new':
        # GENERATE DATA
        # Speed Note: Takes a minute to run for n_max=40, meta_n=50, moment=0
        print("STARTING TO GENERATE DATA")
        hidden_moment_values = hide.make_hidden_moment_convergence_data(n_max, meta_n, moment=moment)
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


def histogram_w_slider(meta_sample):
    """
    meta_sample
        Dictionary with sample size as keys
        And each key maps to a list of values
    """

    keys = meta_sample.keys()
    #slider_min, slider_max = min(keys), max(keys)
    #slider_marks = [{'label': str(key), 'value': key} for key in keys]

    # largest_value = meta_sample.abs().max().max()

    histogram_layout = [
                        html.H1("Histogram Title"),
                        
                        dcc.Slider(0,40,1,
                                   id="sample-size",
                                   value=min(keys), 
                                  ),
                        
                        # Histogram plot
                        dcc.Graph(id='histogram'),
                       ]

    return histogram_layout

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# SETUP
moment = 0

hidden_moment_values = get_data(n_max=40,
                                meta_n=500, 
                                moment=moment,
                                source='pickle')

df = pd.DataFrame(hidden_moment_values)

plots = make_plots(hidden_moment_values)

histogram_layout = histogram_w_slider(hidden_moment_values)

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# APP
if __name__ == '__main__':

    # Create Dash app
    app = dash.Dash(__name__)



    # ------------------------------------------------------------------------------------
    # CALLBACKS
    @app.callback(
                    Output('histogram', 'figure'),
                    [Input('sample-size', 'value')]
    )
    def update_histogram(selected_key):

        largest_value = df.max().max()

        fig = px.histogram(df,
                           x=selected_key,
                           title=f'Histogram for Key {selected_key}',
                           range_x=[0, largest_value],
        )
        
        return fig

    # ------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------
    # LAYOUT
    app.layout = html.Div(
                            plots \
                          + histogram_layout
                         )

    app.run_server(debug=True)

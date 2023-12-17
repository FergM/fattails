import dash
from dash import dcc, html
import numpy as np
import plotly.graph_objs as go

import hidden_moments as hide

# Create Dash app
app = dash.Dash(__name__)

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# SETUP
moment = 0

# GENERATE DATA
# Speed Note: Takes a minute to run for n_max=40, meta_n=50, moment=0
print("STARTING TO GENERATE DATA")
hidden_moment_values = hide.make_hidden_moment_convergence_data(n_max=40, meta_n=50, moment=moment)
# DEBUG
#hidden_moment_values = {'a': [1,2,3], 'b': [4,5,6]}
print("FINISHED GENERATING DATA")


# Calculate Average Values
average_values = {key: np.mean(value) for key, value in hidden_moment_values.items()}

# Traces
# Trace Of Average Values
average_trace = go.Scatter(x=list(average_values.keys()), y=list(average_values.values()), mode='lines+markers', name='Average')
# Raw Data Traces
# Format the raw datapoints as traces
raw_data_traces = []
for key, values in hidden_moment_values.items():
    raw_data_traces.append(go.Scatter(x=[key] * len(values), y=values, mode='markers', name=key))

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# Layout of the app
app.layout = html.Div([

    dcc.Graph(
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
    )


])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

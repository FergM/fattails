import dash
from dash import dcc, html
import numpy as np
import plotly.graph_objs as go

import hidden_moments as hide

# GENERATE DATA
# Speed Note: Takes a minute to run for n_max=40, meta_n=50, moment=0
print("STARTING TO GENERATE DATA")
hidden_moment_values = hide.make_hidden_moment_convergence_data(n_max=40, meta_n=50, moment=0)
# DEBUG # hidden_moment_values = {'a': [1,2,3], 'b': [4,5,6]}
print("FINISHED GENERATING DATA")

# Calculate average values
average_values = {key: np.mean(value) for key, value in hidden_moment_values.items()}

# Create Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([

    dcc.Graph(
        id='average-plot',
        figure={
            'data': [
                go.Scatter(x=list(average_values.keys()), y=list(average_values.values()), mode='lines+markers', name='Average'),
            ],
            'layout': go.Layout(
                title='Average Values Plot',
                xaxis=dict(title='Key'),
                yaxis=dict(title='Average Value')
            )
        }
    )

])
# Roughwork to add scatter too:
# ```
#               go.Scatter(x=list(average_values.keys()), y=[val[0] for val in average_values.values()], mode='markers', name='Data Points'),
# ```
# Add the above in the 'data' list

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
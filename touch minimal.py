import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np

# Create app
app = Dash()

# Load the data

# Define the layout
app.layout = []

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True) # debug=True enables hot-reloading
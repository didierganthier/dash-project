import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load the data
emissions_df = pd.read_csv("emissions.csv")
# Sample data for demonstration purposes
emissions_df = emissions_df.query("year >= 1950")
country_df = emissions_df.query("country == 'France'")

# Create components
header = html.H1("CO2 Emissions Dashboard", style={"textAlign": "center"})

country_co2 = px.line(
    country_df,
    x="year",
    y="co2",
    title="CO2 emissions in France"
)

country_co2_split = px.line(
    country_df,
    x="year",
    y=['oil_co2', 'coal_co2', 'gas_co2'],
    title="CO2 emissions by fuel type in France"
)

app.layout = [
    header,
    dbc.Row(children=[
        dbc.Col(
            dcc.Graph(
                id="country_co2",
                figure=country_co2,
            ), 
            width=8),
        dbc.Col(
            dcc.Graph(
               id="country_co2_split",
               figure=country_co2_split 
            ),
        width=8),
    ])
]

# Run the app
if __name__ == "__main__":
    app.run(debug=True) # debug=True enables hot-reloading
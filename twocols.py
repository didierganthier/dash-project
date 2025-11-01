import dash
from dash import Dash, Input, Output, callback, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load the data
emissions_df = pd.read_csv("emissions.csv")
# Sample data for demonstration purposes
emissions_df = emissions_df.query("year >= 1950")

# Create components
header = html.H1("CO2 Emissions Dashboard", style={"textAlign": "center"})
country_dropdown = dcc.Dropdown(
    id="country_dropdown",
    options=[{"label": c, "value": c} for c in emissions_df["country"].unique()],
    value="France",
)

# Create callbacks
@callback(
    Output("country_co2", "figure"),
    Input("country_dropdown", "value")
)
def update_country_df(country):
    country_df = emissions_df[emissions_df["country"] == country]
    fig = px.line(country_df, x="year", y="co2", title=f"CO2 emissions in {country}")
    return fig

# Create callbacks
@callback(
    Output("country_co2_split", "figure"),
    Input("country_dropdown", "value")
)
def update_country_df_split(country):
    country_df = emissions_df[emissions_df["country"] == country]
    fig = px.line(country_df, x="year", y=['oil_co2', 'coal_co2', 'gas_co2'], title=f"CO2 emissions by fuel type in {country}")
    return fig

app.layout = [
    dbc.Row(children=[
         dbc.Col(header, width=12),
         dbc.Col(country_dropdown, width=4)
        ],
    ),
    dbc.Row(children=[
        dbc.Col(
            dcc.Graph(
                id="country_co2",
            ), 
            width=8),
        dbc.Col(
            dcc.Graph(
               id="country_co2_split",
            ),
        width=8),
    ])
]

# Run the app
if __name__ == "__main__":
    app.run(debug=True) # debug=True enables hot-reloading
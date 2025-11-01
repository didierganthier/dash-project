import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Create app
app = Dash()

# Load the data
emissions_df = pd.read_csv("emissions.csv")
# Sample data for demonstration purposes
emissions_df = emissions_df.query("year >= 1950")
country_df = emissions_df.query("country == 'France'")

# Define the layout
app.layout = [
    html.H1("CO2 Emissions Dashboard", style={"textAlign": "center"}),
    dcc.Graph(
        id="country_co2",
        figure=px.line(
            country_df,
            x="year",
            y="co2",
            title="CO2 emissions in France"
        )
    )
]

# Run the app
if __name__ == "__main__":
    app.run(debug=True) # debug=True enables hot-reloading
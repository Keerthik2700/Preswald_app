import pandas as pd
import plotly.express as px
from preswald import text, table, slider, plotly

# Load the Iris dataset for interactive exploration
iris_df = pd.read_csv('data/iris.csv')

# Add a simple title and description
text("# Iris Flower Analysis Dashboard")
text("This app provides a quick way to explore sepal and petal dimensions for different Iris species.")

# Show the raw dataset for context
text("## Full Dataset")
table(iris_df, title="Complete Iris Dataset")

# Add an adjustable filter for sepal length
text("## Filter by Sepal Length")
min_sepal = slider(
    "Set minimum sepal length (cm)",
    min_val=iris_df["sepal_length"].min(),
    max_val=iris_df["sepal_length"].max(),
    default=5.0
)

# Filter the data dynamically based on user selection
filtered_iris = iris_df[iris_df["sepal_length"] >= min_sepal]

# Show the filtered rows
table(filtered_iris, title=f"Filtered Iris Data (Sepal Length ≥ {min_sepal} cm)")

# Plot: Sepal Length vs Petal Length, colored by species
text("## Sepal vs Petal Length")
scatter = px.scatter(
    filtered_iris,
    x="sepal_length",
    y="petal_length",
    color="species",
    title="Sepal Length vs Petal Length",
    labels={"sepal_length": "Sepal Length (cm)", "petal_length": "Petal Length (cm)"}
)
plotly(scatter)

# Plot: Average Petal Length by Species
text("## Average Petal Length per Species")
avg_petal_len = (
    iris_df.groupby("species")["petal_length"]
    .mean()
    .reset_index(name="average_petal_length")
)

bar_chart = px.bar(
    avg_petal_len,
    x="species",
    y="average_petal_length",
    title="Mean Petal Length by Species",
    labels={"species": "Species", "average_petal_length": "Average Petal Length (cm)"},
    color="species"
)
plotly(bar_chart)

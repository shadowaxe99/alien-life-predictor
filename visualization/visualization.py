```python
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

# Import processed data
from data_collection.data_preprocessing import processed_data

# DOM Element ID
visualization_container = "visualization-container"

def create_visualization():
    # Set up the notebook for Bokeh
    output_notebook()

    # Create a new plot with a title and axis labels
    p = figure(title="Probability of Alien Life Existence", x_axis_label='Regions of the Universe', y_axis_label='Probability')

    # Add a line renderer with legend and line thickness
    p.line(processed_data['region'], processed_data['probability'], legend_label="Probability", line_width=2)

    # Show the results
    show(p)

    # Send a message that visualization is created
    send_message("VisualizationCreated")

def send_message(message):
    print(f"{message} in {visualization_container}")

if __name__ == "__main__":
    create_visualization()
```
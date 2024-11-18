from shiny import App, render, ui
from shinywidgets import render_altair, output_widget
import altair as alt
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.panel_title("Histogram of 200 Draws from Normal with mean mu"),
    ui.input_slider("mu", "mean mu", 0, 100, 20), 
    ui.output_plot("my_hist"),
    ui.output_text_verbatim("my_sumstats")
)

def server(input, output, session):
    @render.plot
    def my_hist():
        sample = np.random.normal(input.n(), 20, 200)
        fig, ax = plt.subplots()
        ax.hist(sample, bins=30, color='blue', alpha=0.7)
        return fig
    @render.text
    def my_sumstats():
        sample = np.random.normal(input.n(), 20, 100)
        min = np.min(sample)
        max = np.max(sample)
        median = np.median(sample)
        return "Min:" + str(min) + ", Median: " + str(median), ", Max: " + str(max)

app = App(app_ui, server)

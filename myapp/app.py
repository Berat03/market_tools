from shiny import ui, render, App
from matplotlib import pyplot as plt
import matplotlib
from market_momentum import simple_moving_average
matplotlib.use('agg')

app_ui = ui.page_fluid(
    ui.h1('Hello'),
    ui.output_image("my_sma"),
)

def server(input, output, session):
    @output
    @render.plot
    def my_sma():
        data = simple_moving_average()
        data.plot()

app = App(app_ui, server)
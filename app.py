from flask import Flask, render_template
import pandas as pd
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from static import plot_success_rate, plot_return_on_strategy, plot_average_profit_loss

app = Flask(__name__)

# Load the Excel file
excel_file_path = 'C:/Users/91725/Downloads/Tradzo performance.xlsx'
df = pd.read_excel(excel_file_path, sheet_name='MASTER')

# Folder to save plots
saved_plots_folder = 'static/saved_plots/'

@app.route('/')
def index():
    success_rate_plot = plot_success_rate(df, saved_plots_folder)
    return_on_strategy_plot = plot_return_on_strategy(df, saved_plots_folder)
    avg_profit_loss_plot = plot_average_profit_loss(df, saved_plots_folder)

    return render_template('index.html', success_rate_plot=success_rate_plot,
                           return_on_strategy_plot=return_on_strategy_plot,
                           avg_profit_loss_plot=avg_profit_loss_plot)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
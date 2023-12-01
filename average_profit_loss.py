import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd  # Import pandas with an alias

def plot_average_profit_loss(df, save_folder):
    start_row = 14
    end_row = 18
    values = df.loc[start_row:end_row, ['SUCCESS RATE', 'Unnamed: 6']]

    bar_width = 0.4
    bar_spacing = 0.2  # Adjust the spacing between bars

    fig, ax = plt.subplots(figsize=(10, 6))


    # Convert bar_positions to a list before adding spacing
    bar_positions = list(range(len(values)))

    # Positioning the bars with spacing
    bar_pos = ax.barh([pos + bar_spacing for pos in bar_positions], values['SUCCESS RATE'], color='green', height=bar_width, label='Average Profit')
    bar_neg = ax.barh([pos - bar_spacing for pos in bar_positions], values['Unnamed: 6'], color='red', height=bar_width, label='Average Loss')

    # Hardcoded names for each bar on the y-axis
    bar_names = ['Intraday', 'Intraday options', 'Options Maker', 'Trading Calls', 'Index Trades']

    for bar, value, name in zip(bar_pos, values['SUCCESS RATE'], bar_names):
        ax.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height() / 2, f"{round(value, 2)}", ha='left', va='center', color='black')

    for bar, value, name in zip(bar_neg, values['Unnamed: 6'], bar_names):
        ax.text(bar.get_width() - 0.02, bar.get_y() + bar.get_height() / 2, f"{round(value, 2)}", ha='right', va='center', color='black')

    ax.set_yticks([pos + bar_spacing for pos in bar_positions])
    ax.set_yticklabels(bar_names)  # Use the hardcoded names for y-axis labels

    ax.legend()

    # Save the plot to a file in the specified folder
    save_path = os.path.join(save_folder, 'avg_profit_loss_plot.png')
    plt.savefig(save_path)
    plt.close()

    return 'avg_profit_loss_plot.png'

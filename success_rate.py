import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_success_rate(df, save_folder):
    start_row = 1
    end_row = 5
    values = df.loc[start_row:end_row, 'SUCCESS RATE']
    bar_positions = range(len(values))
    
    fig, ax = plt.subplots(figsize=(10, 6))

    bar_width = 0.4
    bars = plt.bar(bar_positions, values*100, width=bar_width, align='center')

    # Add text annotations on top of each bar
    for bar, value in zip(bars, values*100):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{round(value, 2)}%", ha='center', va='bottom')

    # Set custom bar names on the x-axis
    custom_xticks = ['Intraday', 'Intraday options', 'Options Maker', 'Trading Calls', 'Index Trades']
    plt.xticks(bar_positions, custom_xticks)

    # Save the plot to a file in the specified folder
    save_path = os.path.join(save_folder, 'success_rate_plot.png')
    plt.savefig(save_path)
    plt.close()

    return 'success_rate_plot.png'

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_return_on_strategy(df, save_folder):
    start_row = 14  # adjust this to the starting row you want
    end_row = 18    # adjust this to the ending row you want

    selected_data = df.loc[start_row:end_row, ['NEGATIVE TRADES']]
    
    # Extract values from the selected column
    values = selected_data['NEGATIVE TRADES']
    figsize=(10, 6)
    plt.figure(figsize=figsize)

    # Determine colors based on positive or negative values
    color = ['green' if val >= 0 else 'red' for val in values]

    # Define hardcoded bar names
    bar_names = ['Intraday', 'Intraday options', 'Options Maker', 'Trading Calls', 'Index Trades']

    # Create a horizontal bar plot
    plt.barh(selected_data.index, values*100, color=color)
    
    # Add text annotations for values
    for index, value in zip(selected_data.index, values*100):
        plt.text(value, index, f'{value:.2f}%', ha='left', va='center', color='black')
    
    # Set labels and title
    plt.xlabel('Values')
    plt.ylabel('Index')
    
    # Set y-axis ticks with hardcoded bar names
    plt.yticks(selected_data.index, bar_names)

    # Save the plot to a file in the specified folder
    save_path = os.path.join(save_folder, 'return_on_strategy_plot.png')
    plt.savefig(save_path)
    
    # Close the plot to release resources
    plt.close()

    return 'return_on_strategy_plot.png'

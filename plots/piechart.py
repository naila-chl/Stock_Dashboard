import plotly.express as px
import pandas as pd

def pie_chart(data, selected_symbols):
    # Check if the selected symbols are in the data columns
    price_changes = []
    for symbol in selected_symbols:
        if symbol in data.columns:
            # Calculate the percentage change for the selected symbol
            symbol_data = data[symbol].tail(1)  # Get the last available data for the symbol
            price_changes.append(symbol_data.pct_change().iloc[-1] * 100)  # Calculate percentage change
        else:
            # If the symbol is not in the data, append 0 or NaN (depending on your preference)
            price_changes.append(0)

    # Create a DataFrame for the pie chart
    pie_data = pd.DataFrame({
        'Symbol': selected_symbols,
        'Price Change (%)': price_changes
    })

    # Create the pie chart
    fig = px.pie(pie_data, names='Symbol', values='Price Change (%)', title='Stock Performance Distribution')
    return fig

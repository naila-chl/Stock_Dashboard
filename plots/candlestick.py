import plotly.graph_objects as go

def candlestick_plot(data):
    fig = go.Figure()
    symbols = data['Symbol'].unique()
    for symbol in symbols:
        symbol_data = data[data['Symbol'] == symbol]
        fig.add_trace(go.Candlestick(
            x=symbol_data['Date'],
            open=symbol_data['Open'],
            high=symbol_data['High'],
            low=symbol_data['Low'],
            close=symbol_data['Close'],
            name=symbol,
        ))
    fig.update_layout(title="Candlestick Chart", xaxis_title="Date", yaxis_title="Price")
    return fig

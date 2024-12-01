import yfinance as yf
import plotly.graph_objects as go

def compare_symbols_chart(symbols, period):
    """Compare plusieurs actions sur une même période."""
    fig = go.Figure()
    for symbol in symbols:
        data = yf.download(symbol, period=period)
        fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=symbol))
    fig.update_layout(title="Comparaison des prix de clôture", xaxis_title="Date", yaxis_title="Prix ($)")
    return fig

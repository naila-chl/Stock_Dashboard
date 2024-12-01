import plotly.graph_objects as go

def candlestick_plot(data):
    """Crée un graphique en chandelier."""
    fig = go.Figure(data=[go.Candlestick(
        x=data['Date'],
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    )])
    fig.update_layout(title="Graphique en chandelier", xaxis_title="Date", yaxis_title="Prix ($)")
    return fig

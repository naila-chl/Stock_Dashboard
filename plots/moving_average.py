import plotly.graph_objects as go

def moving_average_chart(data, window=7):
    """Crée un graphique avec la moyenne mobile."""
    data['Moving Average'] = data['Close'].rolling(window=window).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], mode='lines', name='Prix de clôture'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Moving Average'], mode='lines', name=f'Moyenne mobile ({window} jours)'))
    fig.update_layout(title="Prix de clôture avec moyenne mobile", xaxis_title="Date", yaxis_title="Prix ($)")
    return fig

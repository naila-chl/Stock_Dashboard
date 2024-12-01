import pandas as pd
import plotly.express as px

def rsi_chart(data, period=14):
    """Crée un graphique du RSI (Relative Strength Index)."""
    delta = data['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))

    fig = px.line(data, x='Date', y='RSI', title="Indice de force relative (RSI)")
    fig.add_hline(y=70, line_dash="dash", line_color="red", annotation_text="Surachat", annotation_position="top left")
    fig.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="Survente", annotation_position="bottom left")
    fig.update_layout(xaxis_title="Date", yaxis_title="RSI")
    return fig

import plotly.express as px

def rsi_chart(data):
    data['RSI'] = 100 - (100 / (1 + data['Close'].pct_change().rolling(window=14).mean()))
    fig = px.line(data, x="Date", y="RSI", color="Symbol", title="RSI (Relative Strength Index)")
    return fig

import plotly.express as px

def moving_average_chart(data):
    data['Moving Average'] = data['Close'].rolling(window=10).mean()
    fig = px.line(data, x="Date", y="Moving Average", color="Symbol", title="10-Day Moving Average")
    return fig

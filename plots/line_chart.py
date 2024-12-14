import plotly.express as px

def line_chart(data, symbols):
    fig = px.line(data, x="Date", y="Close", color="Symbol", title="Stock Price Trends")
    return fig

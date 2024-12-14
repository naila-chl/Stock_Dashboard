import plotly.express as px

def daily_variation_chart(data):
    data['Daily Change (%)'] = data['Close'].pct_change() * 100
    fig = px.bar(data, x="Date", y="Daily Change (%)", color="Symbol", title="Daily Price Change (%)")
    return fig

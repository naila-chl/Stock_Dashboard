import plotly.express as px

def price_distribution_chart(data):
    fig = px.histogram(data, x="Close", color="Symbol", title="Price Distribution")
    return fig

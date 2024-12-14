import plotly.express as px

def volume_bar(data):
    fig = px.bar(data, x="Date", y="Volume", color="Symbol", title="Trading Volume")
    return fig

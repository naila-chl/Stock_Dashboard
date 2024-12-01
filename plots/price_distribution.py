import plotly.express as px

def price_distribution_chart(data):
    """Crée un histogramme des prix de clôture."""
    fig = px.histogram(data, x='Close', nbins=50, title="Distribution des prix de clôture")
    fig.update_layout(xaxis_title="Prix ($)", yaxis_title="Fréquence")
    return fig

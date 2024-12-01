import plotly.express as px

def volume_bar(data):
    """Crée un graphique des volumes de transactions."""
    fig = px.bar(data, x="Date", y="Volume", title="Volume des transactions")
    fig.update_layout(xaxis_title="Date", yaxis_title="Volume")
    return fig

import plotly.express as px

def line_chart(data):
    """Crée un graphique de tendance pour le prix de clôture."""
    fig = px.line(data, x="Date", y="Close", title="Tendance des prix de clôture")
    fig.update_layout(xaxis_title="Date", yaxis_title="Prix ($)")
    return fig

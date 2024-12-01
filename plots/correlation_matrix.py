import plotly.express as px

def correlation_matrix(data):
    """Crée une matrice de corrélation."""
    corr = data[['Open', 'High', 'Low', 'Close', 'Volume']].corr()
    fig = px.imshow(corr, text_auto=True, title="Matrice de corrélation")
    fig.update_layout(xaxis_title="Attributs", yaxis_title="Attributs")
    return fig

import plotly.express as px

def heatmap_plot(data):
    """Crée une heatmap pour les variations journalières."""
    data['Daily Change'] = data['Close'] - data['Open']
    data['% Change'] = (data['Daily Change'] / data['Open']) * 100
    fig = px.density_heatmap(data, x="Date", y="% Change", title="Carte de chaleur des variations journalières")
    fig.update_layout(xaxis_title="Date", yaxis_title="% de variation")
    return fig

import plotly.express as px

def correlation_matrix(data):
    pivot_data = data.pivot(index="Date", columns="Symbol", values="Close")
    fig = px.imshow(pivot_data.corr(), text_auto=True, title="Correlation Matrix")
    return fig

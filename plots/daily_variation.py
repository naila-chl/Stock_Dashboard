import plotly.express as px

def daily_variation_chart(data):
    """Crée un graphique des variations journalières (%)"""
    data['Daily Variation (%)'] = data['Close'].pct_change() * 100
    fig = px.bar(data, x="Date", y="Daily Variation (%)", title="Variations journalières en pourcentage")
    fig.update_layout(xaxis_title="Date", yaxis_title="Variation (%)", showlegend=False)
    return fig

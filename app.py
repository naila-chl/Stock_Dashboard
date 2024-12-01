import streamlit as st
from data.stock_data import fetch_stock_data
from plots.candlestick import candlestick_plot
from plots.line_chart import line_chart
from plots.volume_bar import volume_bar
from plots.heatmap import heatmap_plot
from plots.daily_variation import daily_variation_chart
from plots.moving_average import moving_average_chart
from plots.compare_symbols import compare_symbols_chart
from plots.rsi import rsi_chart
from plots.price_distribution import price_distribution_chart
from plots.correlation_matrix import correlation_matrix

# Titre de l'application
st.title("Interactive Stock Dashboard")

# Sidebar pour sélectionner les paramètres
st.sidebar.header("Paramètres")
symbol = st.sidebar.selectbox("Choisissez un symbole boursier", ["AAPL", "TSLA", "MSFT", "GOOG", "AMZN"])
period = st.sidebar.selectbox("Choisissez une période:", ["1mo", "3mo", "6mo", "1y", "5y"], index=0)  # Par défaut "1mo"
visualization = st.sidebar.selectbox(
    "Choisissez une visualisation:", 
    ["Candlestick", "Line Chart", "Volume", "Heatmap", "Daily Variation", 
     "Moving Average", "Comparaison des symboles", "RSI", "Distribution", "Correlation Matrix"]
)

# Télécharger les données
st.write(f"**Données pour {symbol} ({period})**")
data = fetch_stock_data(symbol, period)

if data is not None:
    # Afficher les données brutes
    st.write(data.tail())

    # Calcul des différences de prix et des variations en pourcentage
    data['Price Change'] = data['Close'].diff()  # Différence de prix
    data['Price Change (%)'] = data['Close'].pct_change() * 100  # Variation en pourcentage

    # Afficher les informations des différences de prix et des variations en pourcentage
    st.subheader("Différences de prix et variations en pourcentage")
    st.write(data[['Close', 'Price Change', 'Price Change (%)']].tail())  # Afficher les 5 dernières lignes

    # Afficher le graphique choisi
    if visualization == "Candlestick":
        st.plotly_chart(candlestick_plot(data))
    elif visualization == "Line Chart":
        st.plotly_chart(line_chart(data))
    elif visualization == "Volume":
        st.plotly_chart(volume_bar(data))
    elif visualization == "Heatmap":
        st.plotly_chart(heatmap_plot(data))
    elif visualization == "Daily Variation":
        st.plotly_chart(daily_variation_chart(data))
    elif visualization == "Moving Average":
        st.plotly_chart(moving_average_chart(data))
    elif visualization == "Comparaison des symboles":
        symbols = st.sidebar.text_input("Entrez les symboles à comparer (séparés par des virgules)", "AAPL,MSFT").split(',')
        st.plotly_chart(compare_symbols_chart(symbols, period))
    elif visualization == "RSI":
        st.plotly_chart(rsi_chart(data))
    elif visualization == "Distribution":
        st.plotly_chart(price_distribution_chart(data))
    elif visualization == "Correlation Matrix":
        st.plotly_chart(correlation_matrix(data))

    # Bouton pour télécharger les données en CSV
    st.download_button(
        label="Télécharger les données en CSV",
        data=data.to_csv(index=True).encode('utf-8'),
        file_name=f"{symbol}_data.csv",
        mime='text/csv',
    )
else:
    st.error("Impossible de charger les données.")

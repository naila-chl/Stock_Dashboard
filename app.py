import streamlit as st
import plotly.express as px
import pandas as pd
from data.stock_data import fetch_stock_data
from plots.candlestick import candlestick_plot
from plots.line_chart import line_chart
from plots.volume_bar import volume_bar
from plots.daily_variation import daily_variation_chart
from plots.moving_average import moving_average_chart
from plots.compare_symbols import compare_symbols_chart
from plots.rsi import rsi_chart
from plots.price_distribution import price_distribution_chart
from plots.correlation_matrix import correlation_matrix
from plots.piechart import pie_chart  # Import the pie chart function


# Title of the application
st.title("Stock Market Dashboard")

# Sidebar to select symbols and period
st.sidebar.header("Select Parameters")

# Predefined list of stock symbols for checklist
available_symbols = ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"]
selected_symbols = st.sidebar.multiselect(
    "Select stock symbols:", 
    options=available_symbols, 
    default=available_symbols  # Default to all selected
)

# Period selection
period = st.sidebar.selectbox("Select period:", ["1mo", "3mo", "6mo", "1y", "5y"])

# Load the data
if selected_symbols:
    st.write(f"**Data for {', '.join(selected_symbols)} ({period})**")
    data = fetch_stock_data(selected_symbols, period)

    if data is not None:
        st.write(data.tail())

        # Use Streamlit columns to display multiple plots side by side
        col1, col2 = st.columns(2)

        # Candlestick Plot
        with col1:
            st.plotly_chart(candlestick_plot(data))

        # Line Chart (For Multiple Symbols in One Chart)
        with col2:
            st.plotly_chart(line_chart(data, selected_symbols))

        # Display other charts
        col3, col4 = st.columns(2)

        # Volume Bar Plot
        with col3:
            st.plotly_chart(volume_bar(data))

        

        # Daily Variation Plot
        with col1:
            st.plotly_chart(daily_variation_chart(data))

        # Moving Average
        with col2:
            st.plotly_chart(moving_average_chart(data))

        # RSI Plot
        with col3:
            st.plotly_chart(rsi_chart(data))

        # Price Distribution Plot
        with col4:
            st.plotly_chart(price_distribution_chart(data))

        # Correlation Matrix Plot
        with col1:
            st.plotly_chart(correlation_matrix(data))

            

        # Download Button
        st.download_button(
            label="Download Data as CSV",
            data=data.to_csv(index=True).encode('utf-8'),
            file_name=f"{','.join(selected_symbols)}_data.csv",
            mime='text/csv',
        )
    else:
        st.error("Failed to load data.")
else:
    st.warning("Please select at least one stock symbol.")

import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol, period="1y"):
    """Récupère les données boursières pour un symbole donné et une période spécifique."""
    try:
        # Télécharger les données boursières avec yfinance
        data = yf.download(symbol, period=period)
        
        # Vérifier si des données ont été téléchargées
        if data.empty:
            raise ValueError(f"Aucune donnée disponible pour {symbol} pendant {period}.")

        # Assurez-vous que les données ont bien un index de type DateTime
        data.reset_index(inplace=True)

        # Retourner les données
        return data
    except Exception as e:
        print(f"Erreur lors du téléchargement des données : {e}")
        return None


"""
    Creates a snapshot of stocks and their current values , displays current snapshot as a pdf
"""
import os
import requests
from urllib.parse import urlencode, urljoin
from dotenv import load_dotenv
from typing import List

class Stocker:
  """  
  
    Initializes the stocker class.
    
    The Stocker class contains functionality to generate the current stock value,
      upward/downward trend, theta's, optionality etc. of a given set of chosen stocks

      It also has the ability to render line by line these values in a pdf file, for 
        use by the dtp-controll-panel app

        stocker = {
          "IBM" : {
            price: 1.23
            lastPrice: 1.23
            monthly_trend: "upward"
          },

        }

      Currently sources data from the following API:
        https://www.alphavantage.co/

        Generate an api key from : https://www.alphavantage.co/support/#api-key
        Store API KEY in environment var or .env , see sample

      

  """
  def __init__(self, stocks  : List[str] = []):
    print("Loading env...")
    load_dotenv()
    
    self.stocks = stocks
    self.stocker = {

    }
    self.alpha_v_api_key = os.getenv("STOCKER_API_KEY")


  def get_ticket_daily(self, ticker: str = ""):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "IBM",
        "apikey": self.alpha_v_api_key,
    }

    # Constructing the URL with parameters
    url_with_params = base_url + '?' + urlencode(params)
    r = requests.get(url_with_params)
    data = r.json()

    print(data)

stocker = Stocker()
stocker.get_ticket_daily()
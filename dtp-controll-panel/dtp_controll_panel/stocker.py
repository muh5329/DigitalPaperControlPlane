
"""
    Creates a snapshot of stocks and their current values , displays current snapshot as a pdf
"""
import os
import requests
from urllib.parse import urlencode, urljoin
from dotenv import load_dotenv
from typing import List
from datetime import datetime,timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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
            volume : 123123
            monthly_trend: "upward"
          },

        }
        

      Currently sources data from the following API:
        https://www.alphavantage.co/

        Generate an api key from : https://www.alphavantage.co/support/#api-key
        Store API KEY in environment var or .env , see sample
      
        The above api is rate limited to 25 request per day, might consider using
        https://site.financialmodelingprep.com/developer/docs

        but for the purposes of a single time load non-realtime stock
           maker app there is no need 

           but an alternative is https://site.financialmodelingprep.com/developer/docs  
      

  """
  def __init__(self, stocks  : List[str] = []):
    print("Loading env...")
    load_dotenv()
    
    self.stocks = stocks
    self.stocker = {}
    
    self.alpha_v_api_key = os.getenv("STOCKER_API_KEY")
    self.default_tickers = os.getenv("DEFAULT_TICKERS").split(',')


  def get_ticker_daily(self, ticker: str = ""):
    current_date = datetime.now()
    yyyy_mm_dd = current_date.strftime("%Y-%m-%d")

   
    yesterday = current_date - timedelta(days=1)
    yesterday_yyyy_mm_dd = yesterday.strftime('%Y-%m-%d')

    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": ticker,
        "apikey": self.alpha_v_api_key,
    }

    # Constructing the URL with parameters
    url_with_params = base_url + '?' + urlencode(params)
    r = requests.get(url_with_params)
    data = r.json()
    # print(data)
    if yyyy_mm_dd in data["Time Series (Daily)"]:
      return data["Time Series (Daily)"][yyyy_mm_dd]
    else:
      return data["Time Series (Daily)"][yesterday_yyyy_mm_dd]
    
  def get_dummy_daily_ticker(self,ticker=""):
    data = {'1. open': '121.7700', '2. high': '122.8700', '3. low': '118.7400', '4. close': '120.9100', '5. volume': '222551158'}
    return data

  def build_default_tickers_daily(self):
    for ticker in self.default_tickers:
      data = stocker.get_ticker_daily(ticker)
      #data = stocker.get_dummy_daily_ticker(ticker)
      self.stocker[ticker] =  {
              'price': data['1. open'],
              'lastPrice': '',
              'volume' : data['5. volume'],
              'trend': ''
      }

  def create_pdf_from_dict(self,data, filename):
      c = canvas.Canvas(filename, pagesize=letter)
      y = 750  # Starting y-coordinate for writing data

      for key, value in data.items():
          text = f"{key}: {value}"
          c.drawString(100, y, text)
          y -= 20  # Move to the next line

      c.save()

  

# stocker = Stocker()
# stocker.build_default_tickers_daily()
# stocker.create_pdf_from_dict(stocker.stocker, "output.pdf")


"""
    Creates a snapshot of stocks and their current values , displays current snapshot as a pdf
"""
from typing import List


class Stocker:
  """  
  
    Initializes the stocker class.
    
    The Stocker class contains functionality to generate the current stock value,
      upward/downward trend, theta's, optionality etc. of a given set of chosen stocks

      It also has the ability to render line by line these values in a pdf file, for 
        use by the dtp-controll-panel app

  """
  def __init__(self, stocks  : List[str] = []):
    self.stocks = stocks


  def generate_daily_values(self):
    do="something"
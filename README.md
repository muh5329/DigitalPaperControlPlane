# DigitalPaperControlPlane

Sony Digital Paper control plane to show random stuff on a set interval




[![Python](https://img.shields.io/badge/Python-3.12.2-green.svg)](https://www.python.org/)



## Features

- Random daily art
- NYT or other newspaper [TODO] 
- Comic / Manga Page [TODO] 
- QR Code [TODO] 
- Word of the day[TODO] 
- Multi Function  [TODO]  
    - Weather
    - Calendar
    - Stocks



## How its Run

This program runs on a chron job on a Debian server that according to properties defined in the settings.yml could do one of the following:

    - Download and display a newspaper first thing in the morning
    - Gallery mode, scroll through various comics pages/ random daily arts
    - Show a word of the day 
    - Show WiFi QR Code
    - Show an updating multi function page with the latest weather and calendar / top stocks.




## Appendix

Makes use of https://github.com/janten/dpt-rp1-py python libraries to send commands to the e-paper device


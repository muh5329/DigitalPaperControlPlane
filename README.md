# DigitalPaperControlPlane

Sony Digital Paper control plane . Turns a Sony Digital Paper device into a passive art display/ information display device.




https://github.com/muh5329/DigitalPaperControlPlane/assets/106366024/3de109f4-f922-47b9-97b2-524c941ea079



[![Python](https://img.shields.io/badge/Python-3.12.2-green.svg)](https://www.python.org/)



## Features

- Random daily art ✔️
- NYT or other newspaper [TODO] 
- Comic / Manga Page ✔️ 
- QR Code ✔️
- Word of the day[TODO] 
- Multi Function  [TODO]  
    - Weather
    - Calendar
- Stocks ✔️



## How its Run

This program runs on a chron job on a Debian server that according to properties defined in the settings.yml could do one of the following:

    - Download and display a newspaper first thing in the morning
    - Gallery mode, scroll through various comics pages/ random daily arts
    - Show a word of the day 
    - Show WiFi QR Code
    - Show an updating multi function page with the latest weather and calendar / top stocks.


## Install and runtime 

As a prerequisite , one must register the DPT1 device with your runtime computer via the dpt-rp1-py cli :
    - ```dptrp1 register```

From then on, install the dtp-controll-panel and execute one of the many chron jobs / cli commands
    

## Appendix

Makes use of https://github.com/janten/dpt-rp1-py python libraries to send commands to the e-paper device

Built with Poetry | Typer

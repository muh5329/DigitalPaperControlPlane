# DigitalPaperControlPlane

Sony Digital Paper control plane to show random stuff on a set interval


## Features

- Random daily art / Comic / Manga Page ✔️
- NYT or other newspaper [TODO] 
- QR Code ✔️
- Word of the day[TODO] 
- Multi Function  [TODO]  
    - Weather
    - Calendar
    - Stocks


## Appendix

Makes use of https://github.com/janten/dpt-rp1-py python libraries to send commands to the e-paper device

## Install

Install with 
```
poetry install
```

Test with 
```
dtp-controll-panel
```

## Commands

 !! Device must be registered prior to running commands !!

"""render random"""
- Renders random a random page from a random document

"""upload directory"""
- Uploads all files within a directory to DPT Device
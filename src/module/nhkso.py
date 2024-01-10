import time
import requests
from bs4 import BeautifulSoup


class NHKSO:
    def __init__(self):
        self.url = "https://www.nhkso.or.jp/concert/index.html"
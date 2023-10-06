from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

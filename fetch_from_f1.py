import requests
from bs4 import BeautifulSoup

url = "https://www.formula1.com/en/results/2025/races"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")
row = soup.find_all("tbody")[0]

print(row.text)
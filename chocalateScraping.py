import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


req_response = requests.get(
    "https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
soup = BeautifulSoup(req_response.content, "html.parser")

List = soup.find_all(attrs={"class": 'Rating'})
ratings = []

for rating in List[1:]:
  text = float(rating.get_text())
  ratings.append(text)

plt.hist(ratings)
plt.show()

Names = soup.find_all(attrs={"class": 'Company'})

companyNames = []

for name in Names[1:]:
  companyNames.append(name.get_text())

cocoa_list = soup.find_all(attrs={"class": 'CocoaPercent'})

cocoa_float = []

for cocoa in cocoa_list[1:]:
  cocoa_float.append(float(cocoa.get_text().strip('%')))


dFrame = ({"Company": companyNames, "Ratings": ratings, "CocoaPercentage": cocoa_float})
your_df = pd.DataFrame.from_dict(dFrame)

sorted = your_df.groupby(by="Company").Ratings.mean()
topTen = sorted.nlargest(10)

plt.clf()
plt.scatter(your_df.CocoaPercentage, your_df.Ratings)

z = np.polyfit(your_df.CocoaPercentage, your_df.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(your_df.CocoaPercentage, line_function(your_df.CocoaPercentage), "r--")

plt.show()

import  requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas.core.ops.missing import dispatch_fill_zeros

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

data =[]

for page in range(1,6):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]

        data.append({
            "Title":title,
            "Price":price,
            "Rating":rating
        })

df = pd.DataFrame(data)

df.to_csv("books.csv", index=False)

print("Data saved successfully !")
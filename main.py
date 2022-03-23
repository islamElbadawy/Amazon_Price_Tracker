from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

product_url = "https://www.amazon.com/AMD-Ryzen-5950X-32-Thread-Processor/dp/B0815Y8J9N/ref=sr_1_24?qid=1647664597&s=computers-intl-ship&sr=1-24"

test_mail = 'islamelbadawy21@gmail.com'
test_password = 'treynmufxpcdsuyj'

browser_headers = {
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
}

res = requests.get(url=product_url, headers=browser_headers)

soup = BeautifulSoup(res.text, "lxml")

price = float(soup.find(name="span", class_="apexPriceToPay").getText().split("$")[1])
title = soup.find(name="h1", id="title").getText()


if price <= 670:
    content = f"{title} is now ${price}\n{product_url}"
    with smtplib.SMTP('smtp.gmail.com',587) as conn:
        conn.starttls()
        conn.login(test_mail, test_password)
        conn.sendmail(
            from_addr= test_mail,
            to_addrs= "anascivil7@gmail.com",
            msg= f"Subject:Amazon Price Alert\n\n{content}"
        )



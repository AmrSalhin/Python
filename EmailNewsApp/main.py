import requests
import send_email


apiKey = "9d86746948ca4c5389d4d59f0e19c7ea"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2026-05-10&sortBy=publishedAt&"
       "apiKey=9d86746948ca4c5389d4d59f0e19c7ea")

request = requests.get(url)

content = request.json()

body = ""
for article in content["articles"][:20]:
    body += "subject: Today's News" + "\n" + str(article["title"]) + "\n" + article["url"] + "\n"
    body += str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email.send_email(message=body)

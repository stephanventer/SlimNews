from flask import Flask, render_template
import scrape      
import json

#Define app
app = Flask(__name__)

#Get list of articles
nz_articles = scrape.GetHeraldNZArticles()
#print(nz_articles[0]["title"])

#Define Homepage
@app.route("/")
def home():
    return render_template("index.html", len=len(nz_articles), articles=nz_articles)

#Start app
if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)

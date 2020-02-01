from flask import Flask, send_file

GoldScraper = Flask(__name__)

@GoldScraper.route("/price")
def price():
	return send_file('gold_price.csv', 'text/plain')

if __name__ == "__main__":
	GoldScraper.run()

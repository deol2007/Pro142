from flask import Flask, jsonify
import csv

all_articles = []

with open('shared_articles.csv', encoding='utf-8') as fileObject:
    reader = csv.reader(fileObject)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []
not_read = []

app = Flask(__name__)

@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    })

@app.route("/liked-articles", methods=["POST"])
def liked_article():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/not-liked-articles", methods=["POST"])
def not_liked_article():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(articles)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/did-not-read", methods=["POST"])
def did_not_read():
    articles = all_articles[0]
    all_articles = all_articles[1:]
    not_read.append(articles)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
  app.run()
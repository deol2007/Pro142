from flask import Flask, jsonify
from storage import all_articles, liked_articles, not_liked_articles, not_read
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)

@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        _d = {
            'timestamp':article[0],
            'contentId':article[2],
            'contentType':article[8],
            'url':article[9],
            'title':article[10],
            'lang':article[12],
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200


@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_articles in liked_articles:
        output = get_recommendations(liked_articles[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            'timestamp':recommended[0],
            'contentId':recommended[2],
            'contentType':recommended[8],
            'url':recommended[9],
            'title':recommended[10],
            'lang':recommended[12],
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
  app.run()
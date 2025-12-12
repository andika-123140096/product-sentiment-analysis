from pyramid.view import view_config
from datetime import datetime
from transformers import pipeline
from google import genai
import os
from dotenv import load_dotenv
from .. import models

load_dotenv()

sentiment_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def analyze_sentiment(text):
    result = sentiment_analyzer(text)[0]
    return result['label'].lower()

def extract_key_points(text):
    try:
        prompt = f"Extract key points from this product review: {text}"
        response = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
        return response.text
    except Exception as e:
        return f"Error extracting key points: {str(e)}"

def create_review(review_text, sentiment, key_points, dbsession):
    review = models.Review(
        review_text=review_text,
        sentiment=sentiment,
        key_points=key_points,
        created_at=datetime.utcnow()
    )
    dbsession.add(review)
    dbsession.flush()
    return review
@view_config(route_name='analyze_review', request_method='OPTIONS', renderer='json')
def analyze_review_options(request):
    response = request.response
    response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    })
    return {}

@view_config(route_name='analyze_review', request_method='POST', renderer='json')
def analyze_review(request):
    response = request.response
    response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    })
    try:
        data = request.json_body
        review_text = data.get('review_text', '').strip()
        if not review_text:
            return {'error': 'Review text is required'}

        sentiment = analyze_sentiment(review_text)
        key_points = extract_key_points(review_text)
        review = create_review(review_text, sentiment, key_points, request.dbsession)

        return {
            'id': review.id,
            'review_text': review_text,
            'sentiment': sentiment,
            'key_points': key_points,
            'created_at': review.created_at.isoformat()
        }
    except Exception as e:
        return {'error': str(e)}

@view_config(route_name='get_reviews', request_method='OPTIONS', renderer='json')
def get_reviews_options(request):
    response = request.response
    response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    })
    return {}

@view_config(route_name='get_reviews', request_method='GET', renderer='json')
def get_reviews(request):
    response = request.response
    response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    })
    try:
        query = request.dbsession.query(models.Review).order_by(models.Review.created_at.desc())
        reviews = query.all()
        result = []
        for review in reviews:
            result.append({
                'id': review.id,
                'review_text': review.review_text,
                'sentiment': review.sentiment,
                'key_points': review.key_points,
                'created_at': review.created_at.isoformat() if review.created_at else None
            })
        return result
    except Exception as e:
        return {'error': str(e)}
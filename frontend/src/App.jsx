import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [reviewText, setReviewText] = useState('')
  const [reviews, setReviews] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    fetchReviews()
  }, [])

  const fetchReviews = async () => {
    try {
      const response = await fetch('http://localhost:6543/api/reviews')
      if (!response.ok) throw new Error('Failed to fetch reviews')
      const data = await response.json()
      setReviews(data)
    } catch (err) {
      setError(err.message)
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!reviewText.trim()) return

    setLoading(true)
    setError('')
    try {
      const response = await fetch('http://localhost:6543/api/analyze-review', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ review_text: reviewText }),
      })
      if (!response.ok) throw new Error('Failed to analyze review')
      const newReview = await response.json()
      setReviews([newReview, ...reviews])
      setReviewText('')
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <h1>Product Review Analyzer</h1>
      <form onSubmit={handleSubmit} className="review-form">
        <textarea
          value={reviewText}
          onChange={(e) => setReviewText(e.target.value)}
          placeholder="Enter your product review here..."
          rows="4"
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Analyzing...' : 'Analyze Review'}
        </button>
      </form>
      {error && <p className="error">{error}</p>}
      <div className="reviews">
        <h2>Reviews</h2>
        {reviews.length === 0 ? (
          <p>No reviews yet.</p>
        ) : (
          reviews.map((review) => (
            <div key={review.id} className="review-card">
              <p className="review-text">{review.review_text}</p>
              <p className="sentiment">Sentiment: <span className={`sentiment-${review.sentiment}`}>{review.sentiment}</span></p>
              <p className="key-points">Key Points: {review.key_points}</p>
              <p className="date">{new Date(review.created_at).toLocaleString()}</p>
            </div>
          ))
        )}
      </div>
    </div>
  )
}

export default App

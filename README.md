# Product Review Analyzer

### Nama: Andika Dinata
### NIM: 123140096
### Kelas: RA

A web application for analyzing product reviews using sentiment analysis and key point extraction.

## Features

- **Sentiment Analysis**: Automatically analyzes the sentiment of product reviews (positive, negative, neutral) using a pre-trained transformer model.
- **Key Points Extraction**: Extracts key points from reviews using Google's Gemini AI.
- **Review Storage**: Stores reviews in a SQLite database with timestamps.
- **Web Interface**: User-friendly React frontend for submitting and viewing reviews.
- **API Endpoints**: RESTful API for programmatic access.

## Technologies Used

### Backend
- **Python**: Core programming language
- **Pyramid**: Web framework
- **SQLAlchemy**: ORM for database interactions
- **Transformers**: For sentiment analysis (cardiffnlp/twitter-roberta-base-sentiment-latest)
- **Google Generative AI**: For key points extraction
- **Alembic**: Database migrations
- **Waitress**: WSGI server

### Frontend
- **React**: JavaScript library for building user interfaces
- **Vite**: Build tool and development server
- **ESLint**: Code linting

### Database
- **SQLite**: Lightweight database for development and production

## Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Backend Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd product_review_analyzer
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```

3. Install Python dependencies:
   ```bash
   pip install -e .
   ```

4. Set up the database:
   ```bash
   initialize_product_review_analyzer_db development.ini
   ```

5. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Add your Gemini API key: `GEMINI_API_KEY=your_api_key_here`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

## Usage

### Running the Application

1. Start the backend server:
   ```bash
   pserve development.ini
   ```
   The backend will run on http://localhost:6543

2. Start the frontend development server:
   ```bash
   cd frontend
   npm run dev
   ```
   The frontend will run on http://localhost:5173

3. Open your browser and navigate to http://localhost:5173 to use the application.

### API Endpoints

- `GET /api/reviews`: Retrieve all reviews
- `POST /api/analyze-review`: Analyze a new review
  - Body: `{"review_text": "Your review text here"}`
  - Returns: Review data with sentiment and key points
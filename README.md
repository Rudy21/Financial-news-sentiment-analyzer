📊 Financial News Sentiment Analyzer
This project is a Streamlit web app that performs sentiment analysis on financial news headlines using the pre-trained FinBERT model.

🔍 Features
Upload a CSV file containing financial news headlines.

Automatically analyzes each headline's sentiment (Positive, Neutral, Negative).

Displays a data table and a sentiment distribution bar chart.

Built using Python, Hugging Face Transformers, and Streamlit.

🧠 How It Works
Uses FinBERT — a BERT model fine-tuned for financial sentiment analysis.

Takes a list of headlines and classifies each into one of three sentiment classes.

Visualizes sentiment counts using Streamlit’s built-in charting tools.

📁 Project Structure
bash
Copy
Edit
.
├── app.py                # Streamlit app UI and logic
├── sentiment_model.py    # FinBERT model loading and sentiment function
🗂️ Input Format
Upload a .csv file with a column titled headline.
Example:

csv
Copy
Edit
headline
"Apple beats Q2 earnings expectations"
"Tesla stock falls after Elon Musk's statement"
"Federal Reserve keeps interest rates unchanged"
🚀 Getting Started
Install dependencies

bash
Copy
Edit
pip install streamlit transformers pandas
Run the app

bash
Copy
Edit
streamlit run app.py
Open in browser
Visit http://localhost:8501 to use the app.

✅ Example Output
Dataframe with headline and corresponding sentiment.

Bar chart showing count of Positive / Neutral / Negative headlines.

🧪 Future Improvements
Add real-time news scraping from financial sources.

Include VADER or custom-trained models for comparison.

Add sentiment scoring and polarity visualization.

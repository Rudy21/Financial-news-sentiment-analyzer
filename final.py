# -*- coding: utf-8 -*-
"""Final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yxpDrzpBPP_DGMC0Gxnwy0ZqLIXokrcl
"""

!pip install -q streamlit pyngrok transformers pandas

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pandas as pd
# from transformers import pipeline
# 
# st.title("Financial News Sentiment Analyzer")
# 
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
# 
# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.write("Uploaded Data Preview:")
#     st.dataframe(df.head())
# 
#     if "headline" in df.columns:
#         nlp = pipeline("sentiment-analysis", model="ProsusAI/finbert")
#         st.info("Analyzing sentiment...")
#         results = nlp(df["headline"].tolist())
#         df["sentiment"] = [r["label"] for r in results]
#         st.success("Sentiment analysis complete!")
#         st.dataframe(df)
#     else:
#         st.error("The CSV must contain a column named 'headline'.")

!ngrok config add-authtoken 2yVDomBX9OB1HYmt1iwcHx0Sort_3XxcoDueTkTqWEc2KkGQc

from pyngrok import ngrok
import threading
import os
import time

ngrok.kill()

def start_streamlit():
    os.system("streamlit run app.py")

thread = threading.Thread(target=start_streamlit)
thread.start()

time.sleep(5)

public_url = ngrok.connect(8501)
print(f"Your Streamlit app is live at: {public_url}")


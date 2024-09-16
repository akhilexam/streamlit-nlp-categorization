#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:55:31 2024

@author: akhil.gupta
"""
import streamlit as st
import pandas as pd
import spacy

# Load spaCy's pre-trained model
nlp = spacy.load('en_core_web_md')

# Define the categories and their descriptions
categories = {
    "Office Supplies": "Items such as pencils, pens, notepads, erasers, and office furniture like desks and chairs.",
    "IT Services": "Services related to IT including cloud hosting, software licenses, and IT infrastructure.",
    "Travel": "Expenses related to business travel, including flights, hotels, and transportation.",
    "Marketing": "Advertising and promotional services, including social media ads, Google Ads, and campaigns.",
    "Utilities": "Utility bills including electricity, water, and other essential services.",
    "Cleaning Services": "Services related to cleaning, janitorial work, and maintenance of office spaces."
}

# Function to categorize each row based on the description and items using NLP
def categorize_with_nlp(description, items):
    combined_text = f"{description} {items}".lower()
    doc = nlp(combined_text)
    best_category = "Uncategorized"
    best_similarity = -1
    
    for category, category_description in categories.items():
        category_doc = nlp(category_description.lower())
        similarity = doc.similarity(category_doc)
        if similarity > best_similarity:
            best_similarity = similarity
            best_category = category
    
    return best_category

# Streamlit app
st.title("Indirect Spend Categorization")

# File uploader widget
uploaded_file = st.file_uploader("Upload your spend CSV file", type="csv")

# If a file is uploaded, process it
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if 'Description' in df.columns and 'Items' in df.columns:
        df['Category'] = df.apply(lambda row: categorize_with_nlp(row['Description'], row['Items']), axis=1)
        st.subheader("Categorized Spend Data")
        st.write(df)
        
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download categorized data as CSV",
            data=csv,
            file_name="categorized_indirect_spend.csv",
            mime="text/csv"
        )
    else:
        st.error("The uploaded file must contain 'Description' and 'Items' columns.")

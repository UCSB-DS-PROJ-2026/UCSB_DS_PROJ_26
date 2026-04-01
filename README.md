# Santa Barbara Housing Cost Predictor

A machine learning web app that predicts rental prices for apartments and houses in Isla Vista and Goleta, CA — built to help UCSB students navigate one of California's most competitive rental markets.

## Overview

This project builds an end-to-end rent prediction pipeline using real listing data scraped from Zillow, Craigslist, and Apartments.com. The model takes property features as input and outputs an estimated monthly rent, surfaced through an interactive Streamlit app.

**Current model performance:** Cross-validated R² ~0.60 (10-feature linear regression)

## Features

- Scraped and cleaned ~120 rental listings across Isla Vista and Goleta
- Engineered features from listing text, including NLP-extracted amenity flags (parking, laundry, pets, etc.)
- Geocoded listings and calculated distance to UCSB using geopy
- Iterated from a baseline model (CV R² ~0.56) to an improved 10-feature model (CV R² ~0.60)
- Interactive Streamlit frontend for student use

## Tech Stack

`Python` `scikit-learn` `pandas` `Streamlit` `geopy` `Jupyter`

## Project Structure
```
UCSB-DS-PROJ-2026/
├── notebooks/        # EDA, feature engineering, and modeling
├── requirements.txt  # Dependencies
└── README.md
```

## Getting Started
```bash
git clone https://github.com/AnikaAchary/UCSB-DS-PROJ-2026.git
cd UCSB-DS-PROJ-2026
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Status

🚧 In progress — actively expanding dataset and improving model performance.

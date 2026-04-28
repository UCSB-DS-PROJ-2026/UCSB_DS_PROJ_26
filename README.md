# SB Housing Intelligence 🏠
## Overview
SB Housing Intelligence is a data-driven web platform designed to help UCSB students navigate the expensive and competitive housing market in Santa Barbara. Off-campus housing in areas like Isla Vista and Goleta is often limited, expensive, and difficult to predict, leaving students with little time or information to make informed financial decisions.

This project aims to improve transparency in the rental market by combining real housing data with predictive modeling and interactive tools.

## Problem Statement:

Students in Santa Barbara face significant challenges in finding affordable and reliable   housing due to:

     1. Limited rental availability near UCSB

     2. High increase in demand each academic year

     3. Lack of transparency and centralized pricing information

## Solution
To address this issue, we are developing a web-based platform that:

     •  Predicts Future housing prices in Santa Barbara 

     •  Displays current rental listings and housing trends

     •  Provides student-focused information such as the number of rooms/bathrooms, rent price,            distance from UCSB, and more to help students make informed financial decisions. 

## Methodology

### Data Collection

We gathered housing data from: 

    •  Zillow

    •  Redfin

    •  UCSB housing listings website and public rental data sources

### Data Processing:

    •  Data cleaning using pandas in Python

    •  Handling missing values and standardizing features

    •  Feature engineering (calculating distance to UCSB, price per room, etc)

### Machine Learning Model:

• Model Types: 

    •  Decision Trees (Gradient boosting) 

•  Input Features: 

    •  Location 
    
    •  Number of bedrooms and bathrooms
    
    •  Distance to UCSB 

    •  Rent prices 

•  Output:

    •  Predicted future rental price 



## Features

    •  AI Chat Explorer for housing-related questions

    •  Housing price prediction model

    •  Trends and data visualizations

    •  Student-focused rental insights (distance, size, affordability)
    

## Data Sources

   •   UCSB Housing Listings Website

   •   Red Fin

   •   Zillow

   •   Additional public rental datasets 


## Tech Stack

   •    Python (pandas, scikit-learn)

   •    Jupyter Notebook

   •    Github

   •    Streamlit Community Cloud

   •    Python, scikit-learn, pandas
   
   •    OpenRouteService API

# Amazon Review Sentiment Analysis

## Overview

This project focuses on sentiment analysis using machine learning and natural language processing techniques. The goal is to develop a Streamlit app capable of analyzing sentiments in various scenarios, including single-line reviews, multiple reviews from CSV files, and product reviews from Amazon URLs.

## Project Structure

- **notebooks**: Contains Jupyter notebooks with exploratory data analysis and model development.
- **reviewscrapper.py**: Includes Python scripts for web scraping reviews for a certain URL.
- **scrappedReviews.csv**: The reviews scrapped by "reviewscrapper.py" gets stored here.
- **multiple_review_test.csv**: Test file to test out sentiment analysis for multiple reviews.
- **review_analyzer.py**: Houses the Streamlit app code for interactive sentiment analysis.
- **models.p**: Stores serialized models for sentiment analysis.
- **requirements.txt**: Lists the project dependencies for reproducibility.
- **config.toml**: Configuration for the Streamlit app theme.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/amri-tah/Amazon-Review-Sentiment-Analysis.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Amazon-Review-Sentiment-Analysis
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Open terminal and run the Streamlit app:
    ```bash
    streamlit run review_analyzer.py
    ```

## Usage

1. Explore and run Jupyter notebook `B8_Amazon.ipynb` in the `notebooks` folder for data analysis and model development.

2. Execute Python scripts in the `reviewscrapper.py` for web scraping.

3. Run the Streamlit app for interactive sentiment analysis:

    ```bash
    streamlit run review_analyzer.py
    ```




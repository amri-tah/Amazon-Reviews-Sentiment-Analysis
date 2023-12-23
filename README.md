# Amazon Review Sentiment Analysis

## Overview

This project focuses on sentiment analysis using machine learning and natural language processing techniques. The goal is to develop a Streamlit app capable of analyzing sentiments in various scenarios, including single-line reviews, multiple reviews from CSV files, and product reviews from Amazon URLs.

## Project Structure

- **notebooks**: Contains Jupyter notebooks with exploratory data analysis and model development.
- **test files**: Contains test files to test out sentiment analysis for multiple reviews.
- **models.p**: Stores serialized models for sentiment analysis.
- **review_analyzer.py**: Houses the Streamlit app code for interactive sentiment analysis.
- **reviewscrapper.py**: Includes Python scripts for web scraping reviews for a certain URL.
- **scrappedReviews.csv**: The reviews scrapped by "reviewscrapper.py" gets stored here.
- **requirements.txt**: Lists the project dependencies for reproducibility.
- **.streamlit**: Contains the configuration for the streamlit app's theme
  
## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/amri-tah/Amazon-Reviews-Sentiment-Analysis.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Amazon-Review-Sentiments-Analysis
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

## Screenshots

### Amazon Reviews Dataset Word Cloud:
![](screenshots/wordcloud.png)

### Data Analysis:
![](screenshots/no-of-chars.jpg)
![](screenshots/no-of-words.jpg)

### Streamlit App:
#### Single Reviews:
![](screenshots/single-review.jpg)

#### Product URL Reviews:
![](screenshots/url-review-1.jpg)
![](screenshots/url-review-2.jpg)

#### Multi Review:
![](screenshots/multi-review-1.jpg)
![](screenshots/multi-review-2.jpg)

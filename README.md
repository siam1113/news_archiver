# News Archiver

A Python tool that scrapes news articles and archives them into a DynamoDB table for later reference.

## How it works

- `scraper/scraper.py` — fetches news articles from a source (for example, bdnews24)
- `main.py` — writes scraped article data (title, link, source, thumbnail) into a DynamoDB table named `news_archive`
- `database/schema.py` — defines the structure of the archived data

## Requirements

- An AWS account with DynamoDB access configured
- Python packages listed in `requirements.txt`

## Usage

```bash
pip install -r requirements.txt
python main.py
```

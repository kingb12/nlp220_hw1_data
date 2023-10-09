# NLP 220: Assignment 1 Data

This repository holds the data for assignment 1 in NLP 220, as well as code for reproducing it (not needed for assignment completion).

## Getting Data for Assignment 1

On Mac/Linux (e.g. `nlp-gpu-01`):
```bash
wget "https://raw.githubusercontent.com/kingb12/nlp220_hw1_data/main/small_books_rating.csv"
```

On Windows:

Unable to test myself, but [Wget for Windows](https://eternallybored.org/misc/wget/) looks useful and would result in the same command as above once installed. Some more options [discussed here](https://superuser.com/questions/25538/how-to-download-files-from-command-line-in-windows-like-wget-or-curl).

## (Optional) Full Dataset Download Instructions

To reproduce, do the following, and then run `python create_dataset.py`.

1. Sign up for a [Kaggle](https://www.kaggle.com/) account
2. Set up an API token in your profile
3. Move the API token (provided in `kaggle.json`) to your working computer (could be `nlp-gpu-01`) under `~/.kaggle`.
4. In your assignment environment: `pip install kaggle`
5. `kaggle datasets download -d mohamedbakhet/amazon-books-reviews`
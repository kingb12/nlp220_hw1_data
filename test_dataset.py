import unittest
import pandas as pd

from create_dataset import COUNT_PER_REVIEW_SCORE

class TestDataFrame(unittest.TestCase):

    def setUp(self):
        # Assuming you're reading the DataFrame from a CSV for this example
        self.df = pd.read_csv('small_books_rating.csv')

    def test_unique_review_score_counts(self):
        unique_scores = self.df['review/score'].unique()

        for score in unique_scores:
            count = len(self.df[self.df['review/score'] == score])
            self.assertEqual(count, COUNT_PER_REVIEW_SCORE, f"Expected {COUNT_PER_REVIEW_SCORE} rows for review/score {score}, but got {count} rows.")

if __name__ == '__main__':
    unittest.main()

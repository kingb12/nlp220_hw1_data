
from collections import Counter
import csv

from tqdm import tqdm

COUNT_PER_REVIEW_SCORE: int = 5_000


if __name__ == '__main__':
    with open('Books_rating.csv', 'r') as f:
        reader: csv.DictReader = csv.DictReader(f)
        scores: Counter[int] = Counter()
        with open('small_books_rating.csv', 'w') as out_f:
            writer = csv.DictWriter(out_f, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in tqdm(reader, desc="filtering dataset"):
                score: int = row['review/score']
                if scores[score] >= COUNT_PER_REVIEW_SCORE:
                    continue
                else:
                    scores[score] += 1
                    writer.writerow(row)
                    if all(v >= COUNT_PER_REVIEW_SCORE for v in scores.values()):
                        print(f"Finished filtering: there should be {COUNT_PER_REVIEW_SCORE} items per review/score in small_books_rating.csv")
                        break

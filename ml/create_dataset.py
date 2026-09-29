import os
import random
import pandas as pd


random.seed(42)


FRUIT_PROFILES = {
    "Apple": {
        "weight": (120, 220),
        "size": (6, 9),
        "sweetness": (55, 85),
        "acidity": (35, 65),
        "firmness": (65, 90),
        "ripeness": (65, 95),
        "color_score": (60, 95),
        "diameter": (6, 9),
        "height": (5, 9),
        "width": (6, 9),
    },

    "Banana": {
        "weight": (80, 180),
        "size": (12, 22),
        "sweetness": (65, 95),
        "acidity": (10, 35),
        "firmness": (35, 70),
        "ripeness": (55, 95),
        "color_score": (55, 90),
        "diameter": (3, 5),
        "height": (12, 22),
        "width": (3, 5),
    },

    "Mango": {
        "weight": (150, 400),
        "size": (8, 15),
        "sweetness": (65, 95),
        "acidity": (15, 45),
        "firmness": (40, 75),
        "ripeness": (55, 95),
        "color_score": (55, 95),
        "diameter": (7, 12),
        "height": (8, 15),
        "width": (6, 11),
    },

    "Orange": {
        "weight": (100, 250),
        "size": (6, 10),
        "sweetness": (45, 80),
        "acidity": (40, 75),
        "firmness": (55, 85),
        "ripeness": (60, 95),
        "color_score": (70, 100),
        "diameter": (6, 10),
        "height": (6, 10),
        "width": (6, 10),
    },

    "Strawberry": {
        "weight": (10, 40),
        "size": (3, 7),
        "sweetness": (55, 90),
        "acidity": (25, 60),
        "firmness": (25, 65),
        "ripeness": (55, 95),
        "color_score": (65, 100),
        "diameter": (2, 5),
        "height": (3, 7),
        "width": (2, 5),
    },
}


rows = []


for fruit, profile in FRUIT_PROFILES.items():

    for _ in range(100):

        row = {
            "Weight": round(random.uniform(*profile["weight"]), 2),
            "Size": round(random.uniform(*profile["size"]), 2),
            "Sweetness": round(random.uniform(*profile["sweetness"]), 2),
            "Acidity": round(random.uniform(*profile["acidity"]), 2),
            "Firmness": round(random.uniform(*profile["firmness"]), 2),
            "Ripeness": round(random.uniform(*profile["ripeness"]), 2),
            "Color_Score": round(random.uniform(*profile["color_score"]), 2),
            "Diameter": round(random.uniform(*profile["diameter"]), 2),
            "Height": round(random.uniform(*profile["height"]), 2),
            "Width": round(random.uniform(*profile["width"]), 2),
            "Fruit": fruit,
        }

        rows.append(row)


df = pd.DataFrame(rows)

output_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "dataset",
    "fruit_detection_dataset.csv"
)

df.to_csv(output_path, index=False)

print("Dataset created successfully!")
print(f"Location: {output_path}")
print(f"Total records: {len(df)}")
print("\nFruit distribution:")
print(df["Fruit"].value_counts())
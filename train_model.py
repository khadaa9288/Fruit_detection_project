import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# ==========================================================
# PROJECT PATH
# ==========================================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# ==========================================================
# DATASET PATH
# ==========================================================

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "fruit_detection_dataset_500.csv"
)


# ==========================================================
# MODEL PATH
# ==========================================================

MODEL_DIR = os.path.join(
    BASE_DIR,
    "prediction"
)

os.makedirs(
    MODEL_DIR,
    exist_ok=True
)


MODEL_PATH = os.path.join(
    MODEL_DIR,
    "fruit_detection_model.pkl"
)


# ==========================================================
# START
# ==========================================================

print("\n======================================")
print("FRUIT DETECTION MODEL TRAINING")
print("======================================")


# ==========================================================
# CHECK DATASET
# ==========================================================

if not os.path.exists(DATASET_PATH):

    raise FileNotFoundError(
        f"\nDataset not found:\n{DATASET_PATH}"
    )


# ==========================================================
# LOAD DATASET
# ==========================================================

print("\nLoading dataset...")

df = pd.read_csv(
    DATASET_PATH
)


print("\nDataset loaded successfully!")

print(
    "Rows:",
    len(df)
)

print(
    "Columns:",
    len(df.columns)
)


# ==========================================================
# CLEAN COLUMN NAMES
# ==========================================================

df.columns = (
    df.columns
    .str.strip()
    .str.replace("**", "", regex=False)
)


# ==========================================================
# DISPLAY COLUMNS
# ==========================================================

print("\nDataset columns:")

for column in df.columns:

    print(
        "-",
        column
    )


# ==========================================================
# FEATURES
# ==========================================================

features = [

    "Fruit_Size",

    "Fruit_Weight",

    "Fruit_Width",

    "Fruit_Height",

    "Fruit_Color",

    "Fruit_Texture",

    "Sweetness",

    "Acidity",

    "Ripeness"

]


# ==========================================================
# TARGET
# ==========================================================

target = "Fruit"


# ==========================================================
# CHECK REQUIRED COLUMNS
# ==========================================================

required_columns = (
    features +
    [target]
)


missing_columns = [

    column

    for column in required_columns

    if column not in df.columns

]


if missing_columns:

    print("\n======================================")
    print("ERROR: MISSING DATASET COLUMNS")
    print("======================================")

    for column in missing_columns:

        print(
            "-",
            column
        )

    print("\nAvailable columns:")

    for column in df.columns:

        print(
            "-",
            column
        )

    raise ValueError(
        "\nDataset columns do not match "
        "the expected columns."
    )


# ==========================================================
# REMOVE EMPTY RECORDS
# ==========================================================

df = df.dropna(
    subset=required_columns
).copy()


# ==========================================================
# DISPLAY FRUIT CLASSES
# ==========================================================

print("\nFruit classes:")

print(
    df[target].value_counts()
)


# ==========================================================
# INPUT / TARGET
# ==========================================================

X = df[features]

y = df[target]


# ==========================================================
# CATEGORICAL FEATURES
# ==========================================================

categorical_features = [

    "Fruit_Color",

    "Fruit_Texture",

    "Ripeness"

]


# ==========================================================
# NUMERICAL FEATURES
# ==========================================================

numerical_features = [

    "Fruit_Size",

    "Fruit_Weight",

    "Fruit_Width",

    "Fruit_Height",

    "Sweetness",

    "Acidity"

]


# ==========================================================
# PREPROCESSOR
# ==========================================================

preprocessor = ColumnTransformer(

    transformers=[

        (
            "categorical",

            OneHotEncoder(
                handle_unknown="ignore"
            ),

            categorical_features
        ),

        (
            "numerical",

            "passthrough",

            numerical_features
        )

    ]

)


# ==========================================================
# RANDOM FOREST
# ==========================================================

classifier = RandomForestClassifier(

    n_estimators=200,

    random_state=42,

    n_jobs=-1

)


# ==========================================================
# PIPELINE
# ==========================================================

pipeline = Pipeline(

    steps=[

        (
            "preprocessor",

            preprocessor
        ),

        (
            "classifier",

            classifier
        )

    ]

)


# ==========================================================
# TRAIN / TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)


print(
    "\nTraining records:",
    len(X_train)
)

print(
    "Testing records:",
    len(X_test)
)


# ==========================================================
# TRAIN
# ==========================================================

print(
    "\nTraining Random Forest model..."
)


pipeline.fit(

    X_train,

    y_train

)


# ==========================================================
# PREDICTION
# ==========================================================

y_pred = pipeline.predict(
    X_test
)


# ==========================================================
# ACCURACY
# ==========================================================

accuracy = accuracy_score(

    y_test,

    y_pred

)


print("\n======================================")
print("MODEL TRAINING COMPLETED")
print("======================================")


print(
    f"\nAccuracy: {accuracy * 100:.2f}%"
)


# ==========================================================
# CLASSIFICATION REPORT
# ==========================================================

print(
    "\nClassification Report:"
)


print(

    classification_report(

        y_test,

        y_pred

    )

)


# ==========================================================
# SAVE MODEL
# ==========================================================

joblib.dump(

    pipeline,

    MODEL_PATH

)


# ==========================================================
# SUCCESS
# ==========================================================

print("\n======================================")
print("MODEL SAVED SUCCESSFULLY")
print("======================================")


print(
    "\nModel location:"
)


print(
    MODEL_PATH
)


print(
    "\nTraining completed successfully!"
)
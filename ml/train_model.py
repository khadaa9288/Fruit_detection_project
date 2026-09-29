import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report


# ==============================
# Project paths
# ==============================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "fruit_detection_dataset.csv"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "prediction"
)

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "fruit_detection_model.pkl"
)

ENCODER_PATH = os.path.join(
    MODEL_DIR,
    "fruit_label_encoder.pkl"
)


# ==============================
# Load dataset
# ==============================

print("Loading dataset...")

df = pd.read_csv(DATASET_PATH)

print(f"Dataset loaded successfully!")
print(f"Total records: {len(df)}")


# ==============================
# Display columns
# ==============================

print("\nDataset columns:")
print(df.columns.tolist())


# ==============================
# Target column
# ==============================

target_column = "Fruit"


# ==============================
# Features
# ==============================

X = df.drop(columns=[target_column])
y = df[target_column]


# ==============================
# Encode target labels
# ==============================

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)


# ==============================
# Train/Test Split
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.20,
    random_state=42,
    stratify=y_encoded
)


print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# ==============================
# Random Forest Model
# ==============================

print("\nTraining Random Forest model...")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    max_depth=None
)

model.fit(X_train, y_train)


# ==============================
# Model Evaluation
# ==============================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n================================")
print("MODEL TRAINING COMPLETED")
print("================================")

print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=label_encoder.classes_
    )
)


# ==============================
# Create prediction directory
# ==============================

os.makedirs(MODEL_DIR, exist_ok=True)


# ==============================
# Save model
# ==============================

joblib.dump(model, MODEL_PATH)

print("\nModel saved successfully!")
print(f"Model location: {MODEL_PATH}")


# ==============================
# Save label encoder
# ==============================

joblib.dump(label_encoder, ENCODER_PATH)

print("Label encoder saved successfully!")
print(f"Encoder location: {ENCODER_PATH}")


# ==============================
# Feature importance
# ==============================

print("\nFeature Importance:")

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance.to_string(index=False))

print("\nStep 7 completed successfully!")
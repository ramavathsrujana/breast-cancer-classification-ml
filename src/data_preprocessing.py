Added data preprocessing module

📌 Purpose
- Load dataset
- Clean data
- Encode labels
- Scale features
- Split train & test data

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def load_and_preprocess_data(csv_path):
    df = pd.read_csv(csv_path)

    # Drop ID column if present
    if 'id' in df.columns:
        df.drop('id', axis=1, inplace=True)

    # Encode diagnosis column
    le = LabelEncoder()
    df['diagnosis'] = le.fit_transform(df['diagnosis'])

    X = df.drop('diagnosis', axis=1)
    y = df['diagnosis']

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.25, random_state=42
    )

    return X_train, X_test, y_train, y_test



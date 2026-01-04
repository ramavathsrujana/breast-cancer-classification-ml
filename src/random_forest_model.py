Added Random Forest model training code

📌 Purpose
- Train Random Forest
- Compare with SVM

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_random_forest(X_train, X_test, y_train, y_test):
    rf_model = RandomForestClassifier(
        n_estimators=100, random_state=42
    )
    rf_model.fit(X_train, y_train)

    y_pred = rf_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return rf_model, accuracy

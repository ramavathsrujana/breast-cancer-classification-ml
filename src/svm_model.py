Added SVM model training code

📌 Purpose
- Train SVM model
- Predict results
- Return accuracy

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def train_svm(X_train, X_test, y_train, y_test):
    svm_model = SVC(kernel='linear', probability=True)
    svm_model.fit(X_train, y_train)

    y_pred = svm_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return svm_model, accuracy

Added evaluation and visualization code

📌 Purpose
- Generate confusion matrices
- Plot accuracy comparison

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(title)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

def plot_accuracy_comparison(svm_acc, rf_acc):
    models = ['SVM', 'Random Forest']
    accuracies = [svm_acc, rf_acc]

    plt.bar(models, accuracies)
    plt.ylabel('Accuracy')
    plt.title('Accuracy Comparison')
    plt.show()

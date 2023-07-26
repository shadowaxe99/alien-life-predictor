```python
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def evaluate_model(model, processed_data, predictions):
    # Split the processed data into features and target
    X = processed_data.drop('alien_life', axis=1)
    y = processed_data['alien_life']

    # Use the model to make predictions
    y_pred = model.predict(X)

    # Calculate the accuracy of the model
    accuracy = accuracy_score(y, y_pred)
    print(f"Model Accuracy: {accuracy}")

    # Create a confusion matrix
    cm = confusion_matrix(y, y_pred)

    # Visualize the confusion matrix
    plt.figure(figsize=(10,7))
    sns.heatmap(cm, annot=True, fmt='d')
    plt.xlabel('Predicted')
    plt.ylabel('Truth')
    plt.show()

    # Save the predictions to a variable
    predictions = y_pred

    # Return the accuracy and predictions
    return accuracy, predictions
```
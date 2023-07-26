```python
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint

# Load preprocessed data
from data_collection.data_preprocessing import processed_data

# Load the model architecture
from machine_learning.model_development import model

def train_model(processed_data, model):
    # Split the data into training and validation sets
    train_data, validation_data = processed_data.random_split([0.8, 0.2])

    # Define the model checkpoint
    checkpoint = ModelCheckpoint('model.h5', monitor='val_loss', save_best_only=True)

    # Train the model
    history = model.fit(
        train_data,
        validation_data=validation_data,
        epochs=100,
        callbacks=[checkpoint]
    )

    return model, history

model, history = train_model(processed_data, model)

# Export the trained model
with open('machine_learning/trained_model.pkl', 'wb') as f:
    pickle.dump(model, f)
```
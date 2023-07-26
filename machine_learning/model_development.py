```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def develop_model(processed_data):
    # Define the model architecture
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=[len(processed_data.keys())]),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])

    # Compile the model
    model.compile(
        loss='mean_absolute_error',
        optimizer=tf.keras.optimizers.Adam(0.001),
        metrics=['mae', 'mse']
    )

    return model
```
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# AND gate dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)  # Inputs
y = np.array([[0, 0],  # AND: 0, OR: 0
              [0, 1],  # AND: 0, OR: 1
              [0, 1],  # AND: 0, OR: 1
              [1, 1]], dtype=np.float32) 

# Create a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(2,)),  # More neurons in hidden layer
    tf.keras.layers.Dense(4, activation='relu'),  # Additional hidden layer
    tf.keras.layers.Dense(2, activation='sigmoid')  # Output layer (binary classification)
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X, y, epochs=10, verbose=0,validation_data=(X, y))  # Training for 500 epochs

"""
# Plot training loss and accuracy
plt.figure(figsize=(12, 5))

# Loss plot
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Loss over Epochs')
plt.legend()
plt.grid()

# Accuracy plot
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy', color='green')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Accuracy over Epochs')
plt.legend()
plt.grid()

# Show the plots
plt.show()
        
"""
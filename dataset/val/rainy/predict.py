import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# -----------------------------
# Load model
# -----------------------------
model = load_model("weather_model.h5")

# -----------------------------
# Class labels (must match training order)
# -----------------------------
class_labels = ["cloudy", "rainy", "shine", "sunrise"]

# -----------------------------
# Input image
# -----------------------------
img_path = input("Enter image path: ").strip().strip('"')

if not os.path.exists(img_path):
    raise FileNotFoundError("Image not found! Please check path.")

# -----------------------------
# Load image
# -----------------------------
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

# -----------------------------
# Prediction
# -----------------------------
pred = model.predict(img_array)[0]

pred_index = np.argmax(pred)
pred_label = class_labels[pred_index]
confidence = pred[pred_index]

# -----------------------------
# Print results
# -----------------------------
print("\n=========================")
print("🌤 WEATHER PREDICTION")
print("=========================")

for i, label in enumerate(class_labels):
    print(f"{label}: {pred[i]*100:.2f}%")

print("-------------------------")
print(" Final Prediction:", pred_label)
print(" Confidence:", f"{confidence*100:.2f}%")
print("=========================\n")


plt.figure(figsize=(5,5))
plt.imshow(img)
plt.axis("off")
plt.title(f"{pred_label} ({confidence*100:.2f}%)")
plt.show()
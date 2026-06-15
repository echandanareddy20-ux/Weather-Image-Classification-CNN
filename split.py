import os
import shutil
import random

# ✅ SOURCE (original dataset)
source_dir = "C:/Users/E Chandana Reddy/Downloads/archive/dataset2"

# ✅ DESTINATION (NEW dataset folder)
base_dir = "C:/Users/E Chandana Reddy/OneDrive/Desktop/weather image project/dataset"
train_dir = os.path.join(base_dir, "train")
val_dir = os.path.join(base_dir, "val")

classes = ["cloudy", "rainy", "sunrise", "shine"]

for cls in classes:
    os.makedirs(os.path.join(train_dir, cls), exist_ok=True)
    os.makedirs(os.path.join(val_dir, cls), exist_ok=True)

    files = os.listdir(os.path.join(source_dir, cls))
    random.shuffle(files)

    split = int(0.8 * len(files))

    train_files = files[:split]
    val_files = files[split:]

    for f in train_files:
        shutil.copy(
            os.path.join(source_dir, cls, f),
            os.path.join(train_dir, cls, f)
        )

    for f in val_files:
        shutil.copy(
            os.path.join(source_dir, cls, f),
            os.path.join(val_dir, cls, f)
        )

print("Dataset split complete!")

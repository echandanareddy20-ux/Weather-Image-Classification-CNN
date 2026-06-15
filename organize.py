import os
import shutil

source_dir = "C:/Users/E Chandana Reddy/Downloads/archive/dataset2"

classes = ["cloudy", "rainy", "sunrise", "shine"]

# Create class folders
for cls in classes:
    os.makedirs(os.path.join(source_dir, cls), exist_ok=True)

# Move only image files
for file in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file)

    # ✅ Skip directories
    if os.path.isdir(file_path):
        continue

    for cls in classes:
        if cls in file.lower():
            shutil.move(
                file_path,
                os.path.join(source_dir, cls, file)
            )
            break

print("Done organizing!")
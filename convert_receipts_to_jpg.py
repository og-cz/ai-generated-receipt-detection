"""
convert_receipts_to_jpg.py

This Python script converts all receipt images from a source folder into 
standardized RGB JPEG (.jpg) format and saves them into designated destination folders. 

It is designed for preprocessing datasets for machine learning projects, 
specifically for classifying real vs AI-generated receipt screenshots.

Features:
- Supports input images in PNG, JPG, JPEG, and JFIF formats
- Converts all images to RGB color mode
- Saves all images as high-quality JPGs
- Preserves original filenames (extension changed to .jpg)
- Can use absolute or relative paths for source folders
- Automatically creates destination folders if they do not exist
- Logs errors for any files that cannot be converted

Usage:
1. Set the `source_folders` dictionary to point to your original receipt folders.
2. Set the `destination_folders` dictionary to the folder(s) where converted images should be saved.
3. Run the script. The cleaned images will be saved in the destination folders.
4. After conversion, the dataset is ready for train/validation/test splitting and model training.

Author: Your Name
Date: 2026-01-28
"""


from PIL import Image
import os

cwd = os.getcwd()

# Paths
source_folders = {
    "fake": r"C:\PASTE YOUR ABSOLUTE PATH RAW IMAGE DATA HERE",
    "real": r"C:\PASTE YOUR ABSOLUTE PATH RAW IMAGE DATA HERE"
}

# Destination folders (created in current repo)
destination_folders = {
    "fake": os.path.join(cwd, "clean-total-ai"),
    "real": os.path.join(cwd, "clean-total-legit")
}

# Create destination folders
for dest in destination_folders.values():
    os.makedirs(dest, exist_ok=True)

# Conversion loop
for label in source_folders:
    src_folder = source_folders[label]
    dest_folder = destination_folders[label]

    for filename in os.listdir(src_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".jfif")):
            try:
                img = Image.open(os.path.join(src_folder, filename)).convert("RGB")
                base_name = os.path.splitext(filename)[0]
                save_path = os.path.join(dest_folder, f"{base_name}.jpg")
                img.save(save_path, "JPEG", quality=95)
            except Exception as e:
                print(f"Error converting {filename}: {e}")

print("Conversion complete! Images saved in:", destination_folders)
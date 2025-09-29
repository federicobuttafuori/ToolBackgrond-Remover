# remove_bg_no_ui.py
import os
from rembg import remove
from PIL import Image

# Folders
current_folder = os.path.dirname(os.path.abspath(__file__))
input_folder = current_folder
output_folder = os.path.join(current_folder, "output_images")
os.makedirs(output_folder, exist_ok=True)

processed_count = 0
failed_count = 0

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        # Skip the output folder to avoid re-processing
        if os.path.abspath(input_folder) == os.path.abspath(output_folder):
            continue

        input_path = os.path.join(input_folder, file_name)
        name, _ = os.path.splitext(file_name)
        output_path = os.path.join(output_folder, name + ".png")  # Save as PNG to keep transparency

        try:
            with Image.open(input_path) as img:
                result = remove(img)
                result.save(output_path)
            print(f"Processed: {file_name}")
            processed_count += 1
        except Exception as e:
            print(f"Failed: {file_name} ({e})")
            failed_count += 1

print(f"Done! Processed: {processed_count}, Failed: {failed_count}")

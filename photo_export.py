import os
import shutil
from pathlib import Path
from tqdm import tqdm
import sys

def clear_directory(path):
    """Clear the specified directory."""
    for item in Path(path).glob("*"):
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()

if len(sys.argv) != 3:
    print("Usage: python photo_export.py \"<PhotosLibraryPath>\" \"<DestinationPath>\"")
    sys.exit(1)

# Set the Photos library and the target path based on command-line arguments
photos_library_path = sys.argv[1]  # Replace with the actual Photos library path from the command line
destination_path = sys.argv[2]  # Replace with the desired destination path from the command line

print(f"Photos library path: {photos_library_path}")
print(f"Destination path: {destination_path}")

# Clear the destination path
print("Clearing the destination directory...")
clear_directory(destination_path)

# In newer versions of macOS, the path for original photo files is "originals"
originals_path = os.path.join(photos_library_path, 'originals')
if not os.path.exists(originals_path):
    originals_path = os.path.join(photos_library_path, 'Masters')  # Try "Masters" path if "originals" doesn't exist
    print("Using 'Masters' path for photos.")

# Ensure the destination path exists
Path(destination_path).mkdir(parents=True, exist_ok=True)

# First, get all the file paths to be copied
all_files = [os.path.join(root, file) for root, dirs, files in os.walk(originals_path) for file in files]

# Display copy progress using tqdm
for file_path in tqdm(all_files, desc="Copying photos"):
    # Destination file path (not preserving the original directory structure)
    destination_file_path = os.path.join(destination_path, os.path.basename(file_path))
    # Check for filename conflict and adjust filename
    counter = 1
    base_name, ext = os.path.splitext(destination_file_path)
    while os.path.exists(destination_file_path):
        destination_file_path = f"{base_name}_{counter}{ext}"
        counter += 1
    # Copy file
    shutil.copy2(file_path, destination_file_path)

print("Photo copy completed.")

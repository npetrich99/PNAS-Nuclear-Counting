# Key Imports:
import numpy as np
import os
import pandas as pd
import tifffile
from skimage import measure

# Configuration:
folder_path = r"C:\Users\nolan\Desktop\Segmentations\Nuclear_Masks"
output_excel = "Nuclear_Count_Report.xlsx"

def count_nuclei(image_path):
    # Load the TIFF File:
    img = tifffile.imread(image_path)
    
    # Get All Unique Pixel Values:
    unique_labels = np.unique(img)
    
    # If the background is 0, we subtract 1 from the total count of unique values.
    # We use "unique_labels > 0" to filter out the background regardless of its value.
    actual_labels = unique_labels[unique_labels > 0]
    count = len(actual_labels)
    
    return count

def main():
    results = []

    # Check if Directory Exists:
    if not os.path.exists(folder_path):
        print(f"Error: The folder {folder_path} does not exist.")
        return

    print("Processing files...")

    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".tif", ".tiff")):
            file_path = os.path.join(folder_path, filename)
            try:
                num_masks = count_nuclei(file_path)
                results.append({"Filename": filename, "Nuclear Mask Count": num_masks})
                print(f"Processed: {filename} - Found: {num_masks}")
            except Exception as e:
                print(f"Could not process {filename}: {e}")

    # Create DataFrame and Export to Excel:
    df = pd.DataFrame(results)
    df.to_excel(output_excel, index = False)
    print(f"\nSuccess! Report saved as {output_excel}")

if __name__ == "__main__":
    main()
# Key Imports:
import numpy as np
import warnings
from csbdeep.utils import normalize
from pathlib import Path
from skimage import filters
from stardist.models import StarDist2D
from tifffile import imread, imwrite

warnings.filterwarnings("ignore")

# Configuration:
input_dir = Path(r"/scratch/Users/nope7188/Images")
output_root = Path(r"/scratch/Users/nope7188/Segmentations/Nuclear_Masks")

# StarDist Parameters:
prob_thresh = 0.4
nms_thresh = 0.3

# Preprocessing Parameters:
blur_sigma = 0.5
normalize_pmin = 1
normalize_pmax = 99.8

# Load Pretrained StarDist Model:
model = StarDist2D.from_pretrained("2D_versatile_fluo")

def process_images():
    # Find All .tif and .tiff Files Recursively:
    image_extensions = ("*.tif", "*.tiff")
    image_files = []
    for ext in image_extensions:
        image_files.extend(list(input_dir.rglob(ext)))

    if not image_files:
        print(f"No images found in {input_dir}")
        return

    print(f"Found {len(image_files)} images. Starting processing...")

    for filepath in image_files:
        # Determine Relative Path to Maintain Folder Structure:
        relative_path = filepath.relative_to(input_dir)
        # Define Output Directory for Specific File:
        target_dir = output_root / relative_path.parent
        target_dir.mkdir(parents = True, exist_ok = True)
        
        output_filename = f"{filepath.stem}-nuclear_mask.tif"
        output_path = target_dir / output_filename

        print(f"Processing: {relative_path}")

        try:
            # Load Image:
            img = imread(str(filepath)).astype(np.float32)

            # Check to Ensure it's a Single 2D Slice:
            # If Image has Multiple Channels or Slices, Take the First One Available:
            if img.ndim > 2:
                # Assuming (C, Y, X) or (Z, Y, X) - Take First Index:
                img = img[0] 

            # Preprocessing: Gaussian Blur and StarDist Normalization:
            img_blurred = filters.gaussian(img, sigma = blur_sigma)
            img_norm = normalize(img_blurred, normalize_pmin, normalize_pmax)

            # Segmentation:
            labels, _ = model.predict_instances(
                img_norm, 
                prob_thresh = prob_thresh, 
                nms_thresh = nms_thresh
            )
            
            # Save Results:
            imwrite(str(output_path), labels.astype(np.uint16), compression = "zlib")
            print(f"Saved to: {output_path.relative_to(output_root)}")

        except Exception as e:
            print(f"Error processing {filepath.name}: {e}")

if __name__ == "__main__":
    process_images()
    print("\nAll processing complete.")
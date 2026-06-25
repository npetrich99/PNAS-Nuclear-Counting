# Nuclear Segmentation Using StarDist2D

## Overview:

This repository contains the code and software environment used for nuclear segmentation utilizing StarDist2D.

---

## Repository Contents

| File | Description |
|------|-------------|
| `nuclear_segmentation.py` | Main Segmentation Script |
| `requirements.txt` | Python Package Requirements |
| `requirements_min.txt` | Minimum Python Package Requirements |
| `README.md` | Documentation |
---

## Software Requirements:

This code was tested with:

* Python 3.11.3
* TensorFlow 2.19.0
* StarDist 0.9.1
* NVIDIA GPU (tested on NVIDIA A100 hardware)

The complete software environment is provided in `requirements.txt`.

---

## Installation:

Create and activate a Python virtual environment:

```bash
module purge
module load python/3.11.3

python -m venv STARDIST-VENV
source STARDIST-VENV/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## GPU Verification:

To verify that TensorFlow detects an available GPU:

```bash
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

Expected output:

```text
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

---

## Input Data:

Input directory is set inside `nuclear_segmentation.py` and should be modified by the user if needed. This script expects TIFF images containing a single 2D nuclear channel or multi-dimensional images where the first slice is used.

---

## Running the Analysis:

The script recursively processes all `.tif` and `.tiff` images in the input directory:

```bash
python nuclear_segmentation.py
```

---

## Image Processing Pipeline:

Each image is processed using:
- Gaussian smoothing (σ = 0.5)
- Intensity normalization (1–99.8 percentile)
- StarDist2D pretrained model ("2D_versatile_fluo")
- Probability threshold: 0.4
- NMS threshold: 0.3

---

## Output Files:

The output directory is defined in the script:

`/scratch/Users/nope7188/Segmentations/Nuclear_Masks`

Users should modify this path if running on a different system. The Nuclear_Masks folder contains single-channel labeled segmentation masks in TIFF format for each associated input TIFF image with the suffix `-nuclear_mask.tif`. Folder structure from the input directory is preserved.

---

## Tested Environment:

* Computing Platform: Fiji (University of Colorado Boulder BioFrontiers Institute HPC Cluster)
* GPU: NVIDIA A100
* Python: 3.11.3
* TensorFlow: 2.19.0
* StarDist: 0.9.1

---

## Citation:

If you use this code, please cite the associated manuscript:

Michael R. Blatchley, Kaustav Bera, Nolan R. Petrich, Bruce E. Kirkpatrick, F. Max Yavitt, Patrick S. McGrath, Peter J. Dempsey, Kristi S. Anseth. *"Spatiotemporally controlled matrix softening facilitates deterministic crypt formation in human intestinal organoids"*. PNAS (2026).
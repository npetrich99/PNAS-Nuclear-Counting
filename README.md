# PNAS-Nuclear-Counting

# Automated Nuclear Segmentation and Quantification:

## Overview:

This repository contains a two-step image analysis pipeline for automated nuclear segmentation and quantification in fluorescence microscopy images.

The workflow uses StarDist2D for instance segmentation of nuclei and a downstream quantification script to count segmented nuclei from labeled mask images.

This pipeline was developed and applied in support of:

*"Spatiotemporally controlled matrix softening facilitates deterministic crypt formation in human intestinal organoids"*  
Michael R. Blatchley, Kaustav Bera, Nolan R. Petrich, Bruce E. Kirkpatrick, F. Max Yavitt, Patrick S. McGrath, Peter J. Dempsey, Kristi S. Anseth. PNAS (2026).

---

## Workflow:

```text
Input Fluorescence Images
            │
            ▼
   Nuclear Segmentation
      (StarDist2D)
            │
            ▼
 Labeled Nuclear Masks
            │
            ▼
 Nuclear Quantification
     (Object Counting)
            │
            ▼
 Nuclear_Count_Report.xlsx
```

---

## Repository Structure:

| Directory | Description |
|------------|-------------|
| `Nuclear_Segmentation/` | StarDist2D-Based Nuclear Segmentation Workflow |
| `Nuclear_Counting/` | Quantification of Labeled Nuclear Masks |
| `README.md` | Repository Documentation |

---

## Analysis Pipeline:

### Step 1: Nuclear Segmentation:

The segmentation workflow:

- Loads fluorescence microscopy images.
- Applies image normalization and preprocessing.
- Uses the pretrained StarDist2D model (`2D_versatile_fluo`).
- Generates labeled nuclear instance masks.
- Preserves the input directory structure in the output.

See:

```text
Nuclear_Segmentation/README.md
```

for installation instructions, software requirements, and usage details.

---

### Step 2: Nuclear Quantification:

The quantification workflow:

- Reads labeled segmentation masks.
- Identifies unique nuclear object labels.
- Counts segmented nuclei per image.
- Exports results to an Excel spreadsheet.

See:

```text
Nuclear_Counting/README.md
```

for usage details and expected input formats.

---

## Software Environment:

The segmentation pipeline was tested using:

- Python 3.11.3
- TensorFlow 2.19.0
- StarDist 0.9.1
- NVIDIA A100 GPU

Tested on:

- Fiji (University of Colorado Boulder BioFrontiers Institute HPC Cluster)

---

## Typical Usage:

### 1. Generate Nuclear Masks:

```bash
cd Nuclear_Segmentation
python nuclear_segmentation.py
```

### 2. Quantify Segmented Nuclei:

```bash
cd ../Nuclear_Counting
python counting.py
```

### 3. Review Results:

The counting script generates:

```text
Nuclear_Count_Report.xlsx
```

containing nuclear counts for each segmentation mask.

---

## Citation:

If you use this repository, please cite the associated manuscript:

Michael R. Blatchley, Kaustav Bera, Nolan R. Petrich, Bruce E. Kirkpatrick, F. Max Yavitt, Patrick S. McGrath, Peter J. Dempsey, Kristi S. Anseth. *"Spatiotemporally controlled matrix softening facilitates deterministic crypt formation in human intestinal organoids"*. PNAS (2026).

---
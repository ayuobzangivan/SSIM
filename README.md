# SSIM-Average

This repository contains a Python script for calculating the Structural Similarity Index (SSIM) between corresponding images in two folders (e.g., real and predicted images). The average SSIM score provides an objective metric to evaluate the similarity between the two image sets.

---

## Features
- **Batch SSIM Calculation**: Computes SSIM for all pairs of images in the specified folders.
- **Average SSIM**: Outputs the average SSIM score for a summary metric.
- **Customizable Paths**: Easily adaptable for different datasets by modifying folder paths.

---

## How It Works
1. The script reads images from two folders: one for real images (`real_folder`) and the other for predicted images (`notreal_folder`).
2. It calculates SSIM for each pair of corresponding images.
3. Finally, it computes and prints the average SSIM score.

---

## Code Example

```python
from skimage.metrics import structural_similarity as ssim
from skimage import io
import os

def calculate_ssim_for_folder(real_folder, notreal_folder):
    real_images = os.listdir(real_folder)
    notreal_images = os.listdir(notreal_folder)

    num_images = min(len(real_images), len(notreal_images))
    ssim_scores = []

    for i in range(num_images):
        real_image_path = os.path.join(real_folder, real_images[i])
        notreal_image_path = os.path.join(notreal_folder, notreal_images[i])

        real_image = io.imread(real_image_path)
        notreal_image = io.imread(notreal_image_path)

        ssim_score = ssim(real_image, notreal_image, multichannel=True)
        ssim_scores.append(ssim_score)

    return ssim_scores

Example Usage

real_folder = "path/to/real/images"
notreal_folder = "path/to/predicted/images"

ssim_scores = calculate_ssim_for_folder(real_folder, notreal_folder)
average_ssim = sum(ssim_scores) / len(ssim_scores)
print("Average SSIM:", average_ssim)

Requirements

    Python >= 3.7
    Required libraries:
        scikit-image
        numpy (indirectly used via scikit-image)

Install dependencies with:

pip install -r requirements.txt

How to Use

    Clone the repository:

git clone https://github.com/username/SSIM-Average.git
cd SSIM-Average

Set the folder paths in the script (real_folder and notreal_folder).
Run the script:

    python SSIM_Average.py

Output

The script prints the average SSIM score:

Average SSIM: 0.876543

Applications

    Evaluate image similarity in computer vision projects.
    Compare real and predicted images in GANs or other deep learning models.
    Quantify image quality in preprocessing pipelines.

## License

This project is open-source and available under the MIT License. See the LICENSE file for details.

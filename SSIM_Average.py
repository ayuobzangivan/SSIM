#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os
from skimage.metrics import structural_similarity as ssim
from skimage import io

def calculate_ssim_for_folder(real_folder, notreal_folder):
    real_images = os.listdir(real_folder)
    notreal_images = os.listdir(notreal_folder)

    num_images = min(len(real_images), len(notreal_images))
    ssim_scores = []

    for i in range(num_images):
        real_image_path = os.path.join(real_folder, real_images[i])
        notreal_image_path = os.path.join(notreal_folder, notreal_images[i])

        # Load the images
        real_image = io.imread(real_image_path)
        notreal_image = io.imread(notreal_image_path)

        # Calculate the SSIM
        ssim_score = ssim(real_image, notreal_image, multichannel=True)
        ssim_scores.append(ssim_score)

    return ssim_scores

# Example usage
real_folder = "C:/Users/ayzeg/Dropbox/ممیزی انرژی/پایان نامه/ASSET (3d files and codes and other stuff)/CODE FOR PRE-PROCCESING DATAS/SSIM/REAL"
notreal_folder = "C:/Users/ayzeg/Dropbox/ممیزی انرژی/پایان نامه/ASSET (3d files and codes and other stuff)/CODE FOR PRE-PROCCESING DATAS/SSIM/PREDICTED"

ssim_scores = calculate_ssim_for_folder(real_folder, notreal_folder)
average_ssim = sum(ssim_scores) / len(ssim_scores)
print("Average SSIM:", average_ssim)


# In[ ]:





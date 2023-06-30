import glob
from PIL import Image
import numpy as np
from skimage.measure import compare_ssim as ssim
import math

def compute_ssim_psnr(image_path):
    # Load the image
    image = Image.open(image_path)

    # Split the image into two halves along the middle vertical line
    width, height = image.size
    half_width = width // 2
    image1 = image.crop((0, 0, half_width, height))
    image2 = image.crop((half_width, 0, width, height))

    # Convert images to grayscale if they are in color
    if image1.mode != 'L':
        image1 = image1.convert('L')
    if image2.mode != 'L':
        image2 = image2.convert('L')

    # Convert images to NumPy arrays
    image1 = np.array(image1)
    image2 = np.array(image2)

    # Calculate SSIM
    ssim_score = calculate_ssim(image1, image2)

    # Calculate PSNR
    psnr_score = calculate_psnr(image1, image2)

    return ssim_score, psnr_score

def calculate_ssim(image1, image2):
    # Calculate SSIM
    ssim_score = ssim(image1, image2, data_range=image2.max() - image2.min())

    return ssim_score

def calculate_psnr(image1, image2):
    # Calculate MSE
    mse = np.mean((image1 - image2) ** 2)

    # Calculate PSNR
    psnr_score = 10 * math.log10((255 ** 2) / mse)

    return psnr_score

result_dir = './result_Sony_small_L1L2/'

outputs = glob.glob(result_dir + '0250/*')
# Compute the SSIM score
psnr_lst = []
ssim_lst = []
for output in outputs:
    ssim_score, psnr_score = compute_ssim_psnr(output)
    psnr_lst.append(psnr_score)
    ssim_lst.append(ssim_score)

print psnr_lst
average_psnr = np.mean(psnr_lst)
average_ssim = np.mean(ssim_lst)
print("The average PSNR score is: %f\nThe average SSIM score is: %f" % (average_psnr, average_ssim))

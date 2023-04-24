# from tensorflow.keras.models import save_model
# import os
import numpy as np
from PIL import Image, ImageChops, ImageEnhance
from flask import Flask


def ela(img_path, scale=10, threshold=50):
    # Create a temporary image with lower quality and save it
    resaved_path = "resaved.jpg"
    im = Image.open(img_path)
    im_resaved = im.copy().save(resaved_path, "JPEG", quality=scale)

    # Calculate the error level between the original and resaved image
    orig = Image.open(img_path)
    resaved = Image.open(resaved_path)
    diff = ImageChops.difference(orig, resaved)
    enhancer = ImageEnhance.Brightness(diff)
    diff = enhancer.enhance(10)
    diff.save("diff.jpg")

    # Calculate the average error level of the image
    np_diff = np.asarray(diff)
    ela_value = np.mean(np_diff)

    # Return a boolean value based on whether the average error level is above the threshold
    return ela_value > threshold


# Test the ELA function
#img_path = "venv/images/Aadhar Tarun.jpg"
#threshold = 83
#is_fake = ela(img_path, scale=10, threshold=threshold)
#if is_fake:
#    print(f"The image at {img_path} is likely fake with ELA value above {threshold}")
#else:
    #print(f"The image at {img_path} is likely real with ELA value below {threshold}")


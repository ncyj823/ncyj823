import sys
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep(input_path):
    print(f"Removing background from {input_path}...")
    input_image = Image.open(input_path)
    output_image = remove(input_image)

    np_image = np.array(output_image)
    gray = cv2.cvtColor(np_image, cv2.COLOR_RGBA2GRAY)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    alpha = np_image[:, :, 3] / 255.0
    white_bg = np.ones_like(np_image[:, :, :3]) * 255
    composited = (np_image[:, :, :3] * alpha[:, :, np.newaxis] + white_bg * (1 - alpha[:, :, np.newaxis])).astype(np.uint8)

    gray_final = cv2.cvtColor(composited, cv2.COLOR_RGB2GRAY)
    cv2.imwrite("source-prepped.png", gray_final)
    print("Saved prepped image to source-prepped.png")

if __name__ == "__main__":
    img_path = sys.argv[1] if len(sys.argv) > 1 else "source-photo.jpg"
    prep(img_path)

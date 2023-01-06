import os
import sys

from PIL import Image

def main(images_directory_path):
    print("compressing images in ", images_directory_path, "...")

    for image_name in os.listdir(images_directory_path):
        if image_name.endswith((".jpg", ".jpeg", ".png")):
            image_extension = image_name.split(".")[-1]
            image_path = os.path.join(images_directory_path, image_name)
            orig_img = Image.open(image_path)
            size = orig_img.size
            factor = 0.5
            new_size = (int(factor * size[0]), int(factor * size[1]))
            new_img = orig_img.resize(new_size, Image.ANTIALIAS)

            optimized_images_directory = os.path.join(images_directory_path, "optimized_images")
            os.makedirs(optimized_images_directory, exist_ok=True)

            new_image_name = image_name.replace(f".{image_extension}", f"_optimized.{image_extension}")
            new_image_path = os.path.join(optimized_images_directory, new_image_name)
            new_img.save(new_image_path, optimize=True, quality=95)

    print("...done")


if __name__ == "__main__":
    images_path = sys.argv[1]
    main(images_path)

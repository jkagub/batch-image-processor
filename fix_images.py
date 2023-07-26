#! python

from PIL import Image
import os

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        image_path = os.path.join(input_folder, filename)
        # Try if file is a valid image file
        try:
            with Image.open(image_path) as img:
                # convert to RGB if necessary
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGB')
                # Rotate the image 90° anti-clockwise
                rotated_img = img.rotate(90, expand=True)

                # Resize the image to 128x128
                resized_img = rotated_img.resize((128, 128))
                
        except:
            print(f"Error: {image_path} is not a valid image file")
            continue

        try:
            
            # Save the image to the new folder with .jpeg extension
            #output_filename = os.path.splitext(filename)[0] + ".jpeg"
            output_path = os.path.join(output_folder, filename)
            resized_img.save(output_path, "JPEG")
        except OSError:
            print(f"Error: {output_path} not saved to path")
            continue
        
if __name__ == "__main__":
    input_folder = "images"
    output_folder = "opt\icons"
    process_images(input_folder, output_folder)

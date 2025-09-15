from rembg import remove
from PIL import Image

import os

input_path = os.path.join(os.path.expanduser('~'), 'OneDrive/Documents/OBIALO CHIDINMA JOY/Dr Dinm - Signature.jpg')
output_path = os.path.join(os.path.expanduser('~'), 'OneDrive/Documents/OBIALO CHIDINMA JOY/Dr Dinm - SignatureNoBg.png')

def remove_background(input_path, output_path):
    try:
        # Check if input path exists
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input path '{input_path}' does not exist.")
        
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Open the input image
        input_image = Image.open(input_path)

        # Remove background from the input image
        output_image = remove(input_image)

        # Save the output image
        output_image.save(output_path)
        print(f"Background removed and Image saved successfully at '{output_path}'")
        
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except IOError as io_error:
        print(f"IOError: {io_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Remove background from the image
remove_background(input_path, output_path)
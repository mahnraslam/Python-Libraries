 
from PIL import Image

from PIL import Image
import numpy as np

# Open an image file
with Image.open('lead_30.png') as img:
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Determine the new size
    new_size = (50, 50)
    
    # Calculate block size
    block_size = (img_array.shape[0] // new_size[0], img_array.shape[1] // new_size[1])
    
    # Downsample image by averaging each block
    downsampled_array = img_array.reshape(
        new_size[0], block_size[0], 
        new_size[1], block_size[1], 
        img_array.shape[2]
    ).mean(axis=(1, 3))
    
    # Convert back to image
    downsampled_img = Image.fromarray(np.uint8(downsampled_array))

    # Save the downsampled image
    downsampled_img.save('downsampled_image.png')

# # Open an image file
# with Image.open('lead_30.png') as img:
#     # Resize the image to 5x5 pixels using LANCZOS filter
#     img_resized = img.resize((50, 50), Image.Resampling.LANCZOS)
#     img_resized.save('your_resized_image.png')


# img = Image.open(f'lead_30.png')        
# # Resize the image to a more manageable size
# img_resized = img.resize((5, 5),   Image.Resampling.LANCZOS)
# img.save("resize.png","PNG")
# # img_array = np.asarray(img_resized) 
# # x_position = 500
# # y_position = -28200.0
 
 

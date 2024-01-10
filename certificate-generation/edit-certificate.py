import cv2


def add_text_to_image(image_path, text):
    """
    Add dynamic text to the generated image using OpenCV.
    """
    image = cv2.imread(image_path)
    
    # Text position
    text_position = (50, 50)

    # Text color
    text_color = (255, 255, 255)

    # Font settings
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2

    # Add text to the image
    cv2.putText(image, text, text_position, font, font_scale, text_color, font_thickness)

    # Save the modified image
    cv2.imwrite(image_path, image)
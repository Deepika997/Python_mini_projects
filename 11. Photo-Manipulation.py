from PIL import Image, ImageFilter

try:
    # Open an image file
    img = Image.open(r"C:\Users\Ranjitha\OneDrive\Pictures\Screenshots\Screenshot (383).png")

    # original image
    img.show()

    # Resize the image to a specific width and height
    resized_img = img.resize((400, 300))
    resized_img.show()

    # Rotate the image by a specific angle (in degrees)
    rotated_img = img.rotate(45)
    rotated_img.show()

    # Apply a Gaussian blur filter to the image
    blurred_img = img.filter(ImageFilter.GaussianBlur(radius=2))
    blurred_img.show()

    # Convert the image to grayscale
    grayscale = img.convert("L")
    grayscale.show()

except Exception as e:
    print("An error occurred:", e)

from PIL import Image

def convert_png_to_jpeg(input_path, output_path, quality=75):
    """
    Convert a PNG image to JPEG format.

    Parameters:
    - input_path: Path to the input PNG image.
    - output_path: Path to save the output JPEG image.
    - quality: JPEG quality (default is 75).

    Returns:
    None
    """
    try:
        # Open the PNG image
        png_image = Image.open(input_path)

        # Convert to RGB and save as JPEG
        png_image.convert('RGB').save(output_path, 'JPEG', quality=quality)
        
        print(f"Conversion complete. JPEG image saved at: {output_path}")

    except Exception as e:
        print(f"Error during conversion: {e}")

convert_png_to_jpeg('extreme_ironing.png', '6.jpeg', quality=75)
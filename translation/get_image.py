# pip install pillow

from PIL import Image

def decode_monochrome_to_png(input_file, output_file, width, height, offset):
    """
    Decode a binary file into a grayscale PNG image where each byte is a luminosity value.
    """
    # Open the input file in binary mode
    with open(input_file, 'rb') as f:
        # Skip to the given offset
        f.seek(offset)
        # Read the raw grayscale data
        raw_data = f.read(width * height)  # Each pixel takes 1 byte

    # Check if enough data was read
    if len(raw_data) < width * height:
        raise ValueError("Not enough data in the file for the given dimensions.")

    # Create a grayscale image
    image = Image.frombytes("L", (width, height), raw_data)
    image.save(output_file)

def unscramble_columns(input_file, output_file, width, height):
    """
    Unscramble a monochrome (grayscale) image where all even columns
    are displayed first, followed by all odd columns, row-wise alignment.
    """
    # Open the scrambled image
    scrambled_img = Image.open(input_file).convert("L")  # Ensure grayscale mode ("L")
    scrambled_pixels = scrambled_img.load()

    # Create a new image for the unscrambled result
    unscrambled_img = Image.new("L", (width, height))
    unscrambled_pixels = unscrambled_img.load()

    # Reconstruct the image row by row
    for y in range(height):
        idx1 = 0
        idx2 = width // 2
        for x in range(width):
            if x % 2 == 1:
                unscrambled_pixels[x, y] = scrambled_pixels[idx1, y]
                idx1 += 1
            else:
                unscrambled_pixels[x, y] = scrambled_pixels[idx2, y]
                idx2 += 1

    # Save the unscrambled image
    unscrambled_img.save(output_file)

if __name__ == "__main__":
    # Example usage
    input_file = "DDF.bin"         # Input binary file
    offset = 0x000692A4            # Offset to start reading from (in bytes)

    decode_monochrome_to_png(input_file, "lumo.png", 105, 50, offset)
    unscramble_columns("lumo.png", "lumo_des.png", 105, 50)

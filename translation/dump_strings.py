import os

def extract_utf8_strings(binary_file, output_file, min_length=4):
    def is_printable_utf8(byte_data):
        # Check if the byte data is valid UTF-8
        try:
            byte_data.decode('utf-8')
            return True
        except UnicodeDecodeError:
            return False

    with open(binary_file, 'rb') as f:
        data = f.read()

    # Start variables
    current_string = bytearray()
    start_address = None

    with open(output_file, 'w', encoding='utf-8') as out:
        for i in range(len(data)):
            byte = data[i:i+1]

            if byte != b'\x00':  # Continue building string until null terminator
                if start_address is None:
                    start_address = i  # Record the start address of the potential string
                current_string += byte

            if byte == b'\x00' or i == len(data) - 1:  # Null terminator or end of file
                if current_string and len(current_string) >= min_length:
                    if is_printable_utf8(current_string):
                        # Decode and write the valid string and its start address
                        decoded_str = current_string.decode('utf-8')
                        out.write(f"ADDRESS   :{hex(start_address)}\n")
                        out.write(f"LEN_BYTES :{len(current_string)}\n")
                        out.write(f"ORIGINAL  :{decoded_str}[END]\n")
                        out.write(f"TRANSLATED:{decoded_str}[END]\n\n")
                
                # Reset variables for the next string
                current_string = bytearray()
                start_address = None

if __name__ == "__main__":
    binary_file_path = 'input.bin'  # Path to the input binary file
    output_file_path = 'output.txt' # Path to the output text file
    min_length = 4                  # Minimum length of string to extract

    extract_utf8_strings(binary_file_path, output_file_path, min_length)

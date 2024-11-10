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

    with open(output_file, 'w', encoding='utf-8') as out:
        i = 0
        while i < len(data):
            # Only check for strings starting at addresses that are multiples of 4
            if i % 4 != 0:
                i += 1
                continue

            current_string = bytearray()
            start_address = None

            # Process bytes starting at the current address
            while i < len(data):
                byte = data[i:i+1]

                if byte != b'\x00':  # Continue building string until null terminator
                    if start_address is None:
                        start_address = i  # Record the start address of the potential string
                    current_string += byte
                else:  # Null terminator or end of string
                    if current_string and len(current_string) >= min_length:
                        if is_printable_utf8(current_string):
                            # Decode and write the valid string and its start address
                            decoded_str = current_string.decode('utf-8')
                            out.write(f"ADDRESS   :{hex(start_address)}\n")
                            out.write(f"LEN_BYTES :{len(current_string)}\n")
                            out.write(f"ORIGINAL  :{decoded_str}[END]\n")
                            out.write(f"TRANSLATED:{decoded_str}[END]\n\n")
                    break  # Exit inner loop after null terminator

                i += 1  # Move to the next byte

            # Ensure we increment properly when exiting the inner loop
            i += 1

if __name__ == "__main__":
    binary_file_path = 'input.bin'  # Path to the input binary file
    output_file_path = 'output.txt' # Path to the output text file
    min_length = 4                  # Minimum length of string to extract

    extract_utf8_strings(binary_file_path, output_file_path, min_length)

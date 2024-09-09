import re

def parse_and_insert_translated_strings(original_file, output_file, translation_file):
    # Read the original binary file and make a copy to modify
    with open(original_file, 'rb') as f:
        original_data = bytearray(f.read())

    # Regular expressions for matching the format
    address_pattern = re.compile(r"ADDRESS\s+:\s*(0x[0-9a-fA-F]+)")
    translated_pattern = re.compile(r"TRANSLATED:(.*)", re.DOTALL)
    
    # Read the translation file line by line
    with open(translation_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split sections by the "ADDRESS" keyword
    sections = content.split("ADDRESS")
    
    for section in sections[1:]:  # Skip the first part, as it won't have a valid section
        # Extract address and translated string
        address_match = address_pattern.search(f"ADDRESS{section}")
        translated_match = translated_pattern.search(section)

        if not address_match or not translated_match:
            continue

        # Extract the address as an integer
        address = int(address_match.group(1), 16)
        print(f"Found address: {hex(address)}")  # Debug

        # Extract and process the TRANSLATED string
        translated_text = translated_match.group(1).strip()
        print(f"Original TRANSLATED text: {translated_text}")  # Debug
        translated_text = translated_text.replace('[END]', '\x00')  # Replace [END] with null terminator
        print(f"Processed TRANSLATED text: {translated_text}")  # Debug

        # Function to handle $xx bytes in the string
        def process_translated_string(text):
            result = bytearray()
            i = 0
            while i < len(text):
                if text[i] == '$':  # Handle byte literals like $C3
                    byte_val = int(text[i+1:i+3], 16)
                    result.append(byte_val)
                    i += 3  # Skip $xx
                else:
                    # Append UTF-8 encoded bytes of regular characters
                    result.extend(text[i].encode('utf-8'))
                    i += 1
            return result

        # Convert TRANSLATED text to bytes
        translated_bytes = process_translated_string(translated_text)
        print(f"Translated bytes: {translated_bytes}")  # Debug

        # Find the null-terminator in the original data at the address
        null_terminator_pos = original_data.find(b'\x00', address)
        print(f"Null terminator found at: {null_terminator_pos}")  # Debug

        if null_terminator_pos == -1:
            raise ValueError(f"No null terminator found in the original file after address {hex(address)}.")

        # Ensure we don't overwrite beyond the null-terminator
        max_length = null_terminator_pos - address
        print(f"Max length available: {max_length}")  # Debug

        # Pad with null bytes if needed to fit the original size
        if len(translated_bytes) < max_length:
            translated_bytes += b'\x00' * (max_length - len(translated_bytes))

        # Write the translated bytes back to the original data
        original_data[address:address + max_length] = translated_bytes[:max_length]
        print(f"Data written at address {hex(address)}: {original_data[address:address+max_length]}")  # Debug

    # Write the modified data to the output file
    with open(output_file, 'wb') as f:
        f.write(original_data)
        print(f"File written to {output_file}")  # Debug

if __name__ == "__main__":
    # Example usage
    original_file_path = 'input.bin'  # Path to the original binary file
    output_file_path = 'output.bin'   # Path to the output binary file (modified copy)
    translation_file_path = 'common.txt'    # Path to the file with ADDRESS and TRANSLATED strings

    parse_and_insert_translated_strings(original_file_path, output_file_path, translation_file_path)

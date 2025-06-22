import unicodedata

STOP_STRING = "{}[]()<>$|@&^´`'\"ɰȱ"

def extract_utf8_strings(binary_file, output_file, min_length=4):
    def is_dumpable_string(byte_data, not_chars=''):
        # They do not start below spaces
        if byte_data[0] < 0x20:
            return False

        # Check if the byte_data is valid UTF-8
        try:
            decoded = byte_data.decode('utf-8')
        except UnicodeDecodeError as e:
            return False

        # There is definitely no right to left chars in there, and adding them to stop in ltr IDE is a PITA
        if any(unicodedata.bidirectional(ch) in ('R', 'AL', 'AN') for ch in decoded):
            return False

        # Reject if any character is present
        if not_chars and any(ch in not_chars for ch in decoded):
            return False

        return True

    with open(binary_file, 'rb') as f:
        data = f.read()

    with open(output_file, 'w', encoding='utf-8') as out:
        i = 0
        data_len = len(data)

        while i < data_len:
            # Only check string starts at 4-byte boundaries
            if i % 4 != 0:
                i += 1
                continue

            start = i
            # Collect bytes until null terminator
            current = bytearray()
            j = i
            while j < data_len and data[j] != 0:
                current.append(data[j])
                j += 1

            # If we hit a null or end, process current buffer
            if len(current) >= min_length:
                if is_dumpable_string(current, STOP_STRING):
                    decoded = current.decode('utf-8')
                    out.write(f"ADDRESS   :{hex(start)}\n")
                    out.write(f"LEN_BYTES :{len(current)}\n")
                    out.write(f"ORIGINAL  :{decoded}[END]\n")
                    out.write(f"TRANSLATED:{decoded}[END]\n\n")
                    # Move past this string
                    i = j + 1
                else:
                    # Invalid UTF-8: retry at next 4-byte boundary within this region
                    i = start + 4
            else:
                # Too short or empty: skip past
                i = j + 1

if __name__ == "__main__":
    binary_file_path = 'input.bin'
    output_file_path = 'raw.txt'
    min_length = 4
    extract_utf8_strings(binary_file_path, output_file_path, min_length)

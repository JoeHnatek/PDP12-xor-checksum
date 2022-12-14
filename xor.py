"""
MIT License

Copyright (c) 2022 Joseph Hnatek

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import sys
import os

PAD = b'\x80'   # Padding byte
LOC = b'\x40'   # start Line Of Coding

def getData(filepath: str) -> list:
    """
    Opens filepath in read-binary mode
    Read 2 bytes at a time (12bit words)
    Skip LOC and PAD bytes.
    """
    data = []
    with open(filepath, mode="rb") as f:    # Open file in binary read mode
            while(word := f.read(2)):   # Read word by word
                if(PAD not in word):    # Ignore padding
                    if LOC in word:
                        continue
                    else:
                        binary_value = ''
                        for e in word:
                            # Convert hex to binary,
                            # Strip python bin prefix 0b
                            # Fill left most bits with 0 to ensure a length of 8
                            # Strip meta-data bits 7 & 8
                            binary_value += bin(e)[2:].zfill(8)[2:]
                        data.append(binary_value)

    return data

def xor(data: list) -> int:
    """
    Compute XOR checksum
    """
    result = 0
    for e in data:
        result ^= int(e,2)

    return result

def bin_to_octal(bin_octals: list) -> str:
    """
    Convert binary to octal
    Return string of octal digits for PDP-12
    """
    octals = ""
    for b in bin_octals:    # Convert 3bit binary to octal for PDP-12 readability
        octals += str(int(b,2))

    return octals

def main(filepath: str) -> None:

    data = getData(filepath)

    result = xor(data)

    binary_checksum = bin(result)[2:].zfill(12)  # Convert decimal to 12bits
    bin_octals = [binary_checksum[i:i+3] for i in range(0, len(binary_checksum), 3)]    # Convert 12bits to 4 3bits

    octal = bin_to_octal(bin_octals)

    printStats(filepath, result, binary_checksum, octal)

def printStats(filepath: str, decimal: int, binary: str, octal: str):
    print(f"===== Checksum for {filepath} =====")
    print(f"Decimal:\t{decimal}")
    print(f"Binary:\t{binary}")
    print(f"Octal:\t\t{octal}")

if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
    except:
        raise Exception("Missing file path in arguments. python3 xor.py file")

    if not os.path.isfile(filepath):
        raise FileNotFoundError(filepath)

    ext = filepath[-3:]

    if ext.lower() == 'rim':
        main(filepath)
    else:
        raise Exception(f"{filepath} is not in the proper format (.rim)")

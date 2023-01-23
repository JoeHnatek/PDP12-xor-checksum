# PDP12-xor-checksum
Project for Operating Systems. Compute the XOR checksum of a rim file intended for the PDP12.

## Requirements
- Python3 3.11.0
> Can be used with earlier verions of python by replacing walrus operators and type hints.

## Run
`python3 xor.py <file>`
> File must be in the rim format.

## Example
`python3 xor.py bootloader.rim`
```
===== Checksum for bootloader.rim =====
Decimal:        1100
Binary: 010001001100
Octal:          2114
===== Addresses and Instructions =====
Address     Instruction bAddress     bInsturction
0017        0017        000000001111 000000001111
0020        7240        000000010000 111010100000
0021        3017        000000010001 011000001111
0022        1045        000000010010 001000100101
0023        6416        000000010011 110100001110
0024        6411        000000010100 110100001001
0025        5024        000000010101 101000010100
0026        6402        000000010110 110100000010
0027        6401        000000010111 110100000001
0030        5027        000000011000 101000010111
0031        6406        000000011001 110100000110
0032        7106        000000011010 111001000110
0033        7006        000000011011 111000000110
0034        7510        000000011100 111101001000
0035        5000        000000011101 101000000000
0036        7006        000000011110 111000000110
0037        6401        000000011111 110100000001
0040        5037        000000100000 101000011111
0041        6404        000000100001 110100000100
0042        3417        000000100010 011100001111
0043        5026        000000100011 101000010110
0044        7605        000000100100 111110000101
0045        0100        000000100101 000001000000
```
## Note
I make no promises that this code works as intended :)

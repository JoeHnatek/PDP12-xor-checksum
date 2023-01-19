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
```
## Note
I make no promises that this code works as intended :)

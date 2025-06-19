Investigative Reversing 3

Author: Santiago C/Danny T

Description

We have recovered a binary and an image See what you can make of it. There should be a flag somewhere.

Hints 
You will want to reverse how the LSB encoding works on this problem.

![image](https://github.com/user-attachments/assets/1c827a09-489e-40e7-b0bd-f109508dfd9a)


This is a 64-bit ELF executable file, for Linux operating systems on x86-64 architecture.

PIE (Position Independent Executable): the program can be loaded at any memory address, increasing security (ASLR).

Dynamically linked: the program uses shared libraries (libc, etc.).

Interpreter: /lib64/ld-linux-x86-64.so.2 is the default ELF loader on Linux.

Not stripped: not stripped of debug information such as symbols, easy to analyze with Ghidra.

**The program is trying to open the flag.txt file but cannot find it, resulting in an error.**

![image](https://github.com/user-attachments/assets/0497bb79-6c25-4603-b48a-d339c52404d9)


Reverse Engineering with Ghidra
After opening the mystery with Ghidra, the main() function reveals a few important things:

local_60 = fopen("flag.txt","r");
local_58 = fopen("original.bmp","r");
local_50 = fopen("encoded.bmp","a");
flag.txt: contains the original flag

original.bmp: the original image

encoded.bmp: where the encoded image (output image) will be written

Add header
The program copies the first 723 bytes from original.bmp to encoded.bmp:
local_68 = 0x2d3;

for (int i = 0; i < local_68; i++) {
fputc(local_7e, local_50);
fread(&local_7e, 1, 1, local_58);
}

Embed flags
The data embedding loop runs 100 times:
for (local_74 = 0; local_74 < 100; local_74++) { 
if ((local_74 & 1) == 0) { 
for (local_70 = 0; local_70 < 8; local_70++) { 
local_7d = codedChar(local_70, flag_char, bmp_byte); 
fputc(local_7d, local_50); 
fread(&bmp_byte, 1, 1, local_58); 
} 
} else { 
fputc(bmp_byte, local_50); 
fread(&bmp_byte, 1, 1, local_58); 
}
}
Each flag character is encoded into 8 consecutive bytes in the image through the LSB (least significant bit).

Interspersed between characters is 1 byte of the image that remains intact.

That is:

50 characters × 8 = 400 embedded bytes

50 bytes of the image remain intact

Total: 450 bytes from offset 0x2d3 which is the data embedding area

Embedding technique: LSB Steganography
The value of each bit in each flag character is embedded in the LSB bit of 8 consecutive image bytes.

Example:
Flag char = 'A' = 01000001 (binary)

→ Bit 0 into byte 1
→ Bit 1 into byte 2
→ ...
→ Bit 7 into byte 8

From the above analysis, we can reproduce the reverse logic using the following code:

![image](https://github.com/user-attachments/assets/e8663770-2813-4d66-b84e-5f1e35b1e9d4)

we will run this code to find flag 

![image](https://github.com/user-attachments/assets/67f77ea9-7e85-4b28-a0c9-d1193a99127c)

we found the flag




















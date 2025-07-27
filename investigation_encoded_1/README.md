**investigation_encoded_1**

Author: Santiago C

Challenge Type: Digital Forensics / Reverse Engineering

Description:

We have recovered a binary and 1 file: image01. See what you can make of it.
NOTE: The flag is not in the normal picoCTF{} format.\

<img width="1851" height="840" alt="image" src="https://github.com/user-attachments/assets/1e3c412f-568d-49b0-a539-969e0431fb3b" />

The problem is given a file containing characters and an .ELF file, so we will use the Ghdra tool to analyze the code.

we see main()
Read flags from file

Open output file

Call encode() to encode

<img width="1703" height="746" alt="image" src="https://github.com/user-attachments/assets/38f99660-157a-4211-9b0e-a34e7e974588" />

encode()

Process each character of the flag

Get bits from secret according to matrix

Write each bit to output using save()

Convert each character in the flag into a bit string and write it to the output file.

<img width="1698" height="438" alt="image" src="https://github.com/user-attachments/assets/9dab0178-19d5-466d-8ce2-65939cba1a09" />


save(byte bit)

Collect 8 bits → 1 byte

Write bytes to output file

<img width="1646" height="451" alt="image" src="https://github.com/user-attachments/assets/b01072b6-9dda-41a5-89af-2d57e84a7a92" />

lower(byte c)

If c is in 'A' to 'Z' → add 0x20 to lowercase (A→a)

Otherwise → keep as is

<img width="1676" height="505" alt="image" src="https://github.com/user-attachments/assets/238dbb79-6f37-4986-82e1-336e280f5ba4" />

isValid(char c)

<img width="1697" height="388" alt="image" src="https://github.com/user-attachments/assets/7addb1d8-e851-458d-b408-ce59f3a6e653" />

getValue(int index)

Get the bit at index position in secret:
<img width="1533" height="300" alt="image" src="https://github.com/user-attachments/assets/b29cd5b8-c100-4eda-9dc6-b4a84b179fe3" />
<img width="1560" height="460" alt="image" src="https://github.com/user-attachments/assets/0194d6f2-ecad-4e9f-83a3-721ec3a1ca8e" />

and see the secret[] and matrix[]

<img width="472" height="79" alt="image" src="https://github.com/user-attachments/assets/58b5654a-fee0-4add-9e09-f204cb7d0c01" />

Use a.py to reverse and restore the flag.
we see the flag 


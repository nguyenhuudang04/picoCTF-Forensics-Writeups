**Investigative Reversing 2**

Author: Santiago C/Danny T

Description
We have recovered a binary and an image See what you can make of it. There should be a flag somewhere.
Hints 
Try using some forensics skills on the image
This problem requires both forensics and reversing skills
What is LSB encoding?

<img width="1685" height="765" alt="image" src="https://github.com/user-attachments/assets/92203bca-75cd-46f5-8644-7f2115a7b003" />

Use Ghidra tool to analyze mystery file, in CTF form like this, we will usually analyze code file 
and from there reverse image file to find flag

<pre lang="markdown"> ```undefined8 main(void)

{
  size_t sVar1;
  long in_FS_OFFSET;
  char local_7e;
  char local_7d;
  int local_7c;
  int local_78;
  int local_74;
  int local_70;
  undefined4 local_6c;
  int local_68;
  int local_64;
  FILE *local_60;
  FILE *local_58;
  FILE *local_50;
  char local_48 [56];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_6c = 0;
  local_60 = fopen("flag.txt","r");
  local_58 = fopen("original.bmp","r");
  local_50 = fopen("encoded.bmp","a");
  if (local_60 == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (local_58 == (FILE *)0x0) {
    puts("original.bmp is missing, please run this on the server");
  }
  sVar1 = fread(&local_7e,1,1,local_58);
  local_7c = (int)sVar1;
  local_68 = 2000;
  for (local_78 = 0; local_78 < local_68; local_78 = local_78 + 1) {
    fputc((int)local_7e,local_50);
    sVar1 = fread(&local_7e,1,1,local_58);
    local_7c = (int)sVar1;
  }
  sVar1 = fread(local_48,0x32,1,local_60);
  local_64 = (int)sVar1;
  if (local_64 < 1) {
    puts("flag is not 50 chars");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  for (local_74 = 0; local_74 < 0x32; local_74 = local_74 + 1) {
    for (local_70 = 0; local_70 < 8; local_70 = local_70 + 1) {
      local_7d = codedChar(local_70,(int)(char)(local_48[local_74] + -5),(int)local_7e);
      fputc((int)local_7d,local_50);
      fread(&local_7e,1,1,local_58);
    }
  }
  while (local_7c == 1) {
    fputc((int)local_7e,local_50);
    sVar1 = fread(&local_7e,1,1,local_58);
    local_7c = (int)sVar1;
  }
  fclose(local_50);
  fclose(local_58);
  fclose(local_60);
  if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
    return 0;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
} ``` </pre>



Main() function:

Open flag.txt, original.bmp, encoded.bmp

Copy the first 2000 bytes from original.bmp to encoded.bmp

Read 50 characters from flag.txt

For each character, loop through each bit (8 times), encode the bit and write to encoded.bmp

Finally write the rest of original.bmp to encoded.bmp

✅ Comment: With the hint being LSB encoding and the flag data hidden in the LSB bit of each byte after offset 2000,
each character occupies 8 bytes (8 bits).

****<img width="1713" height="668" alt="image" src="https://github.com/user-attachments/assets/a49963a4-cc81-4a87-9118-91c74b3b7896" />

The codedChar function works as follows:
Shift the ch bit to the right bit_index times.

Take the LSB of the result, overwrite the LSB of cover_byte.

➡️ This is the LSB Steganography technique - hiding data in the last bit of each image byte.


<img width="897" height="174" alt="image" src="https://github.com/user-attachments/assets/2ab809b2-04f9-4641-baab-7cbd5736a66f" />


we have the decrypt code above a.py
we found the flag

**Investigative Reversing 0**
Author: Danny Tunitis

Description
We have recovered a binary and an image. See what you can make of it. There should be a flag somewhere.

Hints 
Try using some forensics skills on the image

This problem requires both forensics and reversing skills

This problem requires both forensics and reversing skills

![image](https://github.com/user-attachments/assets/da859318-d157-4dfa-8351-84a0500b9f72)

Shows that there are 26 bytes of embedded data after the IEND section of the PNG image.

This is a common sign of steganography (hiding data into an image file using append techniques).

![image](https://github.com/user-attachments/assets/242cea19-7763-41b7-8ba4-cdc6122477b4)

not stripped: Binary still has symbol information → easy to parse with Ghidra or IDA


![image](https://github.com/user-attachments/assets/616d35e4-81c7-4083-a8fc-f908a18c7838)

🔍 Conclusion: What does this program do?
Purpose
📥 Read data Read 26 bytes from flag.txt file
🧪 Transform data Some bytes are +5, -3 to "mess up" the data
🖼️ Write data Write the result to the end of the mystery.png file (Stego format)
🛡️ Protection Use stack canary to prevent memory overflow

![image](https://github.com/user-attachments/assets/f247e5d2-7447-4ad3-8f45-a25a45a64726)

Based on that we will write python code to find flag

![image](https://github.com/user-attachments/assets/d2bdaaa8-d9bc-4750-8d9f-134abe15c075)

we found the flag 

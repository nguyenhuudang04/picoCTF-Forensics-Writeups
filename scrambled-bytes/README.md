**scrambled-bytes**
Author: kfb

Description
I sent my secret flag over the wires, but the bytes got all mixed up!

Challenge Endpoints

Download capture.pcapng	capture.pcapng
Download send.py	send.py

let's do the lab right now 

![image](https://github.com/user-attachments/assets/8674000d-3068-4b9c-939b-5a18c7b60bf8)

- see file send.py
![image](https://github.com/user-attachments/assets/7f513c0e-07c0-4ac6-a93d-6aa04d2b5854)

Each byte in the input file is XORed with a random value in [0, 255]

Then the order is shuffled using random.shuffle

Finally sent over UDP, using a random source port

If we know random.seed(...), we can:

Restore the shuffle order

Regenerate the XOR key sequence

Decode and rearrange the flags in the correct order

![image](https://github.com/user-attachments/assets/fe7c545e-532e-4e12-835d-32bd7775de35)

Find the time of calling random.seed(...) = timestamp of the first packet = 1614044650.913789387 . send = 1614044650


![image](https://github.com/user-attachments/assets/3f70f990-d7f1-4f01-9084-ce9d41a77e24)

This script is used to decode a scrambled and XOR-encoded data string, recorded in the network file capture.pcapng.

The original data is sent via UDP packets, each byte has been:

XORed with a random value

Randomly position-shuffled

All based on a random.seed(...) from the timestamp.

![image](https://github.com/user-attachments/assets/f4a38fbe-be84-4e7f-ace5-f1135bd799be)


Step-by-step Explanation (English)

🔹 Step 1: Check the file type

🔹 Step 2: Rename the file to have a .png extension

🔹 Step 3: View the image

finaly see the flag 












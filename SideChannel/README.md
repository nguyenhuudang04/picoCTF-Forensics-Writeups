SideChannel

Author: Anish Singhani

Description

There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?

Download the PIN checker program here pin_checker

Additional details will be available after launching your challenge instance.

Hints 

Read about "timing-based side-channel attacks."

Attempting to reverse-engineer or exploit the binary won't help you, you can figure out the PIN just by interacting with it and measuring certain properties about it.

Don't run your attacks against the master server, it is secured against them. The PIN code you get from the pin_checker binary is the same as the one for the master server.

start now

![image](https://github.com/user-attachments/assets/65bf857f-0294-4efe-8315-8e78f2f9c0ac)

This is an executable file. I will grant it permission to run the file.

![image](https://github.com/user-attachments/assets/6a11c726-ec45-4a4d-9522-742093ccaa1d)

![image](https://github.com/user-attachments/assets/4ca4d366-5512-40fd-80e1-6472f2a4bddf)

We need to enter 8 numbers into the file.

Hints
Read about "timing-based side-channel attacks."

it means timing related

![image](https://github.com/user-attachments/assets/6271f7d9-f257-4bf9-be95-edf017bed440)


We see that the loading time between numbers is different, 

so we need to determine which numbers have a long loading time and then we will record them.

![image](https://github.com/user-attachments/assets/a6dba047-f1ec-41a9-91fd-dafa7a71e2ee)

we see the code a.py found the password is 48390513


![image](https://github.com/user-attachments/assets/be6c233a-4b18-456f-b4ca-b04b7034657e)

we found the flag







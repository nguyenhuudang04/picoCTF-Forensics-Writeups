FindAndOpen

Author: Mubarak Mikail

Description
Someone might have hidden the password in the trace file.
Find the key to unlock this file. This tracefile might be good to analyze.

Hints 
Download the pcap and look for the password or flag.Don't try to use a password cracking tool, there are easier ways here.

let's start right now
Here the problem requires us to find the password in the .pcap file to unlock the zip file.
we will check each packet to see what it contains

![image](https://github.com/user-attachments/assets/ce5ecbd8-9f4b-4c7a-bfa3-5b9e4463c175)

![image](https://github.com/user-attachments/assets/cbef359f-f1e1-45bf-8912-5e72d9b66552)

oh we see the data in this packet looks like a base64 encoded code
we will try to decode

![image](https://github.com/user-attachments/assets/9ffd8ab5-d0d7-4763-9abd-db7dffd31b0d)

this is password to unzip file flag

![image](https://github.com/user-attachments/assets/fdd52ba4-ca3c-444f-bf9e-9b6977ed620b)


we will use it to unlock the file , finally we found the flag

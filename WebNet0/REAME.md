**WebNet0**

Author: Jason

Description
We found this packet capture and key. Recover the flag.

**Hints **

Try using a tool like Wireshark.

How can you decrypt the TLS stream?

![image](https://github.com/user-attachments/assets/a3f2018c-ba95-4729-bee0-40dc04b12744)

we see it includes 1 .pcap file and a key file to decrypt

![image](https://github.com/user-attachments/assets/ffcac10d-7cb4-4d28-aeb8-4c6d85eca4d3)


![image](https://github.com/user-attachments/assets/66c6152e-e0dd-4942-9499-3cd941a339aa)

we see nothing when follow TLS

With TLS/SSL decryption, you need:

Private key .key corresponding to the server in the packet (you have picopico.key).

The packet must use RSA key exchange (TLS 1.2 or lower) → because from TLS 1.3 it cannot be decrypted with private key.

![image](https://github.com/user-attachments/assets/da2fd1b5-7372-497c-b6a5-af8f2ebe451e)

How to configure in Wireshark:

Go to menu: Edit → Preferences.

Open: Protocols → TLS

In the RSA Keys List section

Click Edit.

Add:



![image](https://github.com/user-attachments/assets/83634560-c09b-4943-b3c5-c15f8efd6953)



194 / 5.000
IP Address Port Protocol Key File Path
128.237.148.23 443 http /home/kali/Desktop/CTF/picopico.key

👉 Need the correct key file path and correct server IP (128.237.148.23), port (443), protocol: http.


![image](https://github.com/user-attachments/assets/45afd122-0393-46da-8bb4-6ae60dd0283c)


Select an Application Data packet.

Right click → select Follow → TLS Stream

finally we found Flag




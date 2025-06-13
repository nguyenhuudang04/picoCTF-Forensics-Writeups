🔍 CTF Writeup: Mob Psycho

Decription :

Can you handle APKs?

Download the android apk here.

Hint: Did you know you can unzip APKs?,Now you have the whole host of shell tools for searching these files.


![image](https://github.com/user-attachments/assets/7e2b63a4-e3b5-4c9d-992a-6df97105862f)

- Unzip  the file apk: unzip mobpsycho.apk

![image](https://github.com/user-attachments/assets/95379508-9a6c-4dc6-93a4-758e1154c759)

- web can  find the key word is "flag" in all file and folder : strings * | grep "flag" 

![image](https://github.com/user-attachments/assets/2799cfd8-d797-47a2-b1cd-01282661b3cd)

- we founded the  file flag.txt

![image](https://github.com/user-attachments/assets/9003f438-c3f2-4ae8-9ce9-72ab0c4505bd)

we  read the file with cat tool but That string looks like a hex-encoded flag

![image](https://github.com/user-attachments/assets/3ddc1a48-8c04-48a2-a6d7-9797f31053f8)



Use this command in your terminal to decode it: 



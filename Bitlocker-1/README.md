# 🔐 picoCTF - Bitlocker-1
Jacky is not very knowledgeable about the best security passwords and used a simple password to encrypt their BitLocker drive. See if you can break through the encryption!  
 **Hint:** _Hash cracking_
Dowload file here : https://challengefiles.picoctf.net/c_verbal_sleep/9e934e4d78276b12e27224dac16e50e6bbeae810367732eee4d5e38e6b2bb868/bitlocker-1.dd

![image](https://github.com/user-attachments/assets/ea2dd506-00e9-4b6e-a08b-a9250284ba56)

This is a BitLocker-encrypted volume, but the content cannot be mounted or accessed at the moment."
fdisk -l bitlocker-1.dd   
![image](https://github.com/user-attachments/assets/79597aa8-48b0-4771-ae5e-2a0b7fffbc91)

Use the bitlocker2john tool to extract the hash of the encrypted password for brute-force attacks."
bitlocker2john -i bitlocker-1.dd > hash1.txt
![image](https://github.com/user-attachments/assets/52b095be-ad35-4b9f-a5f9-6ba18b7f2d1f)

![image](https://github.com/user-attachments/assets/5806b7f6-845b-4f9a-a7c5-3e46d47b96dd)
"You can crack the password using a wordlist. One commonly used wordlist is 'rockyou.txt', which you can easily find on Google
The password was found.
John displays this line when a match is found for the hash.
The question mark (?) appears because the BitLocker format may not be 100% supported, as warned at the beginning.
john --format=bitlocker hash1.txt --wordlist=/home/kali/Desktop/labdis/dictionary2.txt

![image](https://github.com/user-attachments/assets/743a31fd-5f72-4a06-a467-0a8ace246497)

Create a folder to contain the disk file for further analysis
sudo mkdir sudo mkdir /mnt/bitlocker                 
sudo mkdir /mnt/decrypted

![image](https://github.com/user-attachments/assets/8739ed6e-5b05-46f5-a147-5049cac96417)

Decrypt the disk using BitLocker.
sudo dislocker -V bitlocker-1.dd -ujacqueline -- /mnt/bitlocker
![image](https://github.com/user-attachments/assets/35bccd1f-ca0a-42cc-8c0b-e1e5677fbf63)

Finally, go to the folder and use cat to view the flag

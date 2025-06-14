DISKO 2
Author: Darkraicg492

Description
Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone!
Download the disk image 

Hints 
How can you extract/isolate a partition?

let's start riht now 

![image](https://github.com/user-attachments/assets/f0cffe41-649c-4c4c-bc79-11b6832bffc1)

first we will check the file,File disko-2.dd has 2 partitions:  fdisk -l disko-2.dd   

Partition 1: Linux (Id=0x83), starting from sector 2048, 51200 sectors long.

Partition 2: FAT32 (Id=0xb), starting from 53248, 65536 sectors long.

![image](https://github.com/user-attachments/assets/cbbc6f1c-f988-4d7e-b44e-ffa577b4efc9)

extract memory partition :dd if=disko-2.dd of=part1.img bs=512 skip=2048 count=51200


![image](https://github.com/user-attachments/assets/d3c6c8b2-eb01-4db5-8d58-dfa1cd1c62ed)
![image](https://github.com/user-attachments/assets/20f4f2a5-93ec-4beb-9a46-750f7f6799e3)

Search for flags in memory partition and we found the Flag: strings part1.img | grep "picoCTF"


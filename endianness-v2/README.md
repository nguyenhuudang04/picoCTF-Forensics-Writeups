**Endianness-v2**

Description
Here's a file that was recovered from a 32-bits system that organized the bytes a weird way. We're not even sure what type of file it is.
Download it here and see what you can get out of it

![image](https://github.com/user-attachments/assets/28a62793-f7ca-403c-974b-598408edaa8d)

 we check the file challengefile it only see the Data

![image](https://github.com/user-attachments/assets/3c3e03db-3dbc-4e83-a89c-a3e47d4f3e8b)

![image](https://github.com/user-attachments/assets/4ffde9f1-3589-47c7-a142-e00a930681d5)

we see it is a jpeg file, but the position of 4 bytes has been changed, We need to reposition the bytes correctly.
 
![image](https://github.com/user-attachments/assets/a1a365d4-fb63-4399-a0a5-abb232110dad)

we will run python code to swap position

![image](https://github.com/user-attachments/assets/c6fcf3c7-3f8f-4046-b408-85abfe1b147e)
 
finaly, we find the flag 



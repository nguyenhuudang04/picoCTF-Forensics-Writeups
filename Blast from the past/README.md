🕰️ picoCTF - Blast from the past


Description
The judge for these pictures is a real fan of antiques. Can you age this photo to the specifications?
Set the timestamps on this picture to 1970:01:01 00:00:00.001+00:00 with as much precision as possible for each timestamp. In this example, +00:00 is a timezone adjustment. Any timezone is acceptable as long as the time is equivalent. As an example, this timestamp is acceptable as well: 1969:12:31 19:00:00.001-05:00. For timestamps without a timezone adjustment, put them in GMT time (+00:00). The checker program provides the timestamp needed for each.

- Download file here: https://artifacts.picoctf.net/c_mimas/91/original.jpg


![image](https://github.com/user-attachments/assets/b61de0f1-46d4-4bbd-961d-bb17707e08d6)

Check file image with exiftool: exiftool original.jpg 


![image](https://github.com/user-attachments/assets/83645ef6-7b37-45c0-8396-004fe22bc161)

- Next, we will set time for immage:
  exiftool \
  -DateTimeOriginal="1970:01:01 00:00:00" \
  -CreateDate="1970:01:01 00:00:00" \
  -ModifyDate="1970:01:01 00:00:00" \
  -TrackCreateDate="1970:01:01 00:00:00+00:00" \
  -MediaCreateDate="1970:01:01 00:00:00+00:00" \
  -SubSecTimeOriginal="001" \
  -OffsetTimeOriginal="+00:00" \
  -OffsetTime="+00:00" \


![image](https://github.com/user-attachments/assets/07bf21a4-d3d2-4f89-9f1b-82499691a011)\

Check if the image meets the requirements


![image](https://github.com/user-attachments/assets/80e3ee1b-53b6-4c60-9167-e1fde4ea7802)

As seen in the checker, we failed because the Samsung-specific tag Time Stamp still had the original value.

So let’s fix it manually!


![image](https://github.com/user-attachments/assets/e1b6b7df-87c2-4589-bc45-6c3a3c2b6c04)

![image](https://github.com/user-attachments/assets/a8c53c9a-2d53-4a09-94fa-4644b8b25deb)

 we can see ofset of Samsung: TimeStamp is 31 37 30 30 35 31 33 31 38 31 34 32 30  
we will change it to " 30 30 30 30 30 30 30 30 30 30 30 30 31 "
hexedit original_modified.jpg


![image](https://github.com/user-attachments/assets/aa6be170-240e-4504-b6fc-22b34d79ba1f)

finally we check the time again and get the flag

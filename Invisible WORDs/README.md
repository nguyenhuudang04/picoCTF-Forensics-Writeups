
**Invisible WORDs**
**Author: LT 'syreal' Jones**

Description
Do you recognize this cyberpunk baddie? We don't either. AI art generators are all the rage nowadays ,
which makes it hard to get a reliable known cover image.
But we know you'll figure it out. The suspect is believed to be trafficking in classics.
That probably won't help crack the stego, 
but we hope it will give motivation to bring this criminal to justice!

**Hint**
Something doesn't quite add up with this image...

How's the image quality?

<img width="1377" height="754" alt="image" src="https://github.com/user-attachments/assets/597747e8-9519-4309-94c0-71c23a6b99ab" />

Since the suggestion is related to the image, we should look at the image quality.


<img width="1919" height="873" alt="image" src="https://github.com/user-attachments/assets/de703322-3671-4659-a147-2f1c9444d67e" />

We immediately realized that the file had a very familiar symbol like a zip file hidden inside.

<img width="1901" height="668" alt="image" src="https://github.com/user-attachments/assets/c65acd42-31b1-41d4-a84c-4a02dabb1839" />

here is the zip file header hidden in .bmp

<img width="1572" height="307" alt="image" src="https://github.com/user-attachments/assets/ac916d8f-27b0-4407-aeea-69ebda06eea1" />

and we also notice that every 2 bytes, 2 more bytes of garbage are inserted into the example 50 4b 95 52 03 04
but the correct header of the zip file format is 50 4b 03 04


from above will have code to run data collection and export to file

<img width="1072" height="655" alt="image" src="https://github.com/user-attachments/assets/60bcc5d4-a067-4d45-bdb7-0878c57d15b3" />

Run the Python script: python a.py
Rename the out file to out.zip so programs like unzip recognize the format.

<img width="1045" height="729" alt="image" src="https://github.com/user-attachments/assets/37778e35-f29a-4671-8830-8f8357e19645" />

will try to unzip with 7z tool
Unzipped file: ZnJhbmtlbnN0ZWluLXRlc3QudHh0
and proceed to read that file and find the flag


<img width="1183" height="141" alt="image" src="https://github.com/user-attachments/assets/60905ce3-e61b-4515-89a9-5e1bb3050d3c" />

we found it


               


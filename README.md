# Automate-Tags
Project Description:  
This project is used automate tasks to bulk modify tags for the image files (.jpg) , video files (.mp4) based on the folder name. This project is a part of google bulk up-loader which is under development. The drawbacks of the present google photos up-loader it doesn't allow images having same resemblance. Such drawback can be nullified by adding "Title" tag to files. Since, It is not an easy task to add tags to all files a script has been developed in python to automate the task. This script adds title tag to all files present in folder and sub directories followed by image count for image files and video count for video files. Hence, The tagged files having same resemblance can be uploaded successfully.

Required Softwares and Tools:
  Python 3 : https://www.python.org/downloads/
  FFMPEG: https://ffmpeg.org/download.html
  EXIFTOOL: https://www.sno.phy.queensu.ca/~phil/exiftool/

Installing FFMPEG and EXIFTOOL (Windows OS only):
1) Download FFMPEG from the above link.
2) Extract the zip file using 7zip. (7zip Download link: https://www.7-zip.org/download.html)
3) Open the extracted folder and copy all files present in the folder.
4) Create a folder named "FFMPEG" in "Local Disk C (C:\)" and paste all files in the folder.
5) Open the command prompt as administrator and set the path of current directory using the command below.
    setx path "%path%;C:\FFMPEG\bin"
6) Download the EXIFTOOL (Windows Executable) from the above link.
7) Extract the zip file and rename "exiftool(-k).exe" to "exiftool.exe".
8) Move the "exiftool.exe" tool to "C:\FFMPEG\bin".

If there is any difficulty in installing files using above mentioned steps, please refer to the links below.
  Installing Python: https://www.howtogeek.com/197947/how-to-install-python-on-windows/
  Installing FFMPEG: https://m.wikihow.com/Install-FFmpeg-on-Windows
  Installing EXIFTOOL: https://www.sno.phy.queensu.ca/~phil/exiftool/install.html

Usage:
1) Copy the Tags.py file to the folder in which the pictures and videos are present.
2) Open command prompt and navigate to the folder in which Tags.py file is present
   (To Navigate via command prompt, refer the following site: https://www.digitalcitizen.life/command-prompt-how-use-basic-commands)
3) Run the file using the command below:
    python Tags.py
4) Wait until the script is executed.

After running the above command, the files present in the current directory and it's sub directoris gets tagged respectively.

Errors:
1) FileNotFoundError: [WinError 2] The system cannot find the file specified: 'modified_video-file-name.mp4' -> 'video-file-name.mp4'
      The above error indicates that the path to "FFMPEG" has not been initialised properly. Here "video-file-name" refers to the name         of an video file. Please refer "Step 5" in "Installing FFMEPG and EXIFTOOL (Windows OS only)" or the following link:                     https://m.wikihow.com/Install-FFmpeg-on-Windows.
2) FileNotFoundError: [WinError 2] The system cannot find the file specified: 'image-file-name.jpg_original'
      The above error indicates that the path to "EXIFTOOL" has not been initialised properly. Here "image-file-name" refers to the name       of an image file. Please refer "Step 5" in "Installing FFMEPG and EXIFTOOL (Windows OS only)" or the following link:                     https://www.sno.phy.queensu.ca/~phil/exiftool/install.html.

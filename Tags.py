#Importing Required Modules
import glob
import os, sys
from time import sleep

#Creating Empty List for Image files and Video Files
img_files = []
vid_files =[]

def image_list():
	img_files.clear()			#Clearing list named "img_files".
	for file in glob.glob("*.jpg"):   	#Searching for images in current directory.
		img_files.append(file)         	#Appending Image filenames in list.
	return True

def videos_list():
	vid_files.clear()			#Clearing list named "vid_files".
	for file in glob.glob("*.mp4"):   	#Searching for videos in current directory.
		vid_files.append(file)         	#Appending Video filenames in list.
	return True

def progress(file,len_files, count):
	percentage = ((count/len_files)*100)								#Formula for Calculating Percentage
	progress_bar = "█" * int(percentage/2) + "-" * (50-int(percentage/2))				#Creating progress_bar as per the calculation of percentage.
	progress = "{}[{}/{}]:[{}][{:.1f}%]".format(file,count,len_files, progress_bar, percentage)	#Formatting progress using progress_bar and percentage. 
	return progress

def img_title( folder_name, files):
	count = 1
	for file in files:
		new_name = file.replace(" ","_")
		os.rename(file,new_name)
		execute = "exiftool -Title=\"" + folder_name + " Image " + str(count) + "\" "  + new_name
		#Suppressing Output
		execute = execute + " >nul 2>&1"
		os.system(execute)
		new_name = new_name + "_original"
		os.remove(new_name)
		show_progress = progress("Images", len(img_files), count)
		print(show_progress, end='\r')
		count += 1
	return True

def vid_title(folder_name, vid_files):
	count = 1
	for file in vid_files:
		new_file = file.replace(" ","_")
		os.rename(file,new_file)
		execute = "ffmpeg -i " + new_file + " -c copy -metadata title=\"" + folder_name + " Video " + str(count) +"\" " + "modified_" + new_file
		#Surpressing Output
		execute = execute + " >nul 2>&1"
		os.system(execute)
		os.remove(new_file)
		new_file = "modified_" + new_file
		os.rename(new_file, file.replace("modified_",""))
		show_progress = progress("Videos", len(vid_files), count)
		print(show_progress, end='\r')
		count += 1
	return True

def list_directory():
	file_paths = []
	current_directory = os.getcwd()
	file_paths.append(current_directory)
	#Adding other file directories.
	for dirname, dirnames, filenames in os.walk(current_directory):
		for subdirname in dirnames:
			file_paths.append(os.path.join(dirname, subdirname))
	return file_paths

file_directories=list_directory()

def Tag_files(file_directories):
	for i in range(len(file_directories)):
		#print("Editing Tags in Folders: [{}/{}]".format(int(i),int(len(file_directories))))
		execute = file_directories[i]
		os.chdir(execute)
		show_progress = progress("Folders", len(file_directories), i)
		print("Editing Tags in {}".format(show_progress))
		folder_name = file_directories[i].split(os.sep)[-1]
		#print(folder_name)
		image_list()			  #Adding Image Filename to original list
		videos_list()			  #Adding Video Filename to original list
		print("Total Files : {} (Images: {}, Videos: {} in directory: {})".format(int(len(img_files) + len(vid_files)),int(len(img_files)),int(len(vid_files)), file_directories[i]))
		img_title(folder_name, img_files)
		print("\n")
		vid_title(folder_name, vid_files)
		os.system("cls")

Tag_files(file_directories)

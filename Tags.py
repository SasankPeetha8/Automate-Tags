import glob
import os, sys
from time import sleep

img_files = []
vid_files =[]
#folder_name = os.getcwd().split(os.sep)[-1]

def image_list():					  #Getting Image List
	#img_list = []					  #Empty list to save image filenames in list
	#print("Getting list of Images..") #Showing Process
	img_files.clear()
	for file in glob.glob("*.jpg"):   #Searching for images
		img_files.append(file)         #Appendign Image filename in list
	return True                   #Returning list contents to original list

def videos_list():					  #Getting Video List
	#vid_list = []                     #Empty list to save video filenames in list
	#print("Getting list of Videos..") #Showing Process
	vid_files.clear()
	for file in glob.glob("*.mp4"):   #Searching for videos
		vid_files.append(file)         #Appending Video filename in list
	return True                   #Returning list contents to original list

def progress(file,len_files, count):
	percentage = ((count/len_files)*100)
	progress_bar = "█" * int(percentage/2) + "-" * (50-int(percentage/2))
	progress = "{}[{}/{}]:[{}][{:.1f}%]".format(file,count,len_files, progress_bar, percentage)
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
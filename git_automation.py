######################################################################
## Python script for git-push files in current folder one at a time.
## Github has push cache limit so one at a time ensures all files being sync-ed.
##
#######################################################################
import os
import sys
# Get current dir
pwd = os.getcwd()

# Print title string
title_string = '''
	:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	  
		Syncing all files in the current folder to github...\n
	
	:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
'''
print(title_string)


# Get all files in current folder in a list, alphabetical order
files_arr = sorted(os.listdir(pwd))


print(":: Checking if any files exceeds size limit of 100M (github upload limit) \n")

for i in range(len(files_arr)):
	file = files_arr[i]
	# os.file.getsize returns the file size in bytes; convert it to MB.
	file_size = os.path.getsize(os.path.join(pwd,file))/1024/1024
	if(file_size > 100):
		print("(!) The file \"{}\" has size {} MB, which exceeds github file size limit of 100Mb.\n".format(file,file_size))
		print("(!) Exiting...\n")
		sys.exit()

print(":: File-size check has passed. Starting to uploading now...\n")

# Iterate through these files
for i in range(len(files_arr)):
    file = files_arr[i]
    print("Executing for file: {}\n\n".format(file))
    #git add
    cmd = "git add " + file + " --verbose"
    os.system(cmd)

    # git commit -m "sync"
    cmd = "git commit -m \"sync\" "
    os.system(cmd)

    # git push origin master
    cmd = "git push origin master"
    os.system(cmd)


 

# Python program to explain shutil.copyfile() method  
    
# importing os module  
import os 
  
# importing shutil module  
import shutil 
  
# path 
path = (r"C:\Users\15039\OneDrive\Documents\GitHub\Python_Projects\python_projects")
  
# List files and directories 
# in '/home/User/Documents' 
print("Before copying file:") 
print(os.listdir(path)) 
  
  
# Source path 
source = (r"C:\User\15039\OneDrive\Desktop\FolderC")
  
# Destination path 
destination = (r"C:\User\15039\OneDrive\Desktop\FolderD")
  
# Copy the content of 
# source to destination 
dest = shutil.copyfile(source, destination) 
  
# List files and directories 
# in "/home / User / Documents" 
print("After copying file:") 
print(os.listdir(path)) 
  
# Print path of newly  
# created file 
print("Destination path:", dest) 

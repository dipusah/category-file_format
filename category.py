import os

DOCUMENT = ['txt','csv','docx','pdf','ppt']
IMAGE = ['png']
PYTHON = ['py']
VIDEO = ['mp4']
AUDIO= ['mp3']

BASE_DIR = r'D:\OS' #Raw File

#print(os.listdir(BASE_DIR))

files = os.listdir(BASE_DIR)
#print(files)
for file in files:
    parts = file.split('.')

    if parts[-1] in DOCUMENT:
        folder_path = os.path.join(BASE_DIR,'DOCUMENT')
        #os.path.exists() For checking the existence of file
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        os.rename(                              #Move command
            os.path.join(BASE_DIR,file),        #(source)
            os.path.join(folder_path, file)     #(destination)
        )

    if parts[-1] in VIDEO:
        folder_path3 = os.path.join(BASE_DIR,'VIDEO')
        #os.path.exists() For checking the existence of file
        if not os.path.exists(folder_path3):
            os.mkdir(folder_path3)
        os.rename(                              #Move command
            os.path.join(BASE_DIR,file),        #(source)
            os.path.join(folder_path3, file)     #(destination)
        )
    if parts[-1] in AUDIO:
        folder_path4 = os.path.join(BASE_DIR, 'AUDIO')
        # os.path.exists() For checking the existence of file
        if not os.path.exists(folder_path4):
            os.mkdir(folder_path4)
        os.rename(  # Move command
            os.path.join(BASE_DIR, file),  # (source)
            os.path.join(folder_path4, file)  # (destination)
        )
    if parts[-1] in IMAGE:
        folder_path2 = os.path.join(BASE_DIR, 'IMAGE')
        if not os.path.exists(folder_path2):
            os.mkdir(folder_path2)
            os.rename(
                os.path.join(BASE_DIR, file),
                os.path.join(folder_path2, file)
            )
     if parts[-1] in PYTHON:
        folder_path5 = os.path.join(BASE_DIR, 'PYTHON')
        if not os.path.exists(folder_path5):
            os.mkdir(folder_path5)
            os.rename(
                os.path.join(BASE_DIR, file),
                os.path.join(folder_path5, file)
            )       

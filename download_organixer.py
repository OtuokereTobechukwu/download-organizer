import shutil
import os
import time

# ------------- Store Folder location --------------#
download_loc = 'C:\\Users\\otuokere joy\\Downloads'
# download_loc1 = 'C:\\Users\\otuokere joy\\Untitled Folder 1'
# download_loc2 = 'C:\\Users\\otuokere joy\\minidownload'

# --------- Create folders to keep different file extensions ---------- #
text_dest = 'C:\\Users\\otuokere joy\\Downloads\\Organized downloads\\text_files'
pdf_dest = 'C:\\Users\\otuokere joy\\Downloads\\Organized downloads\\pdf_files'
executables_dest = 'C:\\Users\\otuokere joy\\Downloads\\Organized downloads\\exe_files'
mp4_dest = 'C:\\Users\\otuokere joy\\Downloads\\Organized downloads\\mp4_files'
picture_dest = 'C:\\Users\\otuokere joy\\Downloads\\Organized downloads\\jpg_files'
doc_dest = 'C:\\Users\\otuokere joy\\Downloads\\Organized downloads\\doc_files'
py_dest = 'C:\\Users\\otuokere joy\\Downloads\\Organized downloads\\py_files'
pptx_dest = 'C:\\Users\\otuokere joy\\Downloads\\Organized downloads\\pptx_files'
xcel_dest = 'C:\\Users\\otuokere joy\\Downloads\\Organized downloads\\xcel_files'
pbix_dest = 'C:\\Users\\otuokere joy\\Downloads\\Organized downloads\\pbix_files'

# ----------- storing the file names in a list ------------#
folder_contents = os.listdir(download_loc)

# ----------- creating a list of file extensions ------------#
file_extensions = ['.pdf', '.jpg', '.jpeg', '.docx', '.exe',
                   '.mp4', '.txt', '.pptx', '.ppt', '.xlsx', '.csv',
                   '.py', '.pbix', '.png', '.xls', '.doc' ]

# --------- Check if files exist inside the directory ----------- #
print('Checking for files in the directory ..')
time.sleep(2)

if len(folder_contents) > 0:
    print('Moving files to their locations.....')
    time.sleep(3)
    for file in folder_contents:
        ext = os.path.splitext(file)[-1].lower()
        if ext in file_extensions:
            if ext == '.pdf':
                shutil.move(download_loc + '\\' + file, pdf_dest)
            elif ext == '.jpg' or '.jpeg' or '.png':
                # print('This is an mp3 file')
                shutil.move(download_loc + '\\' + file, picture_dest)
            elif ext == '.txt':
                # print('This is a text file')
                shutil.move(download_loc + '\\' + file, text_dest)
            elif ext == '.docx':
                # print('This is a text file')
                shutil.move(download_loc + '\\' + file, doc_dest)
            elif ext == '.exe':
                # print('This is a text file')
                shutil.move(download_loc + '\\' + file, executables_dest)
            elif ext == '.mp4':
                # print('This is a text file')
                shutil.move(download_loc + '\\' + file, mp4_dest)
            elif ext == '.xlsx' or '.csv':
                # print('This is a text file')
                shutil.move(download_loc + '\\' + file, xcel_dest)
            elif ext == '.pptx':
                # print('This is a text file')
                shutil.move(download_loc + '\\' + file, pptx_dest)
            elif ext == '.py':
                # print('This is a text file')
                shutil.move(download_loc + '\\' + file, py_dest)
            elif ext == '.pbix':
                # print('This is a text file')
                shutil.move(download_loc + '\\' + file, pbix_dest)
        else:
            print('Failed to move', file, '.')
            print('File extension not recognized!')
else:
    print('There are no files to move')




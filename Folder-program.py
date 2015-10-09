import os, sys
import errno
import functools
import Tkinter, tkFileDialog
root = Tkinter.Tk()
#Starting path of the file explorer for Tkinter
myPath = tkFileDialog.askdirectory(parent=root, initialdir="/",
title='Please select where you would like the Directory created')


#using functool we will create a working root dir and its subfolders
def makefolders(root_dir, subfolders):
    concat_path = functools.partial(os.path.join, root_dir)
    map(os.makedirs, map(concat_path, subfolders))

#Creation of folders according to the syllabus. 
root_dir = myPath+"/ELECTR 155--ePortfolio/"# root folder 
subfolders = ('Folder_1-Cover-Page', 'Folder_2-TOC', 'Folder_3-Student-Photo','Folder_4-Self-Introduction','Folder_5-Simple-Starter-Circuit','Folder_6-Circuit-40-2','Folder-7-Relay-Voltage-Comparator','Folder_8-ELENCO-PCB-Miniaturization','Folder_9-Reverse-Engineering-Project','Folder_10-Additional-Multisim','Folder_11-Summary-Page','Completed-Work')
makefolders(root_dir, subfolders)

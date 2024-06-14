import shutil
import os
folder_src = './source/folder/path' #insert source folder path, where source folder is the folder containing raw fastq files
src = os.path.join(os.getcwd(),folder_src )
folder_ds = './destination/folder/path' #insert destination folder path, where destination folder is the folder to write output to
ds = os.path.join(os.getcwd(),folder_ds )

#create a dictionary that will contain the current names, and the new names. 'current_annotation' is the current name, 'new_name' is the correct informative sample name.

dic_b = {"current_annotation_R1"	:	"new_name_R1",
"current_annotation_R2"	:	"new_name_R2",
"current_anotation2_R1"	:	"current_annotation_R1",
"current_annotation2_R2" : "current_annotation2_R2",
"current_annotation3_R1" : "current_annotation3_R1",
"current_annotation3_R2" : "current_annotation3_R2"}

dir_files_src = os.listdir(src)

for file_src in dir_files_src:
    file_ = file_src[:-6]
    if file_ in dic_b.keys():
        n_wext = dic_b[file_]
        new_src = os.path.join(src,file_src)
        new_des = os.path.join(ds,n_wext + ".fastq")
        shutil.copy(new_src,new_des)





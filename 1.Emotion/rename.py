__author__ = 'CC'

import os;



def rename():
    path="C:\\Users\\CC\\Desktop\\0330_comment";
    filelist=os.listdir(path)
    for files in filelist:
        Olddir=os.path.join(path,files);
        if os.path.isdir(Olddir):
            continue;
        filename=os.path.splitext(files)[0];
        filetype = '.txt'
        #filetype=os.path.splitext(files)[1];
        Newdir=os.path.join(path,filename + filetype);
        os.rename(Olddir,Newdir);
rename();


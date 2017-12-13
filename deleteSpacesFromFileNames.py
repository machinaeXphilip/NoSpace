import os, sys
path = './'

alldirs = []
allsubdirs = []
allfiles = []

for subdir, dirs, files in os.walk(path):
    for file in files:

        print os.path.join(subdir, file)
        filename = os.path.join(subdir, file)
        if " " in file:
            #print("space in:" + file);
            newname = file.replace(' ', '')
            newname = os.path.join(subdir,newname)
            print(filename + "  -->  "+newname)
            os.rename(filename, newname)


temp = os.walk(path, topdown=False)
for root, dirs, files in temp:
    for i in dirs:
        dir = os.path.join(root,i)
        #print dir
        newname = dir.split("/")
        tochange = newname[-1]
        changed = tochange.replace(" ","")
        #print changed
        newname[-1] = changed
        newname = "/".join(newname)
        print newname
        os.rename(dir, newname)



#for filename in os.listdir(path):
#   if " " in filename:
#       print("space in:" + filename);
#       newname = filename.replace(' ', '_')
#       os.rename(filename, newname)
 #if filename.endswith('.rtf'):
  #       newname = filename.replace('.rtf', '.txt')
  #       os.rename(filename, newname)

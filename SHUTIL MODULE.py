import shutil

shutil.copy("main.py" , "main2.py")   #IT copies folder
# shutil.copy2(src , dst)
shutil.copytree(".tutorial" , "mytutorial")    #---It copies file
shutil.move(".tutorial/file.file" , "file.file")  #Moves the files from one place to other

shutil.rmtree("mytutorial")   #
shutil.rm("-----")  #
 
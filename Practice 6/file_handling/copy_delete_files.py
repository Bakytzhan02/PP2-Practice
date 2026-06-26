import shutil, os
shutil.copy("sample.txt","sample_backup.txt")
if os.path.exists("sample_backup.txt"):
    os.remove("sample_backup.txt")

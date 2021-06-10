import os

for filename in os.listdir('icons'):
    if filename.endswith(".png"):
        app = filename.split('.')[0]
        app_path = ("~/%s" % app).replace(' ', '\ ')
        file_path = ("icons/%s" % filename).replace(' ', '\ ')
        # requires folderify
        os.system("folderify %s %s" % (file_path, app_path))

print("Done.")

import os

class GlassesCore:
    def getFilesRecursive(self, path):
        files_and_folders = os.listdir(path)
        files_from_folder = [path + '/' + file_or_folder for file_or_folder in files_and_folders if os.path.isfile(path + '/' + file_or_folder)]
        folders_from_folder = [file_or_folder for file_or_folder in files_and_folders if os.path.isdir(path + '/' + file_or_folder)]
        files = files_from_folder
        if folders_from_folder:
            for folder in folders_from_folder:
                files = files + self.getFilesRecursive(path + '/' + folder)

        return files

    def searchOnFiles(self, files, search):
        for file in files:
            file_object = open(file, 'r')
            for num, line in enumerate(file_object, 1):
                if search in line:
                    print ' - ' + file + ' at line : ' + str(num)
            file_object.close()
            
        
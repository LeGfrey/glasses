import os

class GlassesCore:
    def get_files_recursive(self, path):
        files_and_folders = os.listdir(path)
        files_from_folder = [path + '/' + file_or_folder for file_or_folder in files_and_folders if os.path.isfile(path + '/' + file_or_folder)]
        folders_from_folder = [file_or_folder for file_or_folder in files_and_folders if os.path.isdir(path + '/' + file_or_folder)]
        files = files_from_folder
        if folders_from_folder:
            for folder in folders_from_folder:
                files = files + self.get_files_recursive(path + '/' + folder)

        return files

    def search_on_files(self, files, search):
        for file in files:
            file_object = open(file, 'r')
            for num, line in enumerate(file_object, 1):
                if search in line:
                    print ' - ' + file + ' at line : ' + str(num)
                    print line.lstrip()
                    print ' ----------------------------------------------------- '
            file_object.close()
            
        

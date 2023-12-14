import os
from directory import Directory
from file import File

class FileSystem:
    def __init__(self) -> None:
        self.root = Directory("/", "/")
        self.current_directory = self.root

    #To list the contents of the current directory or specified directory
    def ls(self, path=None):
        if(self.current_directory.contents=={}):
            print()
        else:
            current = self.current_directory
            if path!=None:
                if path[0]=='/':
                    path = path[1:]
                try:
                    for folder in path.split("/"):
                        current = current.contents[folder]
                except KeyError:
                    print(f"{path}: No such file or directory")
            for key in current.contents.keys():
                print(key, end=" ")
            print()

    #To create a new directory
    def mkdir(self, path):
        temp = self.current_directory
        for folder in path.split('/'):
            if(folder in temp.contents.keys()):
                print(f"mkdir: cannot create directory '{folder}': already exists")
                break
            else:
                temp.contents[folder] = Directory(folder, os.path.join(temp.dirpath, folder),  temp)
            temp = temp.contents[folder]

    #To change the directory in the terminal
    def cd(self, path):
        temp = self.current_directory
        try:
            for folder in path.split("/"):
                pointer = self.current_directory.contents[folder]
                if(type(pointer)==Directory):
                    self.current_directory = pointer
                else:
                    raise TypeError(f"cd: {path}: Not a directory")
        except TypeError as t:
            self.current_directory = temp
            print(t)
        except KeyError:
            self.current_directory = temp
            print(f'{path}: No such file or directory')

    #To create a new file
    def touch(self, path):
        if(path[0]=='/'):
            path = path[1:]
        folders = path.split("/")
        temp = self.current_directory
        try:
            for folder in folders[:-1]:
                temp = temp.contents[folder]
            name = folders[-1]
            if name not in temp.contents:
                file = File(name)
                temp.contents[name] = file
            else:
                print("File already exists")
        except KeyError as e:
            print("Directory does not exists")

    #To display the contents of the file
    def cat(self, path):
        if path[0]=='/':
            path = path[1:]
        try:
            temp = self.current_directory
            folders = path.split("/")
            for folder in folders[:-1]:
                temp = temp.contents[folder]
            result = temp.contents[folders[-1]].read()
            if(result==None):
                print()
            else:
                print(result)
        except KeyError as k:
            print(f"{path}: No such file or directory")
    
    #To write a content to a file
    def echo(self, path, data):
        if path[0]=='/':
            path = path[1:]
        folders = path.split("/")
        try:
            temp = self.current_directory
            for folder in folders[:-1]:
                temp = temp.contents[folder]
            file = temp.contents[folders[-1]]
            file.write(data)
        except KeyError as k:
            print(f"{path}: No such file or directory")

    #To remove a file or a directory
    def rm(self, path):
        if path[0] == '/':
            path = path[1:]
        folders = path.split("/")
        try:
            temp = self.current_directory
            for folder in folders[:-1]:
                temp = temp.contents[folder]
            del temp.contents[folders[-1]]
        except KeyError as k:
            print (f"{path}: No such file or directory")

    #To move a file or a directory to the specified location
    def mv(self,source,destination):
        if source[0] == '/':
            source = source[1:]
        source_folders = source.split('/')
        file = None
        file_source = None
        try:
            temp = self.current_directory
            for folder in source_folders[:-1]:
                temp = temp.contents[folder]
            file = temp.contents[source_folders[-1]]
            file_source = temp
        except KeyError as k:
            print(f"{source}: No such file or directory")
            return
        if destination[0] == '/':
            destination = destination[1:]
        destination_folders = destination.split("/")
        try:
            temp = self.current_directory
            for folder in destination_folders:
                temp = temp.contents[folder]
        except KeyError as k:
            print(f"{destination}: No such directory")
            return
        del file_source.contents[source_folders[-1]]
        temp.contents[file.name] = file
        
    #To copy the file from the specified directory to the current directory
    def cp(self,source):
        if source[0] == '/':
            source = source[1:]
        source_folders = source.split('/')
        file = None
        file_name = None
        file_data = None
        try:
            temp = self.current_directory
            for folder in source_folders[:-1]:
                temp = temp.contents[folder]
            file = temp.contents[source_folders[-1]]
            file_name = file.name
            file_data = file.read()
        except KeyError as k:
            print(f"{source}: No such file or directory")
            return
        self.current_directory.contents[file_name] = File(file_name)
        file = self.current_directory.contents[file_name]
        file.write(file_data)
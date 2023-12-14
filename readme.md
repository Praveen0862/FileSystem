In-Memory File System Implementation in Python

Introduction:
    The provided Python code implements a basic in-memory file system, allowing users to perform file and directory operations through a command-line interface. The file system maintains a hierarchical structure with directories and files, enabling users to navigate, create, delete, and manipulate files and directories.

File System Structure:

    The file system consists of three main classes: FileSystem, Directory, and File.
    FileSystem serves as the central control point, managing the current directory and executing user commands.
    Directory represents a directory within the file system, containing subdirectories and files.
    File represents a file and includes methods for reading and writing data.

Key Features:

    1)Navigation:
        Users can navigate through directories using the cd command, providing the path to the desired directory.

            >>>cd /path/to/directory


    2)Listing Contents:
        The ls command allows users to list the contents of the current directory or a specified directory.

            >>>ls
            >>>ls /path/to/directory


    3)Creating Directories:
        Users can create directories using the mkdir command, specifying the directory name.

            >>>mkdir new_directory


    4)Creating Files:
        The touch command creates new files in the current directory.

            >>>touch new_file.txt


    5)Viewing and Editing Files:
        Users can view the contents of a file using the cat command and edit files using the echo command.

            >>>cat file.txt
            >>>echo "content" > file.txt


    6)Copying and Moving:
        The cp command copies files from a specified directory to the current directory, while the mv command moves files between directories.

            >>>cp /path/to/source/file.txt
            >>>mv /path/to/source/file.txt /path/to/destination/


    7)Deleting:
        The rm command deletes files or directories from the file system.

            >>>rm file.txt


Usage:

    The user interacts with the file system through a simple command-line interface, entering commands such as ls, mkdir, cd, etc.
    The exit command terminates the file system.

Improvements:

    The code could benefit from enhanced error handling, support for relative paths, and improved user feedback.
    Refactoring some methods for better readability and maintenance is recommended.
    Consider implementing additional interactive shell features for a more user-friendly experience.

Conclusion:
    The in-memory file system implementation provides a functional foundation for basic file and directory operations. By addressing suggested improvements, the code could become more robust, user-friendly, and maintainable. This project serves as a valuable educational resource for understanding file systems and command-line interfaces in Python.



Commands to execute and run the program:

    git clone <url>

    Make sure that the terminal points to my application directory (fileSystem)

    Build Image : docker build -t filesystem

    Run docker image : docker run -ti filesystem
    
from fileSystem import FileSystem

def start():
    fileSystem = FileSystem()

    while True:
        input_command = input(f"${fileSystem.current_directory.dirpath} ").split(" ")

        command_len = len(input_command)

        if input_command[0]=='exit':
            break

        elif input_command[0]=='ls':
            if(command_len>1):
                fileSystem.ls(input_command[1])
            else:
                fileSystem.ls()
        
        elif input_command[0]=='mkdir':
            if input_command[1:]!=[]:
                for folder_name in input_command[1:]:
                    fileSystem.mkdir(folder_name)
            else:
                print("mkdir: missing operand")
        
        elif input_command[0]=='cd':
            if(command_len==2):
                fileSystem.cd(input_command[1])
            elif(command_len>2):
                print("cd: too many arguments")

        elif input_command[0]=='touch':
            fileSystem.touch(input_command[1])

        elif input_command[0]=='cat':
            if(command_len==2):
                fileSystem.cat(input_command[1])

        elif input_command[0]=='echo':
            if input_command[-2] == '>':
                data = " ".join(input_command[1:-2])
                fileSystem.echo(input_command[-1], data[1:-1])
            else:
                print(" ".join(input_command[1:]))
        
        elif input_command[0] == 'rm':
            for command in input_command[1:]:
                fileSystem.rm(command)

        elif input_command[0] == 'mv':
            if (command_len < 3):
                print("mv: Missing source or destination folder")
            elif (command_len == 3):
                fileSystem.mv(input_command[1],input_command[2])
            else:
                print("mv: too many arguments")

        elif input_command[0] == 'cp':
            if (command_len < 2):
                print("cp: Missing directory to copy")
            elif (command_len == 2):
                fileSystem.cp(input_command[1], input_command[2])
            else:
                print("cp: too many arguements")

        else:
            print(f"Command '{input_command[0]}' not found")


if __name__ == '__main__':
    start()

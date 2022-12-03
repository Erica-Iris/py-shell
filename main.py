import os
class Shell():
    def __init__(self):
        self.path = os.getcwd()
        self.command = ''
        self.commands = ['ls', 'cd', 'pwd', 'exit', 'help','mkdir']
    def ls(self):
        os.listdir(self.path)
    def mkdir(self, path):
        os.mkdir(path)
    def help(self):
        print('Available commands:')
        for command in self.commands:
            print(command)
    def cd(self, path):
        os.chdir(path)
        self.path = os.getcwd()
    def pwd(self):
        print(self.path)

    def main(self):
        while True:
            self.command = input(self.path + ' $ ')
            if self.command == 'ls':
                self.ls()
            elif self.command == 'cd':
                self.cd()
            elif self.command == 'pwd':
                self.pwd()
            elif self.command == 'exit':
                self.exit()
            elif self.command == 'help':
                self.help()
            elif self.command == 'mkdir':
                self.mkdir()
            else:
                print('Command not found')
if __name__ == '__main__':
    shell=Shell()
    shell.main()

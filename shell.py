import os
import sys


class Shell():
    """A simple shell written in Python"""

    def __init__(self):
        self.name = "root"
        self.path = os.getcwd()
        self.command = ''
        self.commands = ['ls', 'cd', 'pwd', 'exit', 'help', 'mkdir']

    def execute_command(self, command):
        """Execute a command"""
        try:
            os.system(command)
        except Exception as command_not_found:
            print(command_not_found)
            print('Command not found')

    def ls(self):
        """List the contents of the current directory"""
        os.listdir(self.path)

    def mkdir(self, *names):
        """Create a directory at the given path"""
        for name in names:
            os.mkdir(name)
            print("目录 '%s' 已创建" % name)

    def help(self):
        """Print the help message"""
        print("psh: a simple shell written in Python")
        print('Available commands:')
        for command in self.commands:
            print(command)

    def change_directory(self, path):
        """Change the current directory"""
        os.chdir(path)
        self.path = os.getcwd()

    def pwd(self):
        """Print the current directory"""
        print(self.path)
    # 快速排序

    def quick_sort(self, nums):
        """Quick sort algorithm"""
        if len(nums) <= 1:
            return nums
        pivot = nums[0]
        left = [x for x in nums if x < pivot]
        right = [x for x in nums if x > pivot]
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

    def op_split(self, command):
        """Split the command into a list of operations"""
        op_list = command.split(" ")
        return op_list

    def clear(self):
        """Clear the screen"""
        os.system('clear')

    def run(self):
        while True:
            self.command = sys.argv[1]
            self.args = sys.argv[2:]
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
                self.mkdir(*self.args)
            elif self.command == 'sort':
                self.quick_sort()
            elif self.command == 'clear':
                self.clear()
            else:
                print('Command not found')

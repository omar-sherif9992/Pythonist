import os
import re
import sys

from Projects.Makefile.command import Command
from file_manager import FileManger
from task import Task
from alive_progress import alive_bar
from SyntaxError import SyntaxError
from validator import Validator


class Parser:
    file_manager = FileManger()
    tasks = []
    tasks_index = {}

    def __init__(self, file_name):
        sys.setrecursionlimit(2500)
        self.file_name = file_name
        self.validator = Validator(file_name)
        self.file_content = self.file_manager.read_file(file_name)
        self.path = os.getcwd() + "/" + self.file_name
        self.parse()
        self.validator.check_dependencies(tasks=self.tasks)
        # self.check_cycles()
        self.validator.check_inner_cycles()
        self.validator.check_cycles(self.tasks_index)

    def parse(self):
        '''parses the file and returns a list of commands'''

        task_name = None
        task_dependencies = []
        task_commands = []
        task_line_number = 0

        flag = False
        count = 0
        lines = self.file_content.splitlines()
        with alive_bar(len(lines), bar='filling', title='Parsing lines') as bar:
            for line in lines:
                bar()
                if line.startswith("\n"):
                    continue
                if ":" in line:
                    if task_name is not None:
                        task_count = (len(self.tasks))
                        self.tasks.append(
                            Task(task_name, task_dependencies, task_commands, task_count, task_line_number))
                        self.tasks_index[task_name] = task_count
                        task_dependencies = []

                    dep_line = (line.split(":")[1].strip())
                    task_name = line.split(":")[0].strip()
                    self.validator.validate_task_name(task_name)
                    task_line_number = count
                    if (len(dep_line) > 0):
                        task_dependencies = dep_line.split(" ")
                    task_commands = []
                    flag = True

                elif flag:
                    line_contains_is_hidden = "@" in line.strip()
                    command = Command(line.strip().replace("@", ""), count, line_contains_is_hidden)
                    task_commands.append(command)

                elif not flag:
                    raise SyntaxError(
                        f"Invalid syntax in file:{self.file_name} \n line:{line} \n line number:{count} ",
                        f"suggestion : must define a task name first")
                else:
                    raise SyntaxError(
                        f"Invalid syntax in file:{self.file_name} \n line:{line} \n line number:{count} \n",
                        f"suggestion : must define a task name first")
                count += 1
        if flag:
            self.tasks_index[task_name] = (len(self.tasks))
            self.tasks.append(
                Task(task_name, task_dependencies, task_commands, (len(self.tasks)), task_line_number))

    def __str__(self) -> str:
        str = f"file name : {self.file_name} \n tasks : {self.tasks}"
        for task in self.tasks:
            str = str + task.__str__()
        return str

    def __repr__(self):
        return "Parser of " + self.file_name

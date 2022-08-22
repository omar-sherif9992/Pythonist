import os

from parser import Parser


class Interpreter:
    """for executing task commands"""
    tasks = []
    tasks_index = {}

    def __init__(self, filename):
        try:
            self.parser = Parser(filename)
            # print(self.parser)
            self.tasks = self.parser.tasks
            self.tasks_index = self.parser.tasks_index
            self.interpret()
        except FileNotFoundError as e:
            print(e)
        except SyntaxError as e:
            print(f"Syntax Error occur while parsing: \n {e}")
        except Exception as e:
            print(f"Error occur while parsing: \n {e}")

    def interpret(self):
        while (True):
            try:
                task_index = int(input("\n\t ------------------------------------------------- \n" +
                                       "Execute Your Task by typing it's corresponding number:\n" +
                                       self.get_task_names() +
                                       "\n\t"

                                       "Enter a number :"
                                       ))
                task = self.tasks[task_index]
                self.execute(task)
            except IndexError as e:
                self.clear()
                print("please enter a valid number")
            except Exception as e:
                self.clear()
                print(e)

    def execute(self, task):
        """executes the task dependencies first then the commands"""
        for dependency in task.task_dependencies:
            self.execute(self.tasks[self.tasks_index[dependency]])
        task.execute()

    def get_task_names(self) -> str:
        """returns the task names in a string and their index in the array"""
        task_names = "Task Names :\n"
        count = 0
        for task, index in self.tasks_index.items():
            task_names += f"\t\t\t\t{index}:{task} \n"
            count += 1
        return task_names

    def clear(self):
        i = 0
        while i > 2:
            try:
                if i == 0:
                    # for windows
                    os.system('cls')
                elif i == 1:
                    os.system("clear")
            except:
                pass
            i += 1

from SyntaxError import SyntaxError
from alive_progress import alive_bar
from graph import Graph


class Validator:
    tasks = []
    tasks_index = {}

    def __init__(self, file_name):
        self.file_name = file_name

    def validate_task_name(self, name: str) -> bool:
        """task name first character should be alphanumeric"""
        if name[0].isalpha():
            return True
        else:
            raise SyntaxError("Task name must not start with other than an alphabet character",
                              "suggestion: task name must start with an alphabet")

        ## These 3 functions are used for validating dependencies

    def check_dependencies(self, tasks: list):
        '''checks if the task dependencies exist in the file'''
        self.tasks = tasks
        with alive_bar(len(tasks), bar='filling', title='checking dependencies validation') as bar:
            for task in tasks:
                self.task_dependencies_exist(task.task_dependencies, task.line_number, task.task_name)
                bar()

    def task_name_exist(self, task_name: str) -> bool:
        '''checks if the task name exist in the file'''
        for task in self.tasks:
            if task.task_name == task_name:
                return True
        return False

    def task_dependencies_exist(self, task_dependencies: list, task_line_number: int, task_name: str) -> bool:
        '''checks if the task dependencies exist in the file'''
        for dependency in task_dependencies:
            if not self.task_name_exist(dependency):
                raise SyntaxError(
                    f"Invalid syntax in file:{self.file_name} \n dependency:{dependency} \n line number:{task_line_number}",
                    f"suggestion : task:{task_name} have a dependency called {dependency} that does not exist")
        return True

    def check_inner_cycles(self):
        '''checks if there are any inner cycles in the file'''
        for task in self.tasks:
            for dependency in task.task_dependencies:
                if dependency == task.task_name:
                    raise SyntaxError(
                        f"Invalid syntax in file:{self.file_name} \n line:{dependency} \n line number:{task.line_number}",
                        f"suggestion : remove this dependency {dependency} from this task {task.task_name}")

    def check_cycles(self, task_index: dict):
        '''checks if there are any cycles in the file'''
        self.tasks_index = task_index
        graph = Graph(len(self.tasks))
        with alive_bar(len(self.tasks), bar='filling', title='checking dependencies cycles') as bar:
            bar()
            for task in self.tasks:
                for dependency in task.task_dependencies:
                    graph.addEdge(self.tasks_index[task.task_name], self.tasks_index[dependency])

            flag, source, destination = graph.isCyclic()

            if flag:
                raise SyntaxError(
                    f"Invalid cycle occurred in " + self.tasks[destination].task_name + " --> " + self.tasks[
                        source].task_name,
                    f"suggestion : remove either dependency {self.tasks[source].task_name} from this task {self.tasks[destination].task_name} or "
                    f"{self.tasks[destination].task_name} from this task {self.tasks[source].task_name}")

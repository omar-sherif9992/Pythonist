class Task:
    task_name = None
    task_dependencies = []
    task_commands = []
    task_count = 0

    def __init__(self, task_name: str, task_dependencies: [], task_commands: [], task_count: int,line_number:int):
        self.task_name = task_name
        self.task_dependencies = task_dependencies
        self.task_commands = task_commands
        self.task_count = task_count
        self.line_number = line_number

    def execute(self):
        for command in self.task_commands:
            command.execute()

    def __str__(self) -> str:
        commands = ""
        for command in self.task_commands:
            commands += f"\n\t{command}"
        return f"\ntask name : {self.task_name} , task count: {self.task_count} , line number:{self.line_number} \n\tdependencies : {self.task_dependencies} \n\tcommands : {commands}\n"
    def __repr__(self):
        return self.task_name
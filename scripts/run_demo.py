
from core.task import Task


if __name__ == "__main__":
    task = Task({
        'name': 'task1',
        'parser': 'parse.P1.P1',
        'input_line': 'inputline.local.LocalInputLine',
        'output_line': 'outputline.local.LocalOutputLine',
        'in_paths': ['input/task1'],
        'out_path': 'out/task1',
    })
    task.run()
    
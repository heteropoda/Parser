
from inputline import InputLine
from tool.misc import get_all_files


class LocalInputLine(InputLine):
    
    def input(self, task):
        if isinstance(task['in_paths'], str):
            task['in_paths'] = [task['in_paths']]
        for paths in task['in_paths']:
            for path in get_all_files(paths):
                with open(path,'r',encoding='utf-8') as f:
                    yield f.read(), path
                    
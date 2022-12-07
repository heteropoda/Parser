
import json
import os
from outputline import OutputLine
from tool.misc import check_dir_create


class LocalOutputLine(OutputLine):
    
    def open_process(self, task):
        file_path = check_dir_create(task['out_path']) + '/' + 'out.json'
        self.out_file = open(file_path, 'a', encoding='utf-8')
        
    def close_process(self, task):
        if self.out_file:
            self.out_file.close()
    
    def output(self, item, path, task):
        if not isinstance(item, str):
            item = json.dumps(item, ensure_ascii=False)
        self.out_file.write(item)
        self.out_file.write('\n')

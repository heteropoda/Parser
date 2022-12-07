

from tool.misc import load_object


class Task(dict):
    
    def __init__(self) -> None:
        pass
    
    def __init__(self, dic: dict) -> None:
        self.update(dic)
        
    def process(self):
        parser = load_object(self.get('parser'))
        input_line = load_object(self.get('input_line'))
        output_line = load_object(self.get('output_line'))
        
        parser.open_process(self)
        input_line.open_process(self)
        output_line.open_process(self)
        
        for text, path in input_line.input(self):
            for item in parser.parse(text, path, self):
                if not item:
                    continue
                output_line.output(item, path, self)
                
        parser.close_process(self)
        input_line.close_process(self)
        output_line.close_process(self)
        
    def run(self):
        self.process()
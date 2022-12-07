from importlib import import_module
import os


def load_object(path):

    if not isinstance(path, str):
        return None

    try:
        dot = path.rindex('.')
    except ValueError:
        raise ValueError(f"Error loading object '{path}': not a full path")

    module, name = path[:dot], path[dot + 1:]
    mod = import_module(module)

    try:
        obj = getattr(mod, name)
    except AttributeError:
        raise NameError(f"Module '{module}' doesn't define any object named '{name}'")

    return obj()


def get_all_files(path, igonre=True):
    out_list = []
    for f in os.listdir(path):
        if igonre:
            if f.startswith('.'):
                continue
            if f.startswith('__'):
                continue
            
        file_path = path + "/" + f
        if os.path.isdir(file_path):
            out_list.extend(get_all_files(file_path))
        elif os.path.isfile(file_path):
            out_list.append(file_path)

    return out_list


def check_dir_create(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    return path
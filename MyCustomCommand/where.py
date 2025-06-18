import os
import sys

def main(*args, **kwargs):
    name_list = args[0]
    # print(args)
    if len(name_list) != 1:
        print("|> [Err 002] Parameter quantity not aligned")
        print("|> [Usage] where <name>")
        return
    
    program_name = name_list[0]
    path_dirs = os.environ.get('PATH', '').split(os.pathsep)
    possible_names = []

    if os.name == 'nt':
        base, ext = os.path.splitext(program_name)
        if not ext:
            pathext = os.environ.get('PATHEXT', '')
            extensions = [e.upper() for e in pathext.split(os.pathsep) if e]
            extensions = [''] + extensions
            possible_names = [base + ext for ext in extensions]
            possible_names = [name.lower() for name in possible_names]
        else:
            possible_names = [program_name.lower()]
    else:
        possible_names = [program_name]

    found = set()

    for dir_path in path_dirs:
        if not os.path.isdir(dir_path):
            continue
        try:
            with os.scandir(dir_path) as entries:
                for entry in entries:
                    if not entry.is_file():
                        continue
                    entry_name = entry.name
                    if os.name == 'nt':
                        entry_name = entry_name.lower()
                    if entry_name in possible_names:
                        found.add(entry.path)
        except (PermissionError, FileNotFoundError):
            pass

    for path in sorted(found):
        print(path)

if __name__ == '__main__':
    main()

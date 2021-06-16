# This is a sample Python script.

# Press Alt+Shift+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from importlib.machinery import SourceFileLoader


def load_build_file(makefile_path: str):
    makefile = SourceFileLoader("makefile", makefile_path).load_module()

    print(f'TEST1 at {makefile_path}', makefile.TEST1 if "TEST1" in dir(makefile) else None)
    print(f'TEST2 at {makefile_path}', makefile.TEST2 if "TEST2" in dir(makefile) else None)
    print(f'TEST3 at {makefile_path}', makefile.TEST3 if "TEST3" in dir(makefile) else None)


print('dir1 ->')
load_build_file('dir1/makefile.py')
print('')

print('THIS ONE SHOULD BE EMPTY, TEST1 and TEST2 are not defined in dir1/dir2/makefile.py')
print('dir1/dir2 ->')
load_build_file('dir1/dir2/makefile.py')

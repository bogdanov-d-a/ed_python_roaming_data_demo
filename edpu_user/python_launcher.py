from edpu import host_alias
import os

_python_3_paths = {
    'PC': 'C:\\Users\\Username\\AppData\\Local\\Programs\\Python\\Python38\\',
    'Laptop': 'C:\\Users\\Username\\AppData\\Local\\Programs\\Python\\Python38\\',
}

def _get_python_3_path():
    return _python_3_paths.get(host_alias.get())

def _start_command(command, work_dir):
    os.system('start /D "{0}" {1}'.format(work_dir, command))

def _start_with_python3(file_name, work_dir, python_name):
    _start_command('{0} {1}'.format(python_name, file_name), work_dir)

def get_python3():
    return _get_python_3_path() + 'python.exe'

def get_python3w():
    return _get_python_3_path() + 'pythonw.exe'

def start_with_python3(file_name, work_dir):
    _start_with_python3(file_name, work_dir, get_python3())

def start_with_python3w(file_name, work_dir):
    _start_with_python3(file_name, work_dir, get_python3w())

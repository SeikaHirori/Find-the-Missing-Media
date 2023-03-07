import os
from pathlib import Path

def run_experiments():
    def print_spacers():
        print("------")

    experiment_finding_absolute_path() 
    print_spacers()

    experiment_finding_relative_path()
    print_spacers()

    experiment_pathlib()

    

def experiment_finding_absolute_path():
    print("Finding absolute path:")
    output:str = os.path.abspath("checkAllPhotos")
    print(output)

def experiment_finding_relative_path():
    print("Finding relative path:")

    dirname = os.path.dirname("")

def experiment_pathlib():
    print("hello pathlib :3")
    cwd = Path.cwd()

    output = cwd
    print(output)
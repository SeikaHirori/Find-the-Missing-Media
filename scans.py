import os
from pathlib import Path

def find_media() -> list[str]:
    _pathway_for_media: str = "_docs/"
    directory_media:Path = Path(_pathway_for_media)

    for index, file in enumerate(directory_media.glob("**/*")):
        print(f"current index: {index}")
        f_name: str = file.name
        f_stem: str = file.stem

        print(f"Printing file's name: {f_name}")
        print(f"Printing file's stem: {f_stem}")
        print()

def run_experiments():
    def print_spacers():
        print("------")

    find_media()

    # experiment_finding_absolute_path() 
    # print_spacers()

    # experiment_finding_relative_path()
    # print_spacers()

    # experiment_pathlib()

def experiment_finding_absolute_path():
    print("Finding absolute path:")
    output:str = os.path.abspath("checkAllPhotos")
    print(output)

def experiment_finding_relative_path():
    print("Finding relative path:")

    dirname = os.path.dirname("")

def experiment_pathlib():
    print("hello pathlib :3")
    cwd:Path = Path.cwd()
    print(cwd)

    output = Path(r'_docs/').glob("**/*")
    print(output)
    print()

    for file in output:
        print(file)
        print(file.__format__)

        convert_to_string:str = str(file.stem)
        print(f"print conversion: {convert_to_string}")
        print()




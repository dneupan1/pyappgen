import os
import subprocess
from collections import namedtuple

ValidationMessage = namedtuple('ValidationMessage', 'is_valid, message')


def is_name_valid(name: str, allowed_chars: [], is_long_name: bool):
    # exclude the list of allowed chars from the name, except for the beginning and end
    modified_name = name[1:-1]
    for allowed_char in allowed_chars:
        modified_name = modified_name.replace(allowed_char, "")
    # append back the beginning and end character on the name
    name = name[0] + modified_name + name[-1]
    if not is_long_name:
        if not name.islower():
            return ValidationMessage(False, "Name should only contain lowercase letters.")
        if not name.isalnum():
            return ValidationMessage(False, "Name should only contain alphanumeric lowercase characters.")
        if not name[0].isalnum():
            return ValidationMessage(False, "Name should begin with alphanumeric character.")
        if not name[0].islower():
            return ValidationMessage(False, "Name should begin with lowercase alphanumeric character.")
        if not name[-1].isalnum():
            return ValidationMessage(False, "Name should end with alphanumeric character.")
    else:
        if not name.isalnum():
            return ValidationMessage(False, "Name should only contain alphanumeric lowercase characters.")
        if not name[0].isalnum():
            return ValidationMessage(False, "Name should begin with alphanumeric character.")
        if not name[-1].isalnum():
            return ValidationMessage(False, "Name should end with alphanumeric character.")
    return ValidationMessage(True, "")


def generate_project(project_name: str,
                     project_long_name: str,
                     project_description: str,
                     exe_name: str,
                     output_folder: str):
    print("Creating python-project structure..")
    print(f"Project Name: {project_name}")
    print(f"Project Long Name: {project_long_name}")
    print(f"Project Description: {project_description}")
    print(f"Exe name: {exe_name}")
    print(f"Output folder: {output_folder}")

    continue_project = input('\nDo you want to continue creating the project? Y or N')

    if continue_project.lower() == "y":
        print(f"Creating project")
        os.chdir(output_folder)
        os.mkdir(project_name)
        os.chdir(project_name)
        with open("main.py", "w+") as main_file:
            main_file.write(f"from .version import __version__\n")
            main_file.write(f"def main():\n")
            main_file.write(f"\tpass\n")

        with open("version.py", "w+") as version_file:
            version_file.write(f"__version__ = \'Version 0\'\n")

        with open("__init__.py", "w+") as init_file:
            init_file.write(f"from .version import __version__\n")

        with open("__main__.py", "w+") as main_file:
            main_file.write(f"from .main import main\n")
            main_file.write(f"main():\n")

        os.chdir(output_folder)
        test_root = f"{output_folder}\\test"
        os.chdir(output_folder)
        os.mkdir("test")
        os.chdir(test_root)

        with open("__init__.py", "w+") as init_file:
            init_file.write("\n\n")

        os.chdir(output_folder)
        with open("build.bat", "w+") as build_script:
            build_script.write(f"call conda activate {project_name}\n")
            build_script.write(f"call pyinstaller --clean --onefile --noconsole pyinstaller_main.py -n {exe_name}\n")

        with open("make_env.bat", "w+") as make_script:
            make_script.write(f"call conda env create --force\n")

        with open("test.bat", "w+") as make_script:
            make_script.write(f"call conda activate {project_name}\n")
            make_script.write(f"pytest test")

        with open("environment.yml", "w+") as env:
            env.write(f"name: {project_name}\n")

        with open("pyinstaller_main.py", "w+") as main:
            main.write(f"from {project_name}.main import main\n")
            main.write(f"main()\n")

        with open("release_notes.txt", "w+") as notes:
            notes.write(f"{project_long_name} Release Notes\n")
            notes.write(f"Version 1\n")
            notes.write(f"\t- Initial release")

        with open("README.md", "w+") as readme:
            readme.write(f"#{project_long_name}\n")
            readme.write(f"{project_description}")







def _clear_screen():
    subprocess.call('cls', shell=True)


def main():
    project_name = input('\nPlease enter project short name\n')
    validity = is_name_valid(project_name, ["_"], False)
    while not validity.is_valid:
        _clear_screen()
        project_name = input(
            f"{validity.message}.\nPlease re-enter project short name: ")
        validity = is_name_valid(project_name, ["_"], False)

    project_long_name = input('\nPlease enter project long name\n')
    validity = is_name_valid(project_long_name, ["_"], True)
    while not validity.is_valid:
        _clear_screen()
        project_long_name = input(
            f"{validity.message}.\nPlease re-enter project long name: ")
        validity = is_name_valid(project_name, ["_"], True)

    exe_name = input('\nPlease enter executable name\n')
    validity = is_name_valid(exe_name, ["_"], False)
    while not validity.is_valid:
        _clear_screen()
        exe_name = input(
            f"{validity.message}.\nPlease re-enter executable name: ")
        validity = is_name_valid(exe_name, ["_"], False)

    project_description = input('\nPlease enter project description\n')

    output_folder = input('\nPlease enter the output folder: ')
    while not os.path.isdir(output_folder):
        _clear_screen()
        output_folder = input('\nPlease reenter the output folder: ')

    generate_project(project_name, project_long_name,
                     project_description, exe_name, output_folder)
    _clear_screen()

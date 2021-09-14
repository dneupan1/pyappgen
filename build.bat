call conda activate pyappgen

call pyinstaller --clean --onefile pyinstaller_main.py -n pyappgen --add-data=./data/*;.

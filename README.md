# Pip-Wrapper
A simple quality of life pip wrapper. This wrapper handles a couple of things for you:

1. Running install commands will auto-create a virtual env in the current directory.
   - If `virtualenv` is not installed, the script will install it globally.
2. After instalation/uninstalation, the script will freeze dependencies to `requirements.txt`.

## Set up
Setting up an alias on your system is probably the easiest way of running this project. I have bound an alias to `mpip` (arbitrary).

On unix style systems:
```bash
alias mpip="python /path/to/script/main.py $@"
```

On windows:
```cmd
DOSKEY mpip="python /path/to/script/main.py $_"
```

## Usage
Replace your existing `pip` commands with your alias (`mpip` in my case).
For example:
```bash
mpip install fire
mpip uninstall numpy
```



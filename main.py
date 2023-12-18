import os
import sys


def is_virtualenv_installed() -> bool:
  try:
    import _virtualenv
    return True
  except ImportError:
    print('`virtualenv` is not installed')
    return False


def ensure_virtualenv_installed() -> None:
  if is_virtualenv_installed():
    return

  print('Installing `virtualenv`')
  os.system('pip install virtualenv')


def get_interpreter_path() -> str | None:
  cwd = os.getcwd()
  interpreter_path_unix = os.path.join(cwd, 'env/bin/python')
  interpreter_path_win = os.path.join(cwd, 'env/Scripts/python')

  if os.path.exists(interpreter_path_unix):
    return interpreter_path_unix

  if os.path.exists(interpreter_path_win):
    return interpreter_path_win

  return None


def get_venv_path() -> str:
  cwd = os.getcwd()
  return os.path.join(cwd, 'env/')


def freeze_requirements(interpreter_path: str) -> str:
  os.system(f'{interpreter_path} -m pip freeze > requirements.txt')


def create_virtual_env(venv_path: str) -> None:
  if not os.path.exists(venv_path):
    print('No `venv` found... creating')
    os.system('python3 -m virtualenv env')


def main(*args: list[str]) -> None:
  ensure_virtualenv_installed()

  venv_path = get_venv_path()
  create_virtual_env(venv_path)

  interpreter_path = get_interpreter_path()

  os.system(f'{interpreter_path} -m pip {" ".join(args)}')

  freeze_requirements(interpreter_path)

if __name__ == '__main__':
  main(*sys.argv[1::])

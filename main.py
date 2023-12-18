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


def is_argument_passed(arguments: list[str], command: list[str]) -> bool:
  full_command = ' '.join(command)
  for arg in arguments:
    if arg in full_command:
      return True
  return False


def strip_custom_commands(command: list[str]) -> list[str]:
  allowed = []
  for arg in command:
    if arg in ['help', '-n', '--no-req', '-h', '--help']:
      continue
    allowed.append(arg)
  return allowed


def show_help() -> None:
  print('Pip wrapper')
  print('Usage:')
  print('If you have created an alias for the tool (referenced as `mpip` here),')
  print('simply replace `pip` with `mpip` for your commands')
  print('\tmpip install <package>')
  print('\tmpip install -r requirements.txt')
  print('')
  print('Options:')
  print('\t-n, --no-req         Do not generate/change requirements.txt')
  print('\thelp, -h, --help     Show this help message')


def main(*args: list[str]) -> None:
  pip_only_args = strip_custom_commands(args)

  if len(args) == 0:
    print('No arguments passed')
    show_help()
    quit(1)

  if is_argument_passed(['-h', '--help', 'help'], args):
    show_help()
    quit(0)

  ensure_virtualenv_installed()

  venv_path = get_venv_path()
  create_virtual_env(venv_path)

  interpreter_path = get_interpreter_path()
  if interpreter_path is None:
    print('Something went wrong, cannot find the virtualenv')
    quit(1)

  os.system(f'{interpreter_path} -m pip {" ".join(pip_only_args)}')

  if not is_argument_passed(['-n', '--no-req'], args):
    freeze_requirements(interpreter_path)

  quit(0)

if __name__ == '__main__':
  main(*sys.argv[1::])

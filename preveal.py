
import subprocess, platform, webbrowser, os

def reveal(dir: str):
    return reveal_file(dir)

def reveal_file(dir: str):
    # todo: add support for open with specific appc
    try:
        if platform.system() == 'Darwin':
            _subprocess_open('open', dir)
            return
        elif platform.system() == 'Windows':
            # todo: implement regex for C:, D:, and more, basically [A-Z]\:
            disk = str() if dir.strip().startswith('C:') else 'C:'
            _subprocess_open('explorer', f'{disk}{dir}')
            return
        elif platform.system() == 'Linux':
            _subprocess_open('xdg-open', f'{dir}')
            return
    except:
        'N/A'
    if not webbrowser.open(f'file:///{os.path.join(os.getcwd(), dir)}'):
        return Exception()
    
def _subprocess_open(command: str, path: str):
    subprocess.check_call([command, '--', f'{(path)}'])

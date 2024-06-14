import os
import pip

SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
# uninstall pykt-toolkit
pip.main(['uninstall', 'pykt-toolkit', '-y'])

# install pykt-toolkit
os.chdir(SCRIPT_PATH)
pip.main(['install', '.'])
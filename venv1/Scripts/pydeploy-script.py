#!C:\Users\���뿵\PycharmProjects\simpletranslator\venv1\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pydeploy==0.2.6','console_scripts','pydeploy'
__requires__ = 'pydeploy==0.2.6'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pydeploy==0.2.6', 'console_scripts', 'pydeploy')()
    )

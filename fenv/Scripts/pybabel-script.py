#!"c:\users\joshua chima\google drive\hackathon\fibase\fibase\fenv\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'Babel==1.3','console_scripts','pybabel'
__requires__ = 'Babel==1.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Babel==1.3', 'console_scripts', 'pybabel')()
    )

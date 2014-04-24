from __future__ import with_statement
from io import open
def revision():
    try:
        with open(u'/proc/cpuinfo',u'r') as f:
            for line in f:
                if line.startswith(u'Revision'):
                    return 1 if line.rstrip()[-1] in [u'2',u'3'] else 2
            else:
                return 0
    except:
        return 0


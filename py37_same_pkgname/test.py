import sys, os

sys.path += [os.path.abspath('./path1'),
             os.path.abspath('./path2')]


from namespace1.package1 import module1
from namespace1.package1 import module2
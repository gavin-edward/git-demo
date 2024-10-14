import os
import sys

print(os.getcwd())

print(os.path.abspath("__file__"))

### sys
print(sys.path)
print(sys.path.append("/home/xxx/project/vip"))

import os
import sys
import numpy as np
import torch
import torchvision

print(os.getcwd())

print(os.path.abspath("__file__"))

### sys
print(sys.path)
print(sys.path.append("/home/xxx/project/vip"))
print (torch.__version__)
print (torch.cuda.is_available())

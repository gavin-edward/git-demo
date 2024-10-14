import os
import sys
import numpy as np

import torch
import torchvision
import torch.nn as nn
import torch.nn.function as F

print(os.getcwd())

print(os.path.abspath("__file__"))

### sys
print(sys.path)
print(sys.path.append("/home/xxx/project/vip"))
print (torch.__version__)
print (torch.cuda.is_available())

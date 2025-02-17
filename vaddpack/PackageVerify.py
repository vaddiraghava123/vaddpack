import os
import sys

package_name ='vaddpack'
try:
    __import__(package_name)
    print("Already installed")
except ImportError:
    print('Package not installed .. ', package_name)
    os.system(f"{sys.executable} -m pip install {package_name}")
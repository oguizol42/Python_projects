import sys
import os
import site

path: str = sys.executable
if sys.prefix == sys.base_prefix:
    print("MATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {path}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python3 -m virtualenv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")

else:
    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python: {path}")
    print(f"Virtual Environment: {os.path.basename(sys.prefix)}\n")

    print(f"Environment Path: {sys.prefix}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")

    print("Package installation path:\n")

    print(site.getsitepackages())

import glob
import os
import sys
print(glob.glob('*'))
print(sys.version)

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

if __name__ == "__main__":
    if "-c" in opts: # categories
        print("Adding new test categories directories if necessary")
        typedir = 'categories'
    elif "-t" in opts: # tags
        print("Adding new tags directories if necessary")
        typedir = 'tags'
    else:
        raise SystemExit(f"Usage: {sys.argv[0]} (-c | -t ) <arguments>...")

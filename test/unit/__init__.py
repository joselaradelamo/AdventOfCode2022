import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir1 = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir1)
sys.path.append(parentdir)
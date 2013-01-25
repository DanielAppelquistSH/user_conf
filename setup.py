from os import makedirs
from os import symlink
from os.path import dirname
from os.path import expanduser
from os.path import lexists
from os.path import relpath

def setupFileSymlink(src_file,dst_file):
  if not lexists(dirname(dst_file)):
    makedirs(dirname(dst_file))

  if not lexists(dst_file):
    symlink(src_file,dst_file)


def main():

  HOME_DIR= expanduser("~") + "/testdummy/"

  configs = [("i3-config",".i3/config")]

  for (src_file, dst_file) in configs:
    setupFileSymlink(relpath(src_file), (HOME_DIR + dst_file))


if __name__ == '__main__':
  main()

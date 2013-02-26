from os import makedirs
from os import symlink
from os.path import dirname
from os.path import expanduser
from os.path import lexists
from os.path import realpath

def setupFileSymlink(src_file,dst_file):
    if not lexists(dirname(dst_file)):
        makedirs(dirname(dst_file))

    if not lexists(dst_file):
        symlink(src_file,dst_file)


def main():

    HOME_DIR= expanduser("~/")
# HOME_DIR+="testdummy"
    configs = [ ("i3-config"    ,".i3/config"),
                ("i3status.conf",".i3/i3status.conf"),
                ("vimrc"        ,".vimrc"),
                ("zshrc"        ,".zshrc"),
                ("Xmodmap"      ,".Xmodmap"),
                ("aliases"      ,".aliases")]

    for (src_file, dst_file) in configs:
        setupFileSymlink(realpath(src_file), (HOME_DIR + dst_file))


if __name__ == '__main__':
  main()

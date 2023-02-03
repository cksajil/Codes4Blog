import sys
import subprocess


def run():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if len(sys.argv) == 2:
            subprocess.Popen([command], shell=True)
        elif len(sys.argv) == 3:
            param = sys.argv[2]
            subprocess.run([command+' '+param], shell=True)
    else:
        print('Invalid usage')


if __name__ == '__main__':
    run()

from GuiBuilder.STARTUP import GuiBuilder
import os
from installer import install
# TODO: Tighten the nuts and bolts. Updates should be backwards compatible


def main():
    cwd = os.getcwd()
    f = open(os.path.join(cwd, 'version.txt'), 'r')
    version = float(f.readline().split('=')[1])
    f.close()
    if version == 0:
        install()
        f = open(os.path.join(cwd, 'version.txt'), 'w')
        # TODO: Reach out to server and request updates based on version (Currently Low Priority)
        f.write('version={}'.format('1.0'))
        f.close()
    application = GuiBuilder(cwd)
    application.run()


if __name__ == '__main__':
    main()

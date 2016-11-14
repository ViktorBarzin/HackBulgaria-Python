import sys
import os


def create_content(file_path):
    with open(file_path, 'w') as w:
        w.write('\n\ndef main():\n' + '    pass\n\n' + 'if __name__ == \'__main__\':\n' + '    main()\n')


def main():
#    if len(sys.argv) < 2 or len(sys.argv) > 3:
#        print('Usage: python create-py <file name>')
 #       return
    create_content(sys.argv[1])
    if '-n' in sys.argv:
        file_name = sys.argv[sys.argv.index('-n') + 1]
    else:
        name = 'default.py'
    #file_name = [x for x in sys.argv if x != sys.argv[0] and x != '-o'][0]
    if '-o' in sys.argv:
        os.system('bash /usr/share/pycharm-community-2016.2.3/bin/pycharm.sh ' + file_name)
        pass
if __name__ == '__main__':
    main()

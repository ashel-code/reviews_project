# from smth import sm
<<<<<<< Updated upstream:manual_parser.py
=======

>>>>>>> Stashed changes:manual_parsing/main.py

instructions = '''- press [x] to stop
- press [f] to mark as fake
- press [c] to mark as correct
- press [h] for help'''

import sys
import termios
import tty

def get_key():
    # сохраняем текущее состояние терминала
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        # устанавливаем новые настройки терминала для чтения одной клавиши
        tty.setraw(sys.stdin.fileno())
        # читаем нажатую клавишу
        ch = sys.stdin.read(1)
    finally:
        # восстанавливаем старые настройки терминала
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():


    comment = 'hmm...'
    print(instructions)
    while True:
        # comment = sm.getRandomComment()
        try:
            print(comment)

            key = get_key()
            if key == 'x':
                print('Stopping...')
                break
            elif key == 'f':
                print('FAKE...')
            elif key == 'c':
                print('CORRECT')
            elif key == 'h':
                print(instructions)
        except:
            print("All comments have been reviewed")
    print()




if __name__ == "__main__":
    # main(sys.argv)
    main()

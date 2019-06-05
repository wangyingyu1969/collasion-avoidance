import sys, tty, termios

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
while True:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    print (' %c' %  ch )
    if ch=='a':
        break

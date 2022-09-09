#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    arg_len = len(argv) - 1
    if arg_len == 0:
        print('{:d} arguments.'.format(arg_len))
    elif arg_len == 1:
        print('{:d} argument:'.format(arg_len))
        print('{:d}: {:s}'.format(arg_len, argv[arg_len]))
    else:
        print('{:d} arguments:'.format(arg_len))
        count = 1
        while count <= arg_len:
            print('{:d}: {:s}'.format(count, argv[count]))
            count += 1

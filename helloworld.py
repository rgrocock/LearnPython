__author__ = 'russellgrocock'
#!/usr/bin/python2.7
# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
    """
    main code block
    Command line args are in sys.argv[1], sys.argv[2] ...
    sys.argv[0] is the script name itself and can be ignored
    """

    print 'Hello there', sys.argv[1]
    name = sys.argv[1]
    print repeat(name, True)

def repeat(name,exclaim):
    """Returns the string name repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = name * 3

    if exclaim:
        result = result + '!!!'
    return result

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
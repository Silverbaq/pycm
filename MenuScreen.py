__author__ = 'Silverbaq'


class MenyScreen:

    import os

    def __init__(self, description, options):
        self.description = description
        self.options = options

    def banner(self, text, ch='=', length=78):
        spaced_text = ' %s ' % text
        banner = '%s\n%s\n%s' % (ch*length,spaced_text.center(length, ch),ch*length)
        return banner

    def line(self, text, ch='=', length=78):
        spaced_text = ' %s ' % text
        line = '\n%s\n' % spaced_text.center(length, ch)
        return line

    # Checks the OS, and sends the clear command
    def clearScreen(self):
        if self.os.name == "nt":
            self.os.system('cls')
        else:
            self.os.system('clear')

    def displayIt(self):
        # Clears the screen
        self.clearScreen()

        # Make banner for screen
        banner = self.banner("somehting")
        print banner

        # Centers the description
        print self.description.center(78,' ')

        # Makes a line for the options
        print self.line("Options")

        # Posts all the options
        count = 1
        for o in self.options:
            print '#{0:2}: ==> {1:10}'.format(str(count),o)
            count = count + 1
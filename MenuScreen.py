#!/usr/bin/python
__author__ = 'Silverbaq'

class MenuScreen:

    import os

    ch = '='
    length = 78

    def __init__(self, bannerTitle, description, options):
        self.bannerTitle = bannerTitle
        self.description = description
        self.options = options

    def banner(self, text):
        spaced_text = ' %s ' % text

        # Makes the Banner String
        banner = '%s\n%s\n%s' % (self.ch * self.length,spaced_text.center(self.length, self.ch), self.ch * self.length)

        return banner

    def line(self, text, ch='*'):
        spaced_text = ' %s ' % text
        line = '\n%s\n' % spaced_text.center(self.length, ch)
        return line

    # Checks the OS, and sends the clear command
    def clearScreen(self):
        if self.os.name == "nt":
            self.os.system('cls')
        else:
            self.os.system('clear')

    # Makes it able to chance the char and the length
    def setConfiguration(self, char='=', length=78):
        self.ch = char
        self.length = length

    def displayIt(self):
        # Clears the screen
        self.clearScreen()

        # Make banner for screen
        banner = self.banner(self.bannerTitle)
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
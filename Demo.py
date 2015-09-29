__author__ = 'Silverbaq'
#!/usr/bin/python

import MenuScreen

options = ['option1', 'option2', 'tmp']
description = 'This is the demo'
title = 'PyCM is so cool!'

ms = MenuScreen.MenuScreen(title, description, options)
ms.setConfiguration('=')

ms.displayIt()

# pycm

Python Console Menu
-------------------

This is a simple console menu, made for Python 2.7

    import MenuScreen
    
    options = ['opetin1', 'option2', 'tmp']
    description = 'This is the demo'
    
    ms = MenuScreen.MenyScreen(description, options)
    
    ms.displayIt()

Output

    ==============================================================================
    ================================= somehting ==================================
    ==============================================================================
                                   This is the demo                               
    
    ================================== Options ===================================
    
    #1 : ==> opetin1   
    #2 : ==> option2   
    #3 : ==> tmp       

# pycm

Python Console Menu
-------------------

This is a simple console menu, made for Python 2.7

    import MenuScreen

	options = ['option1', 'option2', 'tmp']
	description = 'This is the demo'
	title = 'PyCM is so cool!'

	ms = MenuScreen.MenuScreen(title, description, options)
	ms.setConfiguration('=')

	ms.displayIt()

Output

    ==============================================================================
	============================== PyCM is so cool! ==============================
	==============================================================================
								This is the demo                               
	
	********************************** Options ***********************************

	#1 : ==> option1   
	#2 : ==> option2   
	#3 : ==> tmp  

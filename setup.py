from cx_Freeze import setup, Executable 
  
setup(name = "UNO" , 
      version = "0.1" , 
      description = "" , 
      executables = [Executable("uno.py")]) 
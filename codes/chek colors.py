import os 
 try: 
     from colorama import Fore, Back 
  
 except ModuleNotFoundError: 
     os.system("pip instll colorama") 
  
  
 from colors import w , ran , y , c  
 GB = Back.GREEN 
 YB = Back.YELLOW 
 WB = Back.RED 
  
 logo = f""" 
  ▄█     ▄███████▄                                             
 ███    ███    ███                                             
 ███▌   ███    ███                                             
 ███▌   ███    ███                                             
 ███▌ ▀█████████▀                                              
 ███    ███                                                    
 ███    ███                                                    
 █▀    ▄████▀                                                  
                                                               
    ▄████████  ▄██████▄   ▄█    █▄     ▄████████    ▄████████  
   ███    ███ ███    ███ ███    ███   ███    ███   ███    ███  
   ███    ███ ███    ███ ███    ███   ███    █▀    ███    ███  
  ▄███▄▄▄▄██▀ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀  </> Instagram : @the_developer.01  
 ▀▀███▀▀▀▀▀   ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀    
 ▀███████████ ███    ███ ███    ███   ███    █▄  ▀███████████  </> Github: thedeveloper03
   ███    ███ ███    ███ ███    ███   ███    ███   ███    ███  
   ███    ███  ▀██████▀   ▀██████▀    ██████████   ███    ███  
   ███    ███                                      ███    ███  
    
                                     </>Author: the developer 
   """ 
  
 from random import choice 
  
  
 for i in logo: 
     col = choice([Fore.RED , Fore.GREEN , Fore.CYAN , Fore.LIGHTWHITE_EX , Fore.MAGENTA , Fore.BLUE]) 
  
     print(col + i , end="")
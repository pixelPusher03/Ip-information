import os 
 import platform 
 from setup import colors 
 from setup.colors import r,g,y,c , w 
 from colorama import Fore , Back 
  
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
  ▄███▄▄▄▄██▀ ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀   
 ▀▀███▀▀▀▀▀   ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀     
 ▀███████████ ███    ███ ███    ███   ███    █▄  ▀███████████  
   ███    ███ ███    ███ ███    ███   ███    ███   ███    ███  
   ███    ███  ▀██████▀   ▀██████▀    ██████████   ███    ███  
   ███    ███                                      ███    ███  
             {y}<{w}/{y}> {c}Author: {w} thedeveloper {r}|{g} the developer ofc 
  
 {w}<{y}/{w}> {GB}{w}Instagram : @the_developer.01{Back.RESET} 
 l
 {w}<{y}/{w}> {WB}{w}Github: thedeveloperofc the {Back.RESET}                                                                                                      
 """ 
 c = colors 
 try: 
     from colorama import Fore, Style 
 except ModuleNotFoundError: 
     os.system("pip install colorama") 
  
 def banner(): 
     print(c.ran + logo) 
  
  
  
 def banner2(): 
  
  
     print(c.ran,"\n" + "|"+ Style.BRIGHT + Fore.LIGHTCYAN_EX, "- " * 4, " [+] Follow me on Instagram @mr_juice7 ", "- " * 4 + c.ran + "|") 
     print(c.ran, "\n" + "|"+ Style.BRIGHT + Fore.LIGHTYELLOW_EX, "- " * 4, " [+] Follow me on Instagram @cyber_dioxide_ ", "- " * 4+c.ran + "|") 
     print(c.ran , "\n"+ "|"+ Style.BRIGHT + Fore.LIGHTRED_EX, "- " * 4, "[+] Github: https://github.com/Cyber-Dioxide/ ", "- " * 3+c.ran + "|") 
     print(c.ran + "\n"+ "|" + "*" * 60+c.ran + "|") 
  
 def clear(): 
     s = platform.platform() 
     if "Windows" in s: 
         os.system("cls") 
     else: 
         os.system("cls") if "Windows" in platform.platform() else os.system("clear")
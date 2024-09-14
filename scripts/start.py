
import os 
from rich.console import Console
from art import tprint

class Settings:
    general = { 
        "cls_after_use": True ,
	    "off_command" : "pass" ,  
    }
    venv = {
    } 
    st = { 
    "processStart" : "bold blue",
    "processComplite" : "bold italic green",
    "processError" : "italic red",
    "textAction" : "italic purple",
    "textQuestion" : 'bold orange3'
    }
    file_path = { 
        "pip_lib" : "scripts/requirements.txt"
    }
    def __init__(self) -> None:
        pass

   

    

console = Console()
commadList = ('установить библиотеки' , 'обновить библиотеки' , 'выгрузить библиотеки')
setting = Settings()
    

def run_venv(is_run = False , is_stop = False): 

    if not(os.path.exists('.venv')): 
        console.print('Виртуальная среда не найдена' , style=setting.st["processError"])
        
        console.print('создание виртуального окружения',style=setting.st["processStart"])
        os.system('py -m venv .venv')
        console.print('окружение создано', style=setting.st["processComplite"])
     
    if is_run : 
        os.system('cmd /k run.bat') 
        
    if is_stop: 
        os.system('cmd /k stop.bat') 
        
 

def action_selection() -> bool: 
    
    [console.print(f'[{item}]',style = setting.st["textAction"] , end = " ") for item in commadList]

    action  = input()
    if action == setting.general["off_command"]:
        return True
    match action : 
        case 'установить библиотеки':
            console.print(f'путь до файла (по умолчанию {setting.file_path["pip_lib"]}): ' , style=setting.st["textAction"] , end = " ")
            name = input()
            if name == "": 
                name = setting.file_path["pip_lib"]
        
            os.system(f'pip install -r {name}')
        case 'обновить библиотеки':
            pass
        case 'выгрузить библиотеки':
            pass
        case 'запуск venv':
            run_venv(is_run=True)
        case 'выключить venv':
            run_venv(is_stop=True)
    return False 

if __name__ == "__main__": 
    
    tprint('by   sneip4ik' , font = "small")
   
    console.print("Загрузка настроек" , style=setting.st["processStart"])
    # загруска настроек 
    console.print("Настройки загружены" , style=setting.st["processComplite"])
    
    run_venv()
    

    while(not(action_selection())): 
       pass 
    if setting.general["cls_after_use"]: 
        os.system("cmd /k cls")
           
                
            

    
    
    
    
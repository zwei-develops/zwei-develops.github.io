################
##   Signal   ##
################

def main():
    #################
    ##   Imports   ##
    #################

    import os

    def cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    cls()

    print('Importing Modules. This may take some time.')

    #######  Required Modules

    import subprocess
    import sys
    import os
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'prompt_toolkit'])
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'wget'])
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'termcolor'])
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'progress'])

    cls()

    ####### Loading Bar

    import termcolor
    from termcolor import colored

    print(colored('INITIALIZING:', 'yellow'), colored('SPARKPLUG: PY', 'magenta'))

    from time import sleep
    from progress.bar import Bar

    with Bar('Loading', fill='█', suffix='%(percent).1f%% - %(eta)ds') as bar:
            for i in range(100):
                sleep(0.01)
                bar.next()

    ####### Other Modules

    import prompt_toolkit
    from prompt_toolkit import prompt
    import webbrowser
    import wget
    import getpass
    import zipfile

    cls()

    ###################
    ##   Functions   ##
    ###################

    def website():
        with Bar('Loading', fill='█', suffix='%(percent).1f%% - %(eta)ds') as bar:
            for i in range(100):
                sleep(0.001)
                bar.next()
        
        webbrowser.open('https://sparkplug.pro')

    ####### SMB

    def smb():
        url = 'https://github.com/zwei-develops/zwei-develops.github.io/releases/download/SMB/SuperMarioBros.zip'
        path = '/Users/' + getpass.getuser() + '/Downloads/SuperMarioBros.zip'
        path2 = '/Users/' + getpass.getuser() + '/Downloads/'
        wget.download(url, path)
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(path2)
        os.remove(path)
        print(" ")
        print(colored("Done! Check your", 'yellow'), colored('DOWNLOADS', 'red'), colored('folder.', 'yellow'))

    def info():
        cls()
        print(colored('                                                          SPARKPLUG', 'magenta'))
        print(colored('                                                  Sparkplug', 'magenta'),  colored('|', 'grey'), colored('by zwei#0001', 'green'))
        print(colored('                                                  Py', 'blue'), colored('Script', 'yellow'),  colored('|', 'grey'), colored('by M4X4#6494', 'green'))
        print(colored('We at Sparklug do not own any games that are shown in this script. All rights of said games go to the developers, not us.', 'red'))
        with Bar('                                             ', fill='█', suffix=' ') as bar:
            for i in range(1000):
                sleep(0.1)
                bar.next()
        cls()
        Openingprompt()
    ################
    ##   Prompt   ##
    ################
    def Openingprompt():
        print(colored('Welcome to Sparkplug Python, A python script for students to','yellow'), colored('"pass the border"', 'red'), colored('that allows you to play online games that are usually restricted.', 'yellow'))
        print(colored("---------------------------", 'cyan'))
        print(colored('Sparkplug', 'magenta'),  colored('|', 'grey'), colored('by zwei#0001', 'green'))
        print(colored('Py', 'blue'), colored('Script', 'yellow'),  colored('|', 'grey'), colored('by M4X4#6494', 'green'))
        print(colored("---------------------------", 'cyan'))
        print(colored("Don't know where to get started?", 'blue'))
        print(colored("Choose something from the list below. These are all games that the creator has picked for new players.", 'blue'))
        print(colored("----------------------------------------------------------------------------------------------------", 'cyan'))
        print(colored("     1", 'cyan'), ("    >>     Open Website                        "))
        print(colored("     2", 'cyan'), ("    >>     Download | Super Mario Bros.        "))
        print(colored("     3", 'cyan'), ("    >>     Coming Soon                         "))
        print(colored("     4", 'cyan'), ("    >>     Coming Soon                         "))
        print(colored("     5", 'cyan'), ("    >>     Coming Soon                         "))
        print(colored("     6", 'cyan'), ("    >>     Coming Soon                         "))
        print(colored("     7", "cyan"), ("    >>     Credits / Info                      "))
        print(colored("----------------------------------------------------------------------------------------------------", 'cyan'))

    #############
    ##  Main   ##
    #############

    Openingprompt()

    while True:
        text = prompt('Option # >> ')

        ########################
        ##   Call Functions   ##
        ########################

        if text == "1":
            website()
        elif text == "2":
            smb()
        elif text == "3":
            print('Coming Soon')
        elif text == "4":
            print('Coming Soon')
        elif text == "5":
            print('Coming Soon')
        elif text == "6":
            print('Coming Soon')
        elif text == "7":
            info()
        elif text == "cls":
            cls()
            Openingprompt()
        else:
            print(colored('Unknown Option:', 'red'), colored(text, 'cyan'))

######################
##   Script Check   ##
######################

if __name__ == '__main__':
    main()

else:
    print(f"Please do not import this script and just run it instead.")
    print(f"Script Imported: spp.py")
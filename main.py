import subprocess, threading
from tkinter import *

root = Tk()

#global derivacao
derivacao = {}

class Application():
    stop_threads = False
    
    def __init__(self):
        self.root = root
        self.tela()
        self.frame()
        self.inputs()
        self.buttons()
        root.mainloop()

    def tela(self):
        self.root.title('Ping')
        self.root.geometry('714x600')
        self.root.resizable(False,False)

    # cria os frames para adcionar os componentes
    def frame(self):
        self.frame = Frame(self.root)
        self.frame.place(relx = 0 , rely = 0,relwidth = 1, relheight = 1)

    def buttons(self):
        #Bottao Start 
        self.buttonStart = Button(self.frame, text = 'iniciar' , command  = self.start)
        self.buttonStart.place ( relx = 0.37, rely = 0.03, width = 130, height = 50)
        
        #Bottao Stop 
        self.buttonStop = Button(self.frame, text = 'Parar' , command  = self.stop)
        self.buttonStop.place ( relx = 0.57, rely = 0.03, width = 130, height = 50)

    def inputs(self):
        #input do server
        self.labelInputDoBanco = Label(self.frame, text = 'Informe o host do banco do cliente:')
        self.labelInputDoBanco.place(relx = 0.02, rely = 0.02)

        self.inputHostBanco = Entry(self.frame, width = 45)
        self.inputHostBanco.place(relx = 0.02, rely = 0.06)

        #ipconfig
        self.labelIpconfig = Label(self.frame, text = 'ipconfig:')
        self.labelIpconfig.place(relx = 0.02, rely = 0.14)

        self.textBoxIpconfig = Text(self.frame,height=8, width =85)
        self.textBoxIpconfig.place(relx = 0.02, rely = 0.19)

        #tracert
        self.labelTracert = Label(self.frame, text = 'ping:')
        self.labelTracert.place(relx = 0.02, rely = 0.48)

        self.textBoxTracert = Text(self.frame,height=13, width =85)
        self.textBoxTracert.place(relx = 0.02, rely = 0.55)


    def start(self):
        
        stop_threads = False
        
        self.startThreading = threading.Thread(target=self.informacoes)
        self.startThreading.start()
    
    def stop(self):
        self.stop_threads = True


    def informacoes(self):

        server = self.inputHostBanco.get()
        print(server)

        ipconfig = subprocess.getoutput('ipconfig').replace('   ','')
        self.textBoxIpconfig.insert(END,ipconfig[1496:2032])    
        

        while True:

            if self.stop_threads: 
                break

            output = subprocess.getoutput("ping " + server)
            for line in output.split("\n")[2:6]:
                self.textBoxTracert.insert(END,'{}\n'.format(line))
                
        
        
        


Application()
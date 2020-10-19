from tkinter import *

class Window(Frame):
    def __init__(self, Master=None):
        Frame.__init__(self)
        self.master = Master
        self.initWindow()
        

    def initWindow(self):

        self.master.title('GUI')
        self.pack(fill=BOTH, expand = 1)
        
        self.playersUnPhoto = PhotoImage(file = 'C:\\Users\\schle\\projects\\project1\\playerIconUnselected.png')
        self.playersPhoto = PhotoImage(file = 'C:\\Users\\schle\\projects\\project1\\playerIconSelected.png')
        self.selected = 3
        self.playersButton = Button(image = self.playersUnPhoto, command = self.displayPlayers, height = 85, width = 95, highlightthickness = 0, bd = 0)
        self.playersButton.image = (self.playersUnPhoto)
        
        self.teamsPhoto = PhotoImage(file = 'C:\\Users\\schle\\projects\\project1\\teamsIconSelected.png')
        self.teamsUnPhoto = PhotoImage(file = 'C:\\Users\\schle\\projects\\project1\\teamsIconUnSelected.png')
        self.teamsButton = Button(image = self.teamsUnPhoto, command = self.displayTeams, height = 85, width = 95, highlightthickness = 0, bd = 0)
        self.teamsButton.image = (self.teamsUnPhoto)

        self.settingsUnPhoto = PhotoImage(file = 'C:\\Users\\schle\\projects\\project1\\settingsIconUnSelected.png')
        self.settingsPhoto = PhotoImage(file = 'C:\\Users\\schle\\projects\\project1\\settingsIconSelected.png')
        self.settingsButton = Button(image = self.settingsUnPhoto, command = self.displaySettings, height = 85, width = 95,  highlightthickness = 0, bd = 0)
        self.settingsButton.image = (self.settingsUnPhoto)
        
        quitImage = PhotoImage(file = 'C:\\Users\\schle\\projects\\project1\\exitIcon.png')
        quitButton = Button(image = quitImage, command= self.exitSelf, height = 85, width = 95, highlightthickness = 0, bd = 0)  
        quitButton.image = quitImage
        
        self.playersButton.place(x=0,y=0)
        self.teamsButton.place(x=0,y=85)
        self.settingsButton.place(x=0,y=170)
        quitButton.place(x=0,y=255)
    

    def adjustMenu(self):
        if self.selected == 0:
            self.playersButton.configure(image = self.playersPhoto)    
            self.playersButton.image = self.playersPhoto

            #Unselect the other buttons
            self.teamsButton.configure(image = self.teamsUnPhoto)    
            self.teamsButton.image = self.teamsUnPhoto
            self.settingsButton.configure(image = self.settingsUnPhoto)    
            self.settingsButton.image = self.settingsUnPhoto

        elif self.selected == 1:
            self.teamsButton.configure(image = self.teamsPhoto)    
            self.teamsButton.image = self.teamsPhoto

            #Unselect the other buttons
            self.playersButton.configure(image = self.playersUnPhoto)    
            self.playersButton.image = self.playersUnPhoto
            self.settingsButton.configure(image = self.settingsUnPhoto)    
            self.settingsButton.image = self.settingsUnPhoto

        elif self.selected == 2:

            self.settingsButton.configure(image = self.settingsPhoto)    
            self.settingsButton.image = self.settingsPhoto

            #Unselect the other buttons
            self.playersButton.configure(image = self.playersUnPhoto)    
            self.playersButton.image = self.playersUnPhoto
            self.teamsButton.configure(image = self.teamsUnPhoto)    
            self.teamsButton.image = self.teamsUnPhoto


    def exitSelf(self):
        quit()


    def displaySettings(self):
        if self.selected != 2:
            self.selected = 2
            #Adjust menu section
            self.adjustMenu()
            #Display Players Section


    def displayPlayers(self):
        
        if self.selected != 0:
            
            self.selected = 0
            #Adjust menu section
            self.adjustMenu()
            #Display Players Section


    def displayTeams(self):
        if self.selected != 1:
            
            self.selected = 1
            #Adjust menu section

            self.adjustMenu()

            #Display Players Section
        
root = Tk()    
app = Window(root)
root.geometry('600x340')
root.resizable(False, False)
root.mainloop()

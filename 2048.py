# Tkinter library this in python2, we will we implementing the code using python2, just becasue python3 library Tkinter does work will with max system.
from tkinter import Frame, Label, CENTER 
# We are importing some classes like Frame, Label, CENTER:some justifying content.

# These all present in the Tkinter which allow us create a UI.


# Import LogicsFinal files we have already created in the logic part.
import LogicsFinal

# import constants as c means we imported the constant file as well and what ever functionality we will using through (C.)[c dot].
import constants as c



# Here we have created class Game2048 which is inherited from Frame class. So the super class is Frame, And Frame allow us to create a Box kind of things. In which we places all our wedigts like, Button, checkBox,Text Box, every things we can add in a Frame which can present in the Tkinter library. So we will be using class Frame.And our class Game2048 will inherite the function and propreties form the Frame.Which we will using to implement our code.
class Game2048(Frame):
    
    # constructor here 
    def __init__(self):
        
        # So Frame class need an object on which it will be creating a Frame. Self denotes the object of 2048 Game.
        Frame.__init__(self)
        
        # If We have return self.grid(), that it's denote is Tkinter has grid Manger, which allow us to create all wedigts in the form grid. So Our Frame look like a grid Now. And grid means row & col. 
        self.grid()
        
        # self.master.title('2048') means every things in a Frame class has a master things. And its title is 2048  and come at the top.
        self.master.title('2048')
        
        
        
        
        # self.master.bind("<key>", self.key_down) means what ever Frame self.master we will be bind it through key. That means what is happen in the Frame(means), If any key is pressed we will go to self.key_down. So binding is their to see the UI event If any event is happing (if the key event is happing) So we need to go to self.key_down function.
        self.master.bind("<Key>", self.key_down)
        
        
        # self.commands denotes is it create a map,for constant.KEY_UP (KEY_UP means 'w')  so for 'w' we need to implement the LogicsFinal.move_up function. And Similarly all...
        self.commands = {c.KEY_UP: LogicsFinal.move_up, c.KEY_DOWN: LogicsFinal.move_down, c.KEY_LEFT: LogicsFinal.move_left, c.KEY_RIGHT: LogicsFinal.move_right }
        
        
        
        
        # self.grid_cells their is grid_cells means In our grid their will be some cells. currently it is empty it is empty.
        self.grid_cells = []
        
        
        # self.init_grid() means add the grid cells by calling self.init_grid() function
        self.init_grid()
        
        
        # self.init_matrix() will do is we can init_matrix() function... create a matrix of 4*4 and add new 2 in the matrix. 
        self.init_matrix()
        
        
        
        # self.update_grid_cells() means initially all the grid cells having  0 is present, but 2 has comes its background need to be changed and text color of 2 need to be changed. similarly another 2 will we come its background need to be changed and text color of 2 need to be changed. That happen in the self.update_grid_cells(). self.update_grid_cells() changed on the UI. That means set the color according to UI. Set the color according to Number.
        self.update_grid_cells()
        
        
        
        # self.mainloop() does is it actually runs the programs.
        self.mainloop()
        
        
        
    def init_grid(self):
        # SO we have created another Frame, So Frame is what: Frame is actually a wedigts in UI like Button,CheckBOx,TextBox etc.
        # Inside the Frame we have create another Frame,NOw we have create Frame of 400*400 size insie the outside Frame 
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME, width=c.SIZE, height=c.SIZE)
        
        # So We have set background as wedigts
        background.grid()
        
        # Inside our grid we need to add cells.
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                
                # Now we are creating a cell
                # Now another Frame inside the background frame 
                # cell is it selfa Frame
                cell = Frame(background, bg=c.BACKGROUND_COLOR_CELL_EMPTY, width=c.SIZE / c.GRID_LEN, height=c.SIZE /c.GRID_LEN)
                
                
                # adding the cell inside the background with padding
                cell.grid(row=i, column=j, padx=c.GRID_PADDING, pady=c.GRID_PADDING)
                
                # Inside the cell we are adding the Label
                # Label is another wedgits which used to denote the Text box.
                # Scince cell was a grid ,so Label was itself a grid
                # justify = CENTER means we will adding text into CENTER.
                t = Label(master=cell, text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY, justify=CENTER, font=c.FONT, width=5, height=2)
                
                
                # And have visualized the label as grid.
                # Label cover the cell completly.
                t.grid()
                
                # grid_row.append(t) we have append Label.
                grid_row.append(t)
            
            # [l1,l2,l3,l4],[l5,l6,l7,l8],[l9,l10,l11,l12],[l13,l14,l15,l16]
            self.grid_cells.append(grid_row)
            
            
    
    
    # It is just create a matrix.
    # Internally we have mentain a  matrix.
    # What is changed in internally matrix that will we refelected in the UI.
    def init_matrix(self):
        self.matrix = LogicsFinal.start_game()
        # Now we are added two new in the internally matrix.
        LogicsFinal.add_new_2(self.matrix)
        LogicsFinal.add_new_2(self.matrix)
        
    
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg= c.BACKGROUND_COLOR_DICT[new_number], fg=c.CELL_COLOR_DICT[new_number])
        
        # When we are changing the color,Can take some time So this function it will wait untill all the color gets changed.  
        self.update_idletasks()
     
    # What happen when press any key:
    # It takes 2 things self, or event has been come What event in happen.what ever key like w,s,a,d will come.
    def key_down(self, event):
        
        # event.char that will gives that key.
        # repr does what it gives the printable part of that things.
        key = repr(event.char)
        # a,s,d,w key press that means we will do something otherwise we will not do any thing.
        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            # if something has changed then we will do something.
            if changed:
                
                # If something changed then add new 2 in the matrix.
                LogicsFinal.add_new_2(self.matrix)
                # If new 2 is added then we call self.update_grid_cells()
                self.update_grid_cells()
                # bydefault changed is False
                changed = False
                
                if LogicsFinal.get_current_state(self.matrix) == "WON":
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    
                    self.grid_cells[1][2].configure(text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                
                if LogicsFinal.get_current_state(self.matrix) == "LOST":
                    self.grid_cells[1][1].configure(text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    
                    self.grid_cells[1][2].configure(text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    
                    
                    
gamegrid = Game2048()
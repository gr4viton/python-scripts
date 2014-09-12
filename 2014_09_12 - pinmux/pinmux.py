#import _tkinterinter as tkinter
#from _tkinterinter import *

try:
    import tkinter
    from tkinter import *
except ImportError:
    raise ImportError ("The tkinter Module is required to run this program.")

from apihelper import info

#import _tkinternter as tkinter
import time
import string # for alphabet

class ExampleApp(tkinter.Frame):
    ''' An example application for TkInter.  Instantiate
        and call the run method to run. '''
    rec_i = 0
    recs = ['world', 'suckers', 'pals', 'mutants', 'meatbags', 'zombies']
    def __init__(self, master):
        # Initialize window using the parent's constructor
        tkinter.Frame.__init__(self,
                          master,
                          width=300,
                          height=200)
        # Set the title
        self.master.title('TkInter Example')
 
        # This allows the size specification to take effect
        self.pack_propagate(0)
 
        # We'll use the flexible pack layout manager
        self.pack()
 
        # The greeting selector
        # Use a StringVar to access the selector's value
        self.greeting_var = tkinter.StringVar()
        self.greeting = tkinter.OptionMenu(self,
                                      self.greeting_var,
                                      'hello',
                                      'goodbye',
                                      'heyo')
        self.greeting_var.set('hello')
 
        # The recipient text entry control and its StringVar
        self.rec_var = tkinter.StringVar()
        self.rec = tkinter.Entry(self,
                                  textvariable=self.rec_var)
        self.rec_var.set('world')
 
        # The go button
        self.go_button = tkinter.Button(self,
                                   text='Go',
                                   command=self.print_out)
 
        
        # label JX_[1:Y]
        self.lbJX = tkinter.Label(self, text='JX_[1:Y]=')
        #Label(self, text='JX_[1:Y]=')
        # txt JX
        self.curX = 1
        self.eJX_val = tkinter.StringVar()
        self.eJX = tkinter.Entry(self, width=4, textvariable=self.eJX_val)
        self.eJX_val.set(str(self.curX))
        # txt JY
        self.maxY = 20
        self.eJY_val = tkinter.StringVar()
        self.eJY = tkinter.Entry(self, width=4, textvariable=self.eJY_val)
        self.eJY_val.set(str(self.maxY))

        #btn JX1
 
        #btn genJXY
        self.btnGenJXY = tkinter.Button(self,
                                   text='Gen JX_[1:Y]',
                                   command=self.genJXY)
        #lbJXY
        self.lbJXY_val = tkinter.StringVar()
        self.lbJXY = tkinter.Label(self, 
                textvariable=self.lbJXY_val, 
                justify=RIGHT, anchor=N,
                font=("Console", 8)
                )
        self.lbJXY_val.set('')
        
        #txJXY
        self.txJXY = tkinter.Text(self)
        self.txJXY.config(font=("Console", 8), width=10)
        self.txJXY.delete(1.0, END)
        self.txJXY.insert(INSERT, "\n" * (self.maxY-1) )

        self.btnPopulatePTs = tkinter.Button(self, 
                                            text='Populate ports', 
                                            command=self.INSERT_jumpersInPorts)

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #txPTs 
        numOfPorts = 5
        portLetters = list(string.ascii_uppercase)[:numOfPorts]
        self.txPTs = [tkinter.Text(self) for i in range(numOfPorts)]

        [item.config(font=("Console", 8),width=10) for item in self.txPTs]

        #txPT
        self.txPT = {key:value for key, value in zip( portLetters, self.txPTs ) }

        #lbPTs
        self.lbPTs = [tkinter.Label(self) for i in range(numOfPorts)]
        [item.config(text=labelText) for item, labelText in zip(self.lbPTs, portLetters)]

        #lbPins
        self.lbPins = [tkinter.Label(self) for i in range(numOfPorts)]
        maxPinNumber = 32
        labelText = "\n".join(str(s) for s in range(maxPinNumber))
        [item.config(text=labelText,font=("Console", 8),width=2) for item in self.lbPins]


        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Put the controls on the form
        self.lbJX.grid(row=0,column=0,sticky=W)
        self.eJX.grid(row=0,column=1,sticky=W)
        self.eJY.grid(row=0,column=2,sticky=W)
        self.btnGenJXY.grid(row=0,column=3,sticky=W)
        
        self.lbJXY.grid(row=2,column=0,columnspan=1,rowspan=1,sticky=N+W+E)
        self.txJXY.grid(row=2,column=1,columnspan=3,rowspan=1,sticky=N+W+E,pady=1)
        
        col_s = 4 #start column #
        # why multiply by 3 ?? IDN! BUT IT WORKS
        self.btnPopulatePTs.grid(row=0, column=col_s+1, columnspan=numOfPorts*3,sticky=N+W+E+S) 

        [lb.grid(row=1,column=n_col*2,columnspan=2) 
                                        for lb,n_col in zip(self.lbPTs, range(col_s,col_s+numOfPorts))]
        [lb.grid(row=2,column=n_col*2) 
                                        for lb,n_col in zip(self.lbPins, range(col_s,col_s+numOfPorts))]
        [tx.grid(row=2,column=n_col*2+1, sticky=N+W+E+S, pady=1) 
                                        for tx,n_col in zip(self.txPTs, range(col_s,col_s+numOfPorts))]
        #print("\n".join(str(i) for i in self.lbPTs))
        #print(self.lbPTs)

        #self.lbJX.pack(fill=tkinter.X, side=tkinter.LEFT)
        #self.eJX.pack(side=tkinter.LEFT)
        #self.eJY.pack(side=tkinter.LEFT)
        #self.btnGenJXY.pack(side=tkinter.LEFT)
#        self.txJXY.pack(side=tkinter.LEFT)
#        self.txJXY.pack(fill=tkinter.X, side=tkinter.TOP)

#        self.txJXY.pack()
#        self.go_button.pack(fill=tkinter.X, side=tkinter.BOTTOM)

        #self.greeting.pack(fill=tkinter.X, side=tkinter.TOP)
        #self.rec.pack(fill=tkinter.X, side=tkinter.TOP)
        #self.go_button.pack(fill=tkinter.X, side=tkinter.LEFT)

    def genJXY(self):
        ''' Generates JX_[1:Y] list inside txJXY'''
        JX = int(self.eJX_val.get())
        maxY = int(self.eJY_val.get())
        strJumperPins = ["J%i_%i" % (X,Y) for X,Y in zip( (JX,) * (1+maxY) , range(1, maxY+1 ) )]

        self.lbJXY_val.set( "\n".join( strJumperPins ) )

#        self.txJXY.config(height=self.lbJXY.winfo_height()/15)
        self.txJXY.config(height=maxY)

        if maxY != self.maxY: 
            #that means that the height of text has changed
            self.txJXY.delete(1.0, END)
            self.txJXY.insert(INSERT, "\n" * (maxY-1) )

        #if JX != self.curJX: 
        self.curJX = JX
        self.maxY = maxY
#        print( "%s=%s" % (k,v) for k,v in zip(range(5),range(5)) )
        #print(dir(self.txJXY))
        #self.txJXY.insert(INSERT,"\n".join("J%i_" % X 
        #        for X in range(1, 1+int(self.eJY_val.get()))                
        #        ))
#        print([a for a in range(1, 1+int(self.eJY_val.get()))])
        #print("\n".join("J%i_" % X 
        #        for X in range(1, 1+int(self.eJY_val.get()))                
        #        ))
    def INSERT_jumpersInPorts(self):
        ''' inserts Jumper connections list inside txPts'''
        #for line in self.txJXY.get()

        #JX = int(self.eJX_val.get())
        #maxY = 1+int(self.eJY_val.get())
        #self.txJXY.insert(INSERT, 
        #        "\n".join( 
        #            ("J%i_%i" % (X,Y)
        #                for X,Y in zip( (JX,) * maxY , range(1, maxY ) )
        #            )
        #        ))
        #[        
        #    (txPTX.delete(1.0, END),
        #    txPTX.insert(INSERT, "\n" * (-1+len(str_jumpers)) )
        #    ) for txPTX in self.txPT
        #]
    def print_out(self):
        ''' Print a greeting constructed
            from the selections made by
            the user. and changes the next value of recipient string from list of recipients
            '''
        
        print('%s, %s!' % (self.greeting_var.get().title(),
                           self.rec_var.get()))
        
        self.rec_i += 1
        if self.rec_i >= len(self.recs): self.rec_i = 0
        self.rec_var.set(self.recs[self.rec_i])
        
    def run(self):
        ''' Run the app '''
#        self.
        #print(dir(tkinter))
        #info(tkinter)
        #print(tkinter.TOP)
        #print(tkinter.BOTTOM)
        self.genJXY()
        self.mainloop()


app = ExampleApp(tkinter.Tk())
app.run()



#time.sleep(2)

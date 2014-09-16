#import _tkinterinter as tkinter
#from _tkinterinter import *

try:
    import tkinter
    from tkinter import *
except ImportError:
    raise ImportError ("The tkinter Module is required to run this program.")

from apihelper import info
from gr4module import *

#import _tkinternter as tkinter
import time
import string # for alphabet
import re # for text-number splitting


frame = tkinter.Frame
class ExampleApp(frame):
    ''' An example application for TkInter.  Instantiate
        and call the run method to run. '''
    rec_i = 0
    recs = ['world', 'suckers', 'pals', 'mutants', 'meatbags', 'zombies']
    
    def __init__(q, master):
        
        q.SCh = "/" # SplitCharacter
        q.txPTsCounter = 0 # txPTs focus iterator

        # Initialize window using the parent's constructor
        frame = tkinter.Frame.__init__(q,
                          master,
                          width=300,
                          height=200)

        # Set the title
        q.master.title('TkInter Example')
 
        # This allows the size specification to take effect
        q.pack_propagate(0)
 
        # We'll use the flexible pack layout manager
        q.pack()

        # The greeting selector
        # Use a StringVar to access the selector's value
        q.greeting_var = tkinter.StringVar()
        q.greeting = tkinter.OptionMenu(q,
                                      q.greeting_var,
                                      'hello',
                                      'goodbye',
                                      'heyo')
        q.greeting_var.set('hello')
 
        # The recipient text entry control and its StringVar
        q.rec_var = tkinter.StringVar()
        q.rec = tkinter.Entry(q,
                                  textvariable=q.rec_var)
        q.rec_var.set('world')
 
        # The go button
        q.go_button = tkinter.Button(q,
                                   text='Go',
                                   command=q.print_out)
 
        
        # label JX_[1:Y]
        q.lbJX = tkinter.Label(q, text='JX_[1:Y]=')
        #Label(q, text='JX_[1:Y]=')
        # txt JX
        q.curX = 1
        q.eJX_val = tkinter.StringVar()
        q.eJX = tkinter.Entry(q, width=4, textvariable=q.eJX_val)
        q.eJX_val.set(str(q.curX))
        # txt JY
        q.maxY = 20
        q.eJY_val = tkinter.StringVar()
        q.eJY = tkinter.Entry(q, width=4, textvariable=q.eJY_val)
        q.eJY_val.set(str(q.maxY))

        #btn JX1
 
        #btn genJXY
        q.btnGenJXY = tkinter.Button(q,
                                   text='Gen JX_[1:Y]',
                                   command=q.genJXY,
                                   underline=0)


        #____________________________________________________
        #lbJXY
        q.lbJXY_val = tkinter.StringVar()
        q.lbJXY = tkinter.Label(q, 
                textvariable=q.lbJXY_val, 
                justify=RIGHT, anchor=N,
                font=("Console", 8)
                )
        q.lbJXY_val.set('')
        
        #txJXY
        q.txJXY = tkinter.Text(q)
        q.txJXY.config(font=("Console", 8), width=10)
        q.txJXY.delete(1.0, END)
        q.txJXY.insert(INSERT, "\n" * (q.maxY-1) )
        q.txJXY.bind('<Return>', q.KEY_Return(q.txJXY))

        q.btnPopulatePTs = tkinter.Button(q, 
                                            text='Populate ports', 
                                            command=q.INSERT_jumpersInPorts,
                                            underline=11)

        # ____________________________________________________
        # bindings
        q.BIND_keyFcn(master, q.genJXY, '!^', 'qr')
        q.BIND_keyFcn(master, q.INSERT_jumpersInPorts, '!^', 'gpe')
   #     q.BIND_keyFcn(master, q.focus_set(q.eJX), '!', 'z')
        q.BIND_keyFcn(master, q.eJX.focus_set(), '!', 'z')
#        q.BIND_keyFcn(master, q.eJY.focus_set, '!', 'x')

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #txPTs 
        numOfPorts = 5
        portLetters = list(string.ascii_uppercase)[:numOfPorts]

        q.numOfPorts = numOfPorts
        q.portLetters = portLetters
        q.txPTs = [tkinter.Text(q) for i in range(numOfPorts)]
        
        txPTs_width = 32
        [item.config(font=("Console", 8),width=txPTs_width,wrap=NONE) for item in q.txPTs]
        [item.bind('<Return>', q.KEY_Return(item)) for item in q.txPTs]

        #txPT
        q.txPT = {key:value for key, value in zip( portLetters, q.txPTs ) }


        #lbPTs
        q.lbPTs = [tkinter.Label(q) for i in range(numOfPorts)]
        [item.config(text=labelText) for item, labelText in zip(q.lbPTs, portLetters)]

        #lbPins
        q.lbPins = [tkinter.Label(q) for i in range(numOfPorts)]
        maxPinNumber = 32
        q.maxPinNumber = maxPinNumber 
        labelText = "\n".join(str(s) for s in range(maxPinNumber))
        [item.config(text=labelText,font=("Console", 8),width=2) for item in q.lbPins]


        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Put the controls on the form
        q.lbJX.grid(row=0,column=0,sticky=W)
        q.eJX.grid(row=0,column=1,sticky=W)
        q.eJY.grid(row=0,column=2,sticky=W)
        q.btnGenJXY.grid(row=0,column=3,sticky=W)
        
        q.lbJXY.grid(row=2,column=0,columnspan=1,rowspan=1,sticky=N+W+E)
        q.txJXY.grid(row=2,column=1,columnspan=3,rowspan=1,sticky=N+W+E,pady=1)
        
        col_s = 4 #start column #
        # why multiply by 3 ?? IDN! BUT IT WORKS
        q.btnPopulatePTs.grid(row=0, column=col_s+1, columnspan=numOfPorts*3,sticky=N+W+E+S) 

        [lb.grid(row=1,column=n_col*2,columnspan=2) 
                                        for lb,n_col in zip(q.lbPTs, range(col_s,col_s+numOfPorts))]
        [lb.grid(row=2,column=n_col*2) 
                                        for lb,n_col in zip(q.lbPins, range(col_s,col_s+numOfPorts))]
        [tx.grid(row=2,column=n_col*2+1, sticky=N+W+E+S, pady=1 ) 
                                        for tx,n_col in zip(q.txPTs, range(col_s,col_s+numOfPorts))]
        #print("\n".join(str(i) for i in q.lbPTs))
        #print(q.lbPTs)

        #q.lbJX.pack(fill=tkinter.X, side=tkinter.LEFT)
        #q.eJX.pack(side=tkinter.LEFT)
        #q.eJY.pack(side=tkinter.LEFT)
        #q.btnGenJXY.pack(side=tkinter.LEFT)
#        q.txJXY.pack(side=tkinter.LEFT)
#        q.txJXY.pack(fill=tkinter.X, side=tkinter.TOP)

#        q.txJXY.pack()
#        q.go_button.pack(fill=tkinter.X, side=tkinter.BOTTOM)

        #q.greeting.pack(fill=tkinter.X, side=tkinter.TOP)
        #q.rec.pack(fill=tkinter.X, side=tkinter.TOP)
        #q.go_button.pack(fill=tkinter.X, side=tkinter.LEFT)
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # creation of list for storing data

        #class pinX: pass
        #pinX.value
        numOfPins = 32
        str_void = '#void#'
        q.str_void = str_void 
        q.numOfPins = numOfPins
#        pta = { pin:val for pin,val in zip(range(numOfPins), ['#void#']*numOfPins) }
        #dictP = [{ pin:val for pin,val in zip(range(q.numOfPins), ['#void#']*q.numOfPins) }] * q.numOfPorts
        dictP = [ [str_void]*q.numOfPins for i in range(q.numOfPorts) ]
        q.PTs = { char:list for char,list in zip(q.portLetters, dictP) }
#        print(q.PTs)

        #q.PT = { port:pins for port,pins in zip( [portLetters]*pinNumbers, range(pinNumbers )}
    def BIND_keyFcn(q, bindObj, fcn, modifs, keys, *whatever):
#        !alt #super ^ctrl +shift
        key_dict = {"!":'Alt', "#":'Super', "^":'Control', "+":'Shift'}
        str_keys = []
        key_names = list("qr")
        str_keys += [ "<%s-%s>" % (key_dict[modif],key_name) for modif in list(modifs) for key_name in list(keys)]
        [bindObj.bind(str_key, fcn) for str_key in str_keys]

    def genJXY(q, *whatever):
        ''' Generates JX_[1:Y] list inside txJXY'''
        JX = int(q.eJX_val.get())
        maxY = int(q.eJY_val.get())

        q.JX = JX
        strJumperPins = ["J%i_%i" % (X,Y) for X,Y in zip( (JX,) * (1+maxY) , range(1, maxY+1 ) )]


        q.lbJXY_val.set( "\n".join( strJumperPins ) )

#        q.txJXY.config(height=q.lbJXY.winfo_height()/15)
        q.txJXY.config(height=maxY)

        if maxY != q.maxY: 
            #that means that the height of text has changed
            q.txJXY.delete(1.0, END)
            q.txJXY.insert(INSERT, "\n" * (maxY-1) )

        #if JX != q.curJX: 
        q.curJX = JX
        q.maxY = maxY
#        print( "%s=%s" % (k,v) for k,v in zip(range(5),range(5)) )
        #print(dir(q.txJXY))
        #q.txJXY.insert(INSERT,"\n".join("J%i_" % X 
        #        for X in range(1, 1+int(q.eJY_val.get()))                
        #        ))
#        print([a for a in range(1, 1+int(q.eJY_val.get()))])
        #print("\n".join("J%i_" % X 
        #        for X in range(1, 1+int(q.eJY_val.get()))                
        #        ))
    def ADD_jumper(q,port,pin,str_J):
        if q.PTs[port][pin] == q.str_void:
            q.PTs[port][pin] = str_J
            return
        signals = str(q.PTs[port][pin]).split(q.SCh)
        ss = set(signals)
        if str_J not in set(signals):
            print(signals)
            signals.append(str_J)
            q.PTs[port][pin] = q.SCh.join(signals)

    def GET_PTX(q, str_port):
        ''' translates the port name from user text input
         and returns the object in the list prepared for pinsettings insertion'''

        [(port, pin)] =  re.findall(r'(\w+?)(\d+)', str_port.upper())
        success = 1
        return (success, port, int(pin) )
        # dict with all the possibilities?
        # -> not a good idea
    def POPULATE_PTs_from_txJXY(q):
        J_Y = 0

        for line in q.txJXY.get(1.0, END).splitlines():
            J_Y = J_Y+1
            if line:
                str_J = "J%i_%i" % (q.JX, J_Y)
                (success, port, pin) = q.GET_PTX(line) 
                print("PT%s%i=%s" % (port, pin, str_J))
                if success == 1:
                    q.ADD_jumper(port,pin,str_J)
    #            print('path: {}'.format(line))
        
        print(q.PTs)
    def GET_signalNames(q,port,pin):
        if q.PTs[port][pin] != q.str_void:
            return q.PTs[port][pin] 
        else:
            return ""
    def INSERT_jumpersInPorts(q, *whatever):
        ''' inserts Jumper connections list inside txPts'''
        

        q.POPULATE_PTs_from_txJXY()

#        [ portq.PT[port]]
        #q.PTs["A"][4] = "J4"
#        print(q.PTs["A"])
        P__()
#        print(q.PTs)
#        strP = [ "\n xXx" for port in range(numOfPorts)] 

        strP = [ "\n".join( 
                [ q.GET_signalNames(port,pin) for pin in range(q.numOfPins) ]
            ) for port in q.portLetters 
            ] 
        
        #range(q.numOfPorts) ]

#        strP = ["ahoj"] * q.numOfPorts
        #strP[port]
        #print(strP)
        # delete all 
        [tx.delete(1.0, END) for tx in q.txPTs] 
        #insert contains of strPort
        [ tx.insert(INSERT,strP[port]) for tx, port in zip(q.txPTs, range(q.numOfPorts)) ]

        #JX = int(q.eJX_val.get())
        #maxY = 1+int(q.eJY_val.get())
        #q.txJXY.insert(INSERT, 
        #        "\n".join( 
        #            ("J%i_%i" % (X,Y)
        #                for X,Y in zip( (JX,) * maxY , range(1, maxY ) )
        #            )
        #        ))
        #[        
        #    (txPTX.delete(1.0, END),
        #    txPTX.insert(INSERT, "\n" * (-1+len(str_jumpers)) )
        #    ) for txPTX in q.txPT
        #]
        
        q.txPTs[q.txPTsCounter].focus_set()
        q.txPTsCounter += 1
        if q.txPTsCounter >= q.numOfPorts: q.txPTsCounter = 0

    def print_out(q):
        ''' Print a greeting constructed
            from the selections made by
            the user. and changes the next value of recipient string from list of recipients
            '''
        
        print('%s, %s!' % (q.greeting_var.get().title(),
                           q.rec_var.get()))
        
        q.rec_i += 1
        if q.rec_i >= len(q.recs): q.rec_i = 0
        q.rec_var.set(q.recs[q.rec_i])
        
    def run(q):
        ''' Run the app '''
#        q.
        #print(dir(tkinter))
        #info(tkinter)
        #print(tkinter.TOP)
        #print(tkinter.BOTTOM)
        q.genJXY()
        q.mainloop()
    def KEY_Return(q, evt):          
        ''' Makes the Enter not a newline but a down key'''
        
        return 'break' # <--------- this makes normal behaviour disabled
    


def key(event):
    print("pressed", repr(event.char))

root = tkinter.Tk()
app = ExampleApp(root)
#app.bind('<Alt-g>', app.key)
#app.bind('<Alt-g>', key)
app.run()



#time.sleep(2)

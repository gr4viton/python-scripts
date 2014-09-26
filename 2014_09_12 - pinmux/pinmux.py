#import _tkinterinter as tkinter
#from _tkinterinter import *

try:
    import tkinter as tk
    from tkinter import *
except ImportError:
    raise ImportError ("The tkinter Module is required to run this program.")

from apihelper import info
from gr4module import *
from xmlPars import REPLACE_xml_singalNames

import linecache # for config loading

import sys # for save

#import _tkinternter as tkinter
import time
import string # for alphabet
import re # for text-number splitting



config_sufix = "_pinmux.vim"

frame = tk.Frame
class ExampleApp(frame):
    ''' An example application for TkInter.  Instantiate
        and call the run method to run. '''
    rec_i = 0
    recs = ['world', 'suckers', 'pals', 'mutants', 'meatbags', 'zombies']
    
    def __init__(q, master):
        defFont = ("Console", 8)
        defFont_small = ("Console", 6)
        q.SCh = "/" # SplitCharacter
        q.txPTsCounter = 0 # txPTs focus iterator

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # load config

#        pinmux_fname = linecache.getline(q.config_fname, 1)
        a = 'U:\Davidek\LOG\LOGBOOK\\2014_09_11 - pinMux recreation\_2014_09_11 - peby\FRDM-K64F_sdk_notRouted.peb'
        pinmux_fname = a
        q.config_fname = pinmux_fname + config_sufix

        # Initialize window using the parent's constructor
        frame = tk.Frame.__init__(q,
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
        q.greeting_var = tk.StringVar()
        q.greeting = tk.OptionMenu(q,
                                      q.greeting_var,
                                      'hello',
                                      'goodbye',
                                      'heyo')
        q.greeting_var.set('hello')
 
        # The recipient text entry control and its StringVar
        q.rec_var = tk.StringVar()
        q.rec = tk.Entry(q,
                                  textvariable=q.rec_var)
        q.rec_var.set('world')
 
        # The go button
        q.go_button = tk.Button(q,
                                   text='Go',
                                   command=q.print_out)
 
        
        # label JX_[1:Y]
        q.lbJX = tk.Label(q, text='JX_[1:Y]=')
        #Label(q, text='JX_[1:Y]=')
        # txt JX
        q.curX = 1
        q.eJX_val = tk.StringVar()
        q.eJX = tk.Entry(q, width=4, textvariable=q.eJX_val)
        q.eJX_val.set(str(q.curX))
        # txt JY
        q.maxY = 20
        q.eJY_val = tk.StringVar()
        q.eJY = tk.Entry(q, width=4, textvariable=q.eJY_val)
        q.eJY_val.set(str(q.maxY))

        #btn JX1
 
        #btn genJXY
        q.btnGenJXY = tk.Button(q,
                                   text='Gen JX_[1:Y]',
                                   command=q.genJXY,
                                   underline=0)


        #____________________________________________________
        #lbJXY
        q.lbJXY_val = tk.StringVar()
        q.lbJXY = tk.Label(q, 
                textvariable=q.lbJXY_val, 
                justify=RIGHT, anchor=N,
                font=defFont
                )
        q.lbJXY_val.set('')
        
        #txJXY
        q.txJXY = tk.Text(q)
        q.txJXY.config(font=defFont, width=10)
        q.txJXY.delete(1.0, END)
        q.txJXY.insert(INSERT, "\n" * (q.maxY-1) )

        # txInsertMore
        q.txInsertMore = tk.Text(q)
        q.txInsertMore.config(font=defFont, height=10, width = 20 )
 #       q.txJXY.delete(1.0, END)
#        q.txInsertMore.insert(INSERT, "" )

        # btnInsertMore
        q.btnInsertMore = tk.Button(q, 
                                            text='Add more', 
                                            command=q.ADD_more,
                                            underline=6)
        #____________________________________________________
        # btns
        q.btnPopulatePTs = tk.Button(q, 
                                            text='Populate ports', 
                                            command=q.POPULATE_PTs_andActualize,
                                            underline=7)
        q.btnSaveToPinmux = tk.Button(q, 
                                            text='Save to pinmux', 
                                            command=q.SAVE_toPinmux,
                                            underline=0)

        q.btnLoadConfig = tk.Button(q, 
                                            text='Load config', 
                                            command=q.LOAD_config,
                                            underline=0)
        q.btnSaveConfig = tk.Button(q, 
                                            text='Save config', 
                                            command=q.SAVE_config,
                                            underline=0)

        # txFilePinmux
        q.txFilePinmux = tk.Text(q)
        q.txFilePinmux.config(font=defFont_small, height=1, width = 2)
        q.txFilePinmux.insert(INSERT, pinmux_fname )
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #txPTs 
        numOfPorts = 5
        portLetters = list(string.ascii_uppercase)[:numOfPorts]

        q.numOfPorts = numOfPorts
        q.portLetters = portLetters
        q.txPTs = [tk.Text(q) for i in range(numOfPorts)]
        
        txPTs_width = 32
        [item.config(font=defFont,width=txPTs_width,wrap=NONE) for item in q.txPTs]

        #txPT
        q.txPT = {key:value for key, value in zip( portLetters, q.txPTs ) }

        #lbPTs
        q.lbPTs = [tk.Label(q) for i in range(numOfPorts)]
        [item.config(text=labelText) for item, labelText in zip(q.lbPTs, portLetters)]

        #lbPins
        q.lbPins = [tk.Label(q) for i in range(numOfPorts)]
        maxPinNumber = 32
        q.maxPinNumber = maxPinNumber 
        labelText = "\n".join(str(s) for s in range(maxPinNumber))
        [item.config(text=labelText,font=defFont,width=2) for item in q.lbPins]
        
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #btnInsert
        q.btnInsert = tk.Button(q,          text='<= Insert <=', 
                                            command = q.INSERT_sigNameAndActualize,
                                            underline=7)
        #btnAdd
        q.btnAdd = tk.Button(q,             text='<- Add <-', 
                                            command = q.ADD_sigNameAndActualize,
                                            underline=3)
        #btnActualize
        q.btnActualize = tk.Button(q,       text='View actualization', 
                                            command = q.ACTUALIZE_view,
                                            underline=0)
        # txSelPin
        q.txSelPin = tk.Text(q)
        q.txSelPin.config(font=defFont, height=1, width = 4)
        q.txSelPin.insert(INSERT, "a0" )

        # txSigName
        q.txSigName = tk.Text(q)
        q.txSigName.config(font=defFont, height=1, width = 4)
        q.txSigName.insert(INSERT, "" )

        # txWholeValue
        q.txWholeValue = tk.Text(q)
        q.txWholeValue.config(font=defFont, height=1, width = 4 )
        q.txWholeValue.insert(INSERT, "" )

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # Put the controls on the form
        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        #____________________________________________________
        # JX_generator        
        
        q.btnPopulatePTs.grid(row=2, column=0, columnspan=4,sticky=N+W+E+S) 

        q.lbJX.grid(row=3,column=0,sticky=W)
        q.eJX.grid(row=3,column=1,sticky=W)
        q.eJY.grid(row=3,column=2,sticky=W)
        q.btnGenJXY.grid(row=3,column=3,sticky=W)
        
        q.lbJXY.grid(row=4,column=0,columnspan=1,rowspan=1,sticky=N+W+E)
        q.txJXY.grid(row=4,column=1,columnspan=3,rowspan=1,sticky=N+W+E,pady=1)
        
        q.txInsertMore.grid(row=5,column=0,columnspan=4,rowspan=1,sticky=S+N+W+E,pady=1)
        q.btnInsertMore.grid(row=5,column=4,columnspan=1,rowspan=1,sticky=S+N+W+E,pady=1)
        #____________________________________________________
        # pin selector, adder and inserter
        q.txSelPin.grid(row=0,column=1,columnspan=2,rowspan = 2)

        q.btnAdd.grid(row=0,column=3,sticky=W+S+E+N)
        q.btnInsert.grid(row=1,column=3,sticky=W+S+E+N)

        Label(q, text='new SigName:').grid(row=0,column=4,columnspan=1,sticky=W+S+E+N)
        Label(q, text='Pin signals:').grid(row=1,column=4,columnspan=1,sticky=W+S+E+N)
        q.txSigName.grid(row=0,column=5,columnspan=1,sticky=W+S+E+N)
        q.txWholeValue.grid(row=1,column=5,columnspan=1,sticky=W+S+E+N)

        # ____________________________________________________
        # upper strip
        col_s = 4 #start column #
        q.btnActualize.grid(row=1,column=6,columnspan=2,sticky=W+S+E+N)

        q.btnSaveToPinmux.grid(row=0,column=col_s+5, columnspan=1,sticky=N+W+E+S) 
        q.txFilePinmux.grid(row=1,column=col_s+5, columnspan=6,sticky=N+W+E+S) 

        q.btnSaveConfig.grid(row=2,column=col_s+5, columnspan=1,sticky=N+W+E+S) 
        q.btnLoadConfig.grid(row=2,column=col_s+7, columnspan=1,sticky=N+W+E+S) 

        # ____________________________________________________
        # txPTs
        [lb.grid(row=3,column=n_col*2-col_s,columnspan=2) 
                                        for lb,n_col in zip(q.lbPTs, range(col_s,col_s+numOfPorts))]
        [lb.grid(row=4,column=n_col*2-col_s) 
                                        for lb,n_col in zip(q.lbPins, range(col_s,col_s+numOfPorts))]
        [tx.grid(row=4,column=n_col*2+1-col_s, sticky=N+W+E+S, pady=1 ) 
                                        for tx,n_col in zip(q.txPTs, range(col_s,col_s+numOfPorts))]
        #print("\n".join(str(i) for i in q.lbPTs))
        #print(q.lbPTs)

        #q.lbJX.pack(fill=tk.X, side=tk.LEFT)
        #q.eJX.pack(side=tk.LEFT)
        #q.eJY.pack(side=tk.LEFT)
        #q.btnGenJXY.pack(side=tk.LEFT)
#        q.txJXY.pack(side=tk.LEFT)
#        q.txJXY.pack(fill=tk.X, side=tk.TOP)

#        q.txJXY.pack()
#        q.go_button.pack(fill=tk.X, side=tk.BOTTOM)

        #q.greeting.pack(fill=tk.X, side=tk.TOP)
        #q.rec.pack(fill=tk.X, side=tk.TOP)
        #q.go_button.pack(fill=tk.X, side=tk.LEFT)
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # creation of list for storing data
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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

        
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # bindings
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        modifs = '!'
        # button shortcuts
        q.BIND_keyFcn(master, q.genJXY, modifs, 'gq')
        q.BIND_keyFcn(master, q.POPULATE_PTs_andActualize, modifs, 'pe')
        q.BIND_keyFcn(master, q.ADD_sigNameAndActualize, modifs, 'air')
        q.BIND_keyFcn(master, q.ACTUALIZE_view, modifs, 'v')
        q.BIND_keyFcn(master, q.SAVE_toPinmux, modifs, 's')

        # exit
        q.BIND_keyFcn(master, q.EXIT_program, modifs, 'q')
#        master.bind("<Shift-Escape>", q.EXIT_program) 

        # focus shortcuts
        # not working
        q.BIND_keyFcn(master, q.eJX.focus_set(), '!', 'z')
   #     q.BIND_keyFcn(master, q.focus_set(q.eJX), '!', 'z')
#        q.BIND_keyFcn(master, q.eJY.focus_set, '!', 'x')
        
        # ____________________________________________________
        # disable some keys
        items = q.txPTs + [q.txSigName,q.txSelPin,q.txJXY]
        keys = ['<Return>', '<Tab>', '<space>']
        #[item.bind(key, q.KEY_disable(item)) for item in items ]
        [item.bind(key, q.KEY_disable(item)) for item in items for key in keys]


        q.txSigName.bind('<Return>', q.KEY_disable(q.txJXY))
        q.txSelPin.bind('<Return>', q.KEY_disable(q.txJXY))
        q.txJXY.bind('<Return>', q.KEY_disable(q.txJXY))
        
        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # view
        q.ACTUALIZE_view()
    def ADD_more(q):
        lines = q.txInsertMore.get(1.0,END).split("\n")
        [ q.ADD_sigNameFrom( *(line.split("=")) ) for line in lines if line != ""]
        q.ACTUALIZE_view()
#        splited.pop()
        
        #print(splited)
    def UPDATE_fnames(q):
        q.save_fname = q.txFilePinmux.get(1.0,END)
        q.config_fname = q.save_fname[:-1] + config_sufix

    def EXIT_program(q, *whatever):
        q.SAVE_config()
        q.destroy()
        q.exit()
    def LOAD_config(q):
        q.UPDATE_fnames()

        print("\n".join(["puvodni:","%"*80, str(q.PTs), "%"*80]))
        f = open(q.config_fname,'r')
        lins = f.readlines() 
        f.close() 

        pad = 3
        iline = pad
        
        #for iport in range(0, q.numOfPorts):
        #    iline = pad + iport * q.numOfPins
        #    q.PTs[q.portLetters[iport]] = ["volno"] * q.numOfPins
#       #     q.PTs[q.portLetters[iport]] = [q.str_void] * q.numOfPins
        #    q.PTs[q.portLetters[iport]] = [ lins[ipin] for ipin in range(iline, q.numOfPins -1)][:-1]
        #    print( str(iline) )
        #    print( q.portLetters[iport])
        
        
        for iport in range(0, q.numOfPorts):
            q.PTs[q.portLetters[iport]] = [q.str_void] * q.numOfPins
        
        whole = "".join(lins)
        PP = [ port.split('\n') for port in whole.split("##PORT") ] 
        
        
        #delete first element config name
        PP = PP[1:]

        #delete first element (port letter)
        PP = [ port[1:] for port in PP ]
        # delete [##end] element
        PP[-1] = PP[-1][:-1]

        for i in range(0, q.numOfPorts):
            for w in range(0, q.numOfPins):
                if PP[i][w] == "":
                    PP[i][w] = q.str_void #"volno" 
#        [pin = "volno" for pin in port if pin == ""]
        #pin = ["volno" for pin in port for port in PP if pin == ""]
        print(PP)

        # fill dictionary
        for iport in range(0, q.numOfPorts):
            q.PTs[q.portLetters[iport]] = PP[iport]
        #print(pins)

#        print("\n".join(["nove:","%"*80, str(q.PTs), "%"*80]))
        q.ACTUALIZE_view()
    def SAVE_config(q):
        q.UPDATE_fnames()
        lins = [q.save_fname]
        
        strPTs = [txPT.get(1.0,END) for txPT in q.txPTs]
        lins += [("##PORT%s\n%s") % (let, strPT) for (let,strPT) in zip(q.portLetters,strPTs)]
        lins += ["##END"]

        f = open(q.config_fname,'w')
        f.writelines(lins) 
        f.close() 
        print(lins)

    def ADD_sigNameAndActualize(q, *whatever):
        """ inserts signal name from text [txSigName] into dictionary [PTs]
        as stated in [txSelPin] and populates [txPTs] text fields"""
        q.ADD_sigName()
        q.ACTUALIZE_view()

    def INSERT_sigNameAndActualize(q, *whatever):
        """ inserts signal name from text [txSigName] into dictionary [PTs]
        as stated in [txSelPin] and populates [txPTs] text fields"""
        q.INSERT_sigName()
        q.ACTUALIZE_view()

    def ADD_sigNameFrom(q, strSelPin, strSigName):
        """ adds signal name = [txSigName] into dictionary [PTs]
        as stated in [txSelPin] to its current signal names """
        (suc,port, pin) = q.GET_PTX( strSelPin.strip() )
        q.APPEND_sigName(port,pin, strSigName.strip() )

    def ADD_sigName(q):
        """ adds signal name = [txSigName] into dictionary [PTs]
        as stated in [txSelPin] to its current signal names """
        (suc,port, pin) = q.GET_PTX( q.txSelPin.get(1.0, END).strip() )
        q.APPEND_sigName(port,pin, q.txSigName.get(1.0, END).strip() )

    def INSERT_sigName(q):
        """ inserts signal name = [txSigName] into dictionary [PTs]
        as stated in [txSelPin] instead of its previous value"""
        (suc,port, pin) = q.GET_PTX( q.txSelPin.get(1.0, END).strip() )
        q.PTs[port][pin] = q.txWholeValue.get(1.0, END).strip()


    def UPDATE_txWholeValue(q):
        """updates [txSigName] text value according to [PTs] dictionary """
        (suc,port, pin) = q.GET_PTX( q.txSelPin.get(1.0, END).strip() )
        sigName = q.PTs[port][pin]
        # if void??
        q.txWholeValue.delete(1.0, END)
        q.txWholeValue.insert(INSERT, sigName )
        
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
    def APPEND_sigName(q,port,pin,sigName):
        if sigName == q.str_void:
            return
        if q.PTs[port][pin] == q.str_void:
            q.PTs[port][pin] = sigName
            return
        signals = str(q.PTs[port][pin]).split(q.SCh)
        ss = set(signals)
        if sigName not in set(signals):
            print(signals)
            signals.append(sigName)
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
                    q.APPEND_sigName(port,pin,str_J)
    #            print('path: {}'.format(line))
        
        print(q.PTs)

    def GET_signalNames(q,port,pin):
        if q.PTs[port][pin] != q.str_void:
            return q.PTs[port][pin] 
        else:
            return ""

    def UPDATE_txPTs(q):
        strP = [ "\n".join( 
                [ q.GET_signalNames(port,pin) for pin in range(q.numOfPins) ]
            ) for port in q.portLetters 
            ] 
        [tx.delete(1.0, END) for tx in q.txPTs] 
        #insert contains of strPort
        [ tx.insert(INSERT,strP[port]) for tx, port in zip(q.txPTs, range(q.numOfPorts)) ]


    def ACTUALIZE_view(q, *whatever):
        q.UPDATE_txPTs()
        q.UPDATE_txWholeValue()

    def POPULATE_PTs_andActualize(q, *whatever):
        '''not used anymore'''
        
        q.POPULATE_PTs_from_txJXY()

        q.UPDATE_txPTs()
#        [ portq.PT[port]]
        #q.PTs["A"][4] = "J4"
#        print(q.PTs["A"])
        P__()
#        print(q.PTs)
#        strP = [ "\n xXx" for port in range(numOfPorts)] 

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
        #print(tk.TOP)
        #print(tk.BOTTOM)
        q.genJXY()
        q.POPULATE_PTs_from_txJXY()
        q.mainloop()
    def KEY_disable(q, evt):          
        ''' Makes the key do nothing'''
        #print(evt)
        return 'break' # <--------- this makes normal behaviour disabled
    def KEY_down(q, evt):          
        ''' Makes the key do nothing'''
        #print(evt)
        return 'break' # <--------- this makes normal behaviour disabled
    def SAVE_toPinmux(q):
        """Save file dialog to save dictionary [PTs] into xml file through module [xmlPars.py] """
        str_void = q.str_void
        PTs = q.PTs
        fname = q.txFilePinmux.get(1.0,END).strip()
        fname_new = fname
        REPLACE_xml_singalNames(fname, PTs, str_void, fname_new, makebackup=True)


def key(event):
    print("pressed", repr(event.char))

root = tk.Tk()
app = ExampleApp(root)
#app.bind('<Alt-g>', app.key)
#app.bind('<Alt-g>', key)
app.run()



#time.sleep(2)



# todos:
# save PTs to file
# saving dialog
# backpropagation:
# go through xml file pinmux.peb and find which port pins are availible -> color them in label view - to know

#text field for processing:
# e2=something;e3=something_else [Add]
# also a possibility for prefix to be asigned

#erase button

# iterating through permutations / or only changin first element fifo style in the signal names - by clicking on label

# loading from xml

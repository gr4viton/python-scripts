%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% There are things which are good to know, and they are in this file !! %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// TEMP
sdk_f_k22f
http://B50002@sw-stash.freescale.net/scm/mcucore/mcu-sdk.git
dev_ksdk_1.1_ga
dev_ksdk_1.2_ga

2015_01_21_-_dev_ksdk_1.1_ga
2015_01_21_-_dev_ksdk_1.2_ga

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[x] nove umistneni manualu - doc a schematics
"\\zcz09fs\PET\Manuals\Freescale\Kinetis L\L2KS\Board\SPF-28303_A.pdf"

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
____________________________________________________
nainstalovane programy..staci rozbalit
X:\Backup\testing\Clean_products\PExDrv_10.4.x
____________________________________________________
jak zjistit zda-li mcu m� podporu SDK nebo oboji nebo pouze SDK:
[ c:\_ACCUREV\Non_PEx_Files\DeviceSpreadsheet\DeviceSpreadsheet_Internal.xlsx ]
vyfiltrovat dle sloupce (napr         Kinetis subfamily)
sloupec 		= podpora
_________________________________
PE LDD Mcu comp. name 	= nonSDK
PE SDK Mcu comp. name	= SDK
____________________________________________________
carmen
ddavidek
longpwd
____________________________________________________
PROGRAMS
[] CW CWDS = CodeWarior Development Suite (complete IDE)
[] PE = Processor Expert - plugin to CW / Eclipse
 is a development system to create, configure, optimize, migrate, and deliver software components that generate source code for Freescale silicon.
[] CDE
[] DriverSuite
[] debugger openSDA
TSS - touchScreenSensor
pouzivat LDD componenty

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// ACCUREV
[]
View Streams -> a nad streamem ze kterejho  
-> show active -> transaction
-> show active
[] accurev - navod na instalaci
ddavidek
core id pswrd
Z:\Documentation\Tasks\2013\Hiring - Training Materials

[] MCU_REL revision number- nekdy do resolution - resolve do jiry chce to c�slo..
najet na soubor a d�t history
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
/ Eclipse 
[] workbench window positions settings
\.metadata\.plugins\org.eclipse.e4.workbench\workbench.xmi
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// PE
Zajiste vsichni vite, ze seznam vsech dulezitych milestones tykajicich se Processor Expertich produktu je zde:
http://compass.freescale.net/go/pexstatus
- nedivali se tak uz asi neni

[] PE project refresh - po rucni editaci .pa
____________________________________________________
>> COMPONENTS
[] kdyz nechci inicializovat komponentu tak auto Initialization!
[] Enable component - ppo rucn� editac .pe
[] dokumentace komponent na 
freescale.com
reference
v RpR ty dokumentace pise: Peter Moravcik
[] PWM timer
- pokud chci PWM na 2 pinech ktere sdileji stejny timer 
  -- musi mit jeden TimeUnit component 
  -- tzn spolecne nastaveni TIM_X (perioda..)
  -- ktery prave muze mit tech vic channelu..
  -- takze pridam dva PWM_LDD, ale nechame je odkazovat na stejny TU..
  -- ten TU muzou pouzivat i dalsi komponenty / vystup na piny = ostatni kanaly TIM_X, ale maji pak stejne nastaveni (periodu..)
[] RTC_ldd = vyuziva primo RTC chip
RealTime_LDD = nad jakymkoliv timerem
- Zapnout clock RTC chipu 
 --> Components - Processors - Cpu 
 --> Components Inspector - Clock settings - RTC clock input = Enabled
[]  seznam v�ech PE podporovan�ch MCU lze vyvolat
 - Processor Expert -> #Extras -> Export Supported Components and Licences - XLS
____________________________________________________
>> Component inspector 
-> dyz das value doleva od Name..tak

____________________________________________________
>> IAR
iar in PExDS.. addo version 6.50

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// KDS
[] odinstalace obcas nestac�
- mus� se smazat i obsah slo�ky instalace (zustavaj� pluginy) 2014_08_18
- C:\ProgramData\Processor Expert\PECache\ - obcas pomo�e smazat.. (stac� posledn�
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// PE Micro OpenSDA
[] nen� radno nech�vat pripojene 2 desky obe s OpenSDA
- je to pomalejsi !
-  teoreticky muze vest k chybe?
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// IAR
____________________________________________________
DEBUGGERs
nad projectem: [Options - Debugger]
[] J-Link

[] PE micro 
- [Setup - Driver: PE micro]
- [Download - [x] Use flash loader(s)]
[Debugger -> PE micro]
- [P&E Hardware interface type: USB Multilink (FX)]
- [Interface: SWD] # pokud swd

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
// HW
[] terminal nejede -> odpojit a pripojit usb konektor
[] i2c spadlo -> odpojit a pripojit usb konektor
[] debugger 
- OpenSDA = PE micro
 -- kdy� nejde.. - pc nevid� procesor
  --- vypojit desku i debugger
  --- zapojit desku
  --- zapojit debugger
  --- vytahnout a zapojit kabel (1 na jednicku)

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% SITES
[] helpdesk - ticket add
https://hclfslitsm.service-now.com/ess/
[] service desk
http://servicedesk.freescale.net/
[x] roznovsky zapisnik dochazky
http://bigm.ea.freescale.net/attendance/index.asp?menu=2&m=6&y=2014	    
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PR
// communication
[] wiki 30-04-2014
http://freeshare.freescale.net:2222/public/pem-cmty-svc/Lists/RecentWiki/Product%20Engineering/Releases%20overview.aspx
[] outlook online
web posta: https://outlook.office365.com
napis tam len svoj email a nedavaj enter. daj len tab... to sa zazracne prepne. a potom sa prihlasis cez b50002

//week report
P:\ZCZ09\Wiki\PEx-weekly summary report

// lidi
vr�tnice t222

Vlady  t      | Ondra Lutera    t   
Palo   t      | Laco     t   
ja     t420   | Ladislav t420 
�tepan t      | Marek Neuzil t   

	    
Bastek JOZEF-B23207 = Jozo
Vadkerti LADISLAV-B23189 = laco
Ukropec LIBOR-B23185 = pc
Olga
Marek Vinkler

Martin form�nek - cesta z lomnice..
Jirka - vpravo CCW 1 
 - MCU drsnak - xts ci jaka obdoba raspi -> udelal si k tomu touchdisp driver etc!
Karel
____________________________________________________
Trmac MAREK-B23204
http://freeshare.freescale.net:2222/my/Person.aspx?accountname=fsl\B23204
____________________________________________________
Petr Cach - vysoky
http://freeshare.freescale.net:2222/Pages/people_search_results.aspx?k=petr%20cach
____________________________________________________
ZCZ09
http://freeshare.freescale.net:2222/Pages/people_search_results.aspx?k=ZCZ09
____________________________________________________

____________________________________________________
Hluchan RADIM-B23198 - gray mluvka
http://freeshare.freescale.net:2222/my/Person.aspx?accountname=fsl\B23198
____________________________________________________
Filip vojtech - beatle
http://freeshare.freescale.net:2222/my/Person.aspx?accountname=fsl\B23183
____________________________________________________
Petr Struzka - kortez
Struzka Petr-B23200
http://freeshare.freescale.net:2222/my/Person.aspx?accountname=fsl\B23200

____________________________________________________
Standa - vousvlas

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
LAUGHT
- fifo skr�n



http://tunein.com/radio/100-Chill-Radio-s144548/

http://www.di.fm/chilloutdreams

� a dalsie ?



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
files

phonebook:
\\zcz09carmen\PET\ZCZ09\PhoneBook\phone book FSL_04-06-2014.xlsx
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
attendence
-> dy� nemocen tak vol�m olze! ona to zad�!
-> zad�vat �e nepracoval - to mo�e zmenit.. ale pracoval na nepracoval nezmeni 
-> print to pdf - options -> advanced -> scale 77
-> pak print - tray 2 - a4

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[] nove pluginy
\\zcz09fs\PExCore\Eclipse
http://zcz09fs/PExCore/Eclipse

Mimo jine to prinasi i vyhodu moznosti pristupu na pluginy pres HTTP rozhrani, cili update site v eclipse lze zadat pro RT7 napr takto:
http://zcz09fs/PExCore/Eclipse/RT7/site



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
ondra lutera - je z fektu 
- zn� doktorandy na robotice aj automatizaci - byli s nim v rocniku
kr�z, �tastn�, rozmocil?, �panel?

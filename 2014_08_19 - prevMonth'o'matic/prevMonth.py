
#najit soubor thisMonth ve spravne slo�ce
#otev��t ho pro �ten�

#zkop�rovat ho cel� do textov�ho �et�zce
str = file
# promazat nevypln�n� pozn�mky?? 
# bacha aby se nesmazala:
#[]
#sadasd
#asd
#

done = 1
# separace notes
while done:
    # X = prvn� pozn�mka v pracovn� ��sti textu

    # te� se hled� jestli je X je posledn� / jedin� v dan�m m�s�ci
    #naj�t redex
    a = [.]...#>?.d_
    # nebo jestli je za n� bl�e druh� pozn�mka
    b = [.]...[]

    c = b
    if len(a)<len(b):
        # tzn �e je dal�� (druh�) pozn�mka k X bl�e ne� konec m�s�ce 
        # tzn bereme jako note tu krat��
        # etc
        c = a


    note = str[ c.start, c.len ]

    # zjist�me typ pozn�mky
    # tzn co je uprost�ed [] vs [x] .@..
    note_char = redex(note,"[]")
    switch(note_char):
        case "x":
            #nic
        case "..":
            # nic
        case "":
            # berem ju a z�rove� 
            # p�ed �u budem d�vat symbol za�azen� do historie = @@
            undone_notes.text.add(note)
#            undone_notes.pos.add(pos_so_far+c.start)
    # useknem note z pracovn�ho �et�zce
    trimmed_len = c.start + c.len
    str = ltrim(str,trimmed_len)
    # a pokra�ujeme dal�� note..

# znovu na�tem soubor
# zkop�rovat ho cel� do textov�ho �et�zce
str = file

# proj�d�me string postupn� redexem a hled�me nevypln�n� pozn�mky
a = \r[] 
# pokud nalezneme dopln�me na za��tek ��dku znak archivace @@


# nakonec p�id�me nakonec stringu ��ru a v�ecky undone_notes
str=str+"%%%%%%%%%%%%%%%%%%%%%%%"
for note_text in undone_notes.text:
    str = str + note_text

# a zap�eme do souboru
file.write(str)


# promazat od pr�zdn�ch dn�
# * od pr�zdn�ch spac�ch hodin
# *

# vytvo�it nov� a zapsat do star�ho..

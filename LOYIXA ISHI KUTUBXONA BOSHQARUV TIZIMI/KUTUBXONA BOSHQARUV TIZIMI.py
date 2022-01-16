from tkinter import *
import tkinter.messagebox
import LibBksDatabase


class Library:

    def __init__(self, root):
        self.root = root
        self.root.title("Kutubxona Boshqaruv Tizimini Loyixalash")
        self.root.geometry("1360x750+0+0")

        MTy = StringVar()
        Ref = StringVar()
        Tit = StringVar()
        fna = StringVar()
        sna = StringVar()
        Adr1 = StringVar()
        Adr2 = StringVar()
        pcd = StringVar()
        MNo = StringVar()
        BkID = StringVar()
        Bkt = StringVar()
        Atr = StringVar()
        DBo = StringVar()
        Ddu = StringVar()
        sPr = StringVar()
        LrF = StringVar()
        DoD = StringVar()
        DonL = StringVar()

        # =============================================HisobKitoblar=====================================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Kutubxona Boshqaruv Tizimini Loyixalash", "Chiqishni Xoxlasangiz, Tasdiqlang")
            if iExit > 0:
                root.destroy()
                return

        def ClearData():
            self.txtMType.delete(0, END)
            self.txtBkID.delete(0, END)
            self.txtRef.delete(0, END)
            self.txtBkt.delete(0, END)
            self.txtTit.delete(0, END)
            self.txtAtr.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtsna.delete(0, END)
            self.txtDdu.delete(0, END)
            self.txtAdr1.delete(0, END)
            self.txtAdr2.delete(0, END)
            self.txtDonL.delete(0, END)
            self.txtLrF.delete(0, END)
            self.txtpcd.delete(0, END)
            self.txtDoD.delete(0, END)
            self.txtMNo.delete(0, END)
            self.txtsPr.delete(0, END)
            self.txtDBo.delete(0, END)


        def addData():
            if(len(MTy.get())!=0):
               LibBksDatabase.addDataRec(MTy.get(),Ref.get(),Tit.get(),fna.get(),sna.get(),Adr1.get(),Adr2.get(),pcd.get(), \
                    MNo.get(),BkID.get(),Bkt.get(),Atr.get(),DBo.get(),Ddu.get(),sPr.get(),LrF.get(),DoD.get(),DonL.get())

               booklist.delete(0,END)
               booklist.insert(END,(MTy.get(),Ref.get(),Tit.get(),fna.get(),sna.get(),Adr1.get(),Adr2.get(),pcd.get(), \
                    MNo.get(),BkID.get(),Bkt.get(),Atr.get(),DBo.get(),Ddu.get(),sPr.get(),LrF.get(),DoD.get(),DonL.get()))
            

        def DisplayData():
            booklist.delete(0,END)
            for row in LibBksDatabase.viewData():
                booklist.insert(END,row)


        def SelectedBook(event):
            global sb
            searchBk = booklist.curselection()[0]
            sb = booklist.get(searchBk)

            self.txtMType.delete(0, END)
            self.txtMType.insert(END,sb[1])
            self.txtBkID.delete(0, END)
            self.txtBkID.insert(END,sb[2])
            self.txtTit.delete(0, END)
            self.txtTit.insert(END,sb[3])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END,sb[4])
            self.txtsna.delete(0, END)
            self.txtsna.insert(END,sb[5])
            self.txtAdr1.delete(0, END)
            self.txtAdr1.insert(END,sb[6])
            self.txtAdr2.delete(0, END)
            self.txtAdr2.insert(END,sb[7])
            self.txtpcd.delete(0, END)
            self.txtpcd.insert(END,sb[8])
            self.txtMNo.delete(0, END)
            self.txtMNo.insert(END,sb[9])
            self.txtRef.delete(0, END)
            self.txtRef.insert(END,sb[10])
            self.txtBkt.delete(0, END)
            self.txtBkt.insert(END,sb[11]) 
            self.txtAtr.delete(0, END)
            self.txtAtr.insert(END,sb[12])
            self.txtDBo.delete(0, END)
            self.txtDBo.insert(END,sb[13])
            self.txtDoD.delete(0, END)
            self.txtDoD.insert(END,sb[14])
            self.txtsPr.delete(0, END)
            self.txtsPr.insert(END,sb[15])
            self.txtLrF.delete(0, END)
            self.txtLrF.insert(END,sb[16]) 
            self.txtDdu.delete(0, END)
            self.txtDdu.insert(END,sb[17])
            self.txtDonL.delete(0, END)
            self.txtDonL.insert(END,sb[18])


        def DeleteDate():
            if(len(MTy.get())!=0):
                LibBksDatabase.deleteRec(sb[0])
                ClearData()
                DisplayData()

        def searchDatabase():
            booklist.delete(0,END)
            for row in LibBksDatabase.searchData(MTy.get(),Ref.get(),Tit.get(),fna.get(),sna.get(),Adr1.get(),\
                        Adr2.get(),pcd.get(),\
                          MNo.get(),BkID.get(),Bkt.get(),Atr.get(),DBo.get(),Ddu.get(),sPr.get(), \
                          LrF.get(),DoD.get(),DonL.get()):
                booklist.insert(END,row)


        def update():
            if(len(MTy.get())!=0):
                LibBksDatabase.dataUpdate(sb[0],MTy.get(),Ref.get(),Tit.get(),fna.get(),sna.get(),Adr1.get(),\
                                          Adr2.get(),pcd.get(),\
                           MNo.get(),BkID.get(),Bkt.get(),Atr.get(),DBo.get(),Ddu.get(),sPr.get(), \
                                          LrF.get(),DoD.get(),DonL.get())
                                          
                                                  
            

        # =============================================Jadvallar=====================================================


        
        MainFrame = Frame(self.root, bd=10, bg='powder blue')
        MainFrame.grid()

        TitFrame = Frame(MainFrame, width=1300, padx=60, bd=15, relief=RIDGE)
        TitFrame.pack(side=TOP)
        
        self.lblTit = Label(TitFrame, width=33, font=('arial', 40, 'bold'), text="    Kutubxona boshqaruv tizimini Loyixalash\t",)
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=20, width=1200, height=90, padx=20, pady=20, bg="powder blue",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)


        FrameDetail = Frame(MainFrame, bd=15, width=1300, height=100, padx=20, relief=RIDGE,bg="powder blue" )
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=15, width=700, height=600, padx=20, relief=RIDGE, bg="powder blue")
        DataFrame.pack(side=BOTTOM)

        
        DataFrameLEFT = LabelFrame(DataFrame, bd=10, width=800, height=400, padx=13, pady=2, relief=RIDGE, bg="powder blue",
                                   font=('arial', 12, 'bold'), text=" Kutubxonaga azolik togrisidagi malumot:")
        DataFrameLEFT.pack(side=LEFT)


        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=420, height=400, padx=10, relief=RIDGE,
                                    bg='powder blue', font=('arial',12, 'bold'), text="Kitob Tavfsilotlari:",)
        DataFrameRIGHT.pack(side=RIGHT)


    

        # =============================================Amallar=====================================================

        self.lblMemberType =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Azolik Turi:", padx=2, pady=2,
                                   bg='powder blue')
        self.lblMemberType.grid(row=0, column =0, sticky=W)

        self.txtMType =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=MTy, width=25)
        self.txtMType.grid(row=0, column =1)


        self.lblBkID =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Kitob ID:", padx=2, pady=2, bg='powder blue')
        self.lblBkID.grid(row=0, column =2, sticky=W)
        self.txtBkID =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=BkID, width=25)
        self.txtBkID.grid(row=0, column =3)


        self.lblRef =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Tartib Raqam:", padx=2, pady=2, bg='powder blue')
        self.lblRef.grid(row=1, column =0, sticky=W)
        self.txtRef =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Ref, width=25)
        self.txtRef.grid(row=1, column =1)


        self.lblBkt =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Kitob Nomi:", padx=2, pady=2, bg='powder blue')
        self.lblBkt.grid(row=1, column =2, sticky=W)
        self.txtBkt =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Bkt, width=25)
        self.txtBkt.grid(row=1, column =3)


        self.lblTit =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Jinsi:", padx=2, pady=2, bg='powder blue')
        self.lblTit.grid(row=2, column =0, sticky=W)
        self.txtTit =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Tit, width=25)
        self.txtTit.grid(row=2, column =1)


        self.lblAtr =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Muallif:", padx=2, pady=2, bg='powder blue')
        self.lblAtr.grid(row=2, column =2, sticky=W)
        self.txtAtr =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Atr, width=25)
        self.txtAtr.grid(row=2, column =3)


        self.lblfna =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Ism:", padx=2, pady=2, bg='powder blue')
        self.lblfna.grid(row=3, column =0, sticky=W)
        self.txtfna =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=fna, width=25)
        self.txtfna.grid(row=3, column =1)


        self.lblDBo =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Ijara Sanasi:", padx=2, pady=2, bg='powder blue')
        self.lblDBo.grid(row=3, column =2, sticky=W)
        self.txtDBo =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DBo, width=25)
        self.txtDBo.grid(row=3, column =3)


        self.lblsna =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Familiyasi:", padx=2, pady=2, bg='powder blue')
        self.lblsna.grid(row=4, column =0, sticky=W)
        self.txtsna =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=sna, width=25)
        self.txtsna.grid(row=4, column =1)


        self.lblDdu =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Muddat:", padx=2, pady=2, bg='powder blue')
        self.lblDdu.grid(row=4, column =2, sticky=W)
        self.txtDdu =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Ddu, width=25)
        self.txtDdu.grid(row=4, column =3)


        self.lblAdr1 =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Manzil 1:", padx=2, pady=2, bg='powder blue')
        self.lblAdr1.grid(row=5, column =0, sticky=W)
        self.txtAdr1 =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Adr1, width=25)
        self.txtAdr1.grid(row=5, column =1)


        self.lblDonL =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Ijaraga Olgan Kunlari:", padx=2, pady=2, bg='powder blue')
        self.lblDonL.grid(row=5, column =2, sticky=W)
        self.txtDonL =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DonL, width=25)
        self.txtDonL.grid(row=5, column =3)


        self.lblAdr2 =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Manzil 2:", padx=2, pady=2, bg='powder blue')
        self.lblAdr2.grid(row=6, column =0, sticky=W)
        self.txtAdr2 =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Adr2, width=25)
        self.txtAdr2.grid(row=6, column =1)


        self.lblLrF =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Kech Qaytish Jarimasi:", padx=2, pady=2, bg='powder blue')
        self.lblLrF.grid(row=6, column =2, sticky=W)
        self.txtLrF =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=LrF, width=25)
        self.txtLrF.grid(row=6, column =3)


        self.lblpcd =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Pochta Indeksi:", padx=2, pady=2, bg='powder blue')
        self.lblpcd.grid(row=7, column =0, sticky=W)
        self.txtpcd =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=pcd, width=25)
        self.txtpcd.grid(row=7, column =1)


        self.lblDoD =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Muddatidan Otgan:", padx=2, pady=2, bg='powder blue')
        self.lblDoD.grid(row=7, column =2, sticky=W)
        self.txtDoD =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DoD, width=25)
        self.txtDoD.grid(row=7, column =3)


        self.lblMNo =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Mobil Raqam:", padx=2, pady=2, bg='powder blue')
        self.lblMNo.grid(row=8, column =0, sticky=W)
        self.txtMNo =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=MNo, width=25)
        self.txtMNo.grid(row=8, column =1)

        self.lblsPr =Label(DataFrameLEFT, font=('arial', 12, 'bold'), text="Sotish Narxi:", padx=2, pady=2, bg='powder blue')
        self.lblsPr.grid(row=8, column =2, sticky=W)
        self.txtsPr =Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=sPr, width=25)
        self.txtsPr.grid(row=8, column =3)


        # =============================================Listbox va Scrollbar=====================================================

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, stick ='ns')

        booklist = Listbox(DataFrameRIGHT,width=45, height=12, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        booklist.bind('<<ListboxSelect>>', SelectedBook)
        booklist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=booklist.yview)


        # =============================================Knopkalar=====================================================

        self.btnAddData=Button(ButtonFrame, text='Bazaga Qoshish', font=('arial', 14, 'bold'), height=3, width=14, bd=7, command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData=Button(ButtonFrame, text='Bazadan Korish', font=('arial', 14, 'bold'), height=3, width=14, bd=7, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData=Button(ButtonFrame, text='Tozalash', font=('arial', 14, 'bold'), height=3, width=13, bd=7, command=ClearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData=Button(ButtonFrame, text='Ochirish', font=('arial', 14, 'bold'), height=3, width=13, bd=7, command=DeleteDate)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnUpdateData=Button(ButtonFrame, text='Yangilash', font=('arial', 14, 'bold'), height=3, width=13, bd=7, command=update)
        self.btnUpdateData.grid(row=0, column=4)

        self.btnSearchData=Button(ButtonFrame, text='Qidirish', font=('arial', 14, 'bold'), height=3, width=13, bd=7, command=searchDatabase)
        self.btnSearchData.grid(row=0, column=5)

        self.btnExitData=Button(ButtonFrame, text='Chiqish', font=('arial', 14, 'bold'), height=3, width=13, bd=7, command=iExit)
        self.btnExitData.grid(row=0, column=6)





if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()

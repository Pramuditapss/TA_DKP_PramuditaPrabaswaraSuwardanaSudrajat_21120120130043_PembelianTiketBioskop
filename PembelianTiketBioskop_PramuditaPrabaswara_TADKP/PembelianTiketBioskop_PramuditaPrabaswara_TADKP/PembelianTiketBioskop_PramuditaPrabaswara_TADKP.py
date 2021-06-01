from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def submit():
    #NAMA
    if  stringnama.get() == "":
        messagebox.showerror("Error","BELUM MENGISI NAMA")
        return
    else :
        for character in stringnama.get():
            if character.isdigit() == True :
                messagebox.showerror("Error","TOLONG ISI NAMA DENGAN BENAR")
                return
    #FILM
    pembelian=""
    if film.get()== 0:
        messagebox.showerror("Error","BELUM MEMILIH FILM")
        return
    elif film.get() == 1:
        pembelian=" BLACK PANTHER "
    elif film.get() == 2:
        pembelian=" DOCTOR STRANGE "
    elif film.get() == 3:
        pembelian=" CAPTAIN MARVEL "
    #WAKTU   
    if strjam.get() == "WAKTU":
        messagebox.showerror("Error","BELUM MEMILIH WAKTU")
        return
    #TIKET
    harga=""
    if strtkt.get() == "JUMLAH TIKET":
        messagebox.showerror("Error","BELUM MEMILIH JUMLAH TIKET")
        return
    elif strtkt.get() == "1":
        harga=" Rp 50.000 "
    elif strtkt.get() == "2":
        harga=" Rp 100.000 "
    elif strtkt.get() == "3":
        harga=" Rp 150.000 "
    elif strtkt.get() == "4":
        harga=" Rp 200.000 "
    elif strtkt.get() == "5":
        harga=" Rp 250.000 "
    #HARI   
    hari=""
    if strhr.get() == "HARI":
        messagebox.showerror("Error","BELUM MEMILIH HARI")
        return
    elif strhr.get() == "SENIN":
        hari="SENIN"
    elif strhr.get() == "SELASA":
        hari="SELASA"
    elif strhr.get() == "RABU":
        hari="RABU"
    elif strhr.get() == "KAMIS":
        hari="KAMIS"
    elif strhr.get() == "JUMAT":
        hari="JUMAT"
    elif strhr.get() == "SABTU":
        hari="SABTU"
    elif strhr.get() == "MINGGU":
        hari="MINGGU"
    #OUTPUT   
    pesan = "Pemesanan atas nama " + stringnama.get() + " dengan jumlah " + strtkt.get() +" tiket"  + " untuk Film " + pembelian + " pada pukul " + strjam.get() + " untuk hari " + hari +" berhasil!\n" + "Total Harga : " + harga + "\n" + "Tiket Akan Segera Dicetak\n" 
    messagebox.showinfo("PEMESANAN", pesan)

    cetak = "...".join(str(cetak) 
    for cetak in range(5, 0, -1))
    messagebox.showinfo("MENCETAK...", (cetak))
    



#GUI
top = Tk()  
top.geometry("500x250")
top.title("PEMBELIAN TIKET BIOSKOP XII")
top.configure(background="#cee5d5")

#gambar bg
bg1 = PhotoImage(file="D:/BG/CINEMA1.png")
#canvas
my_canvas = Canvas(top, width=500, height=250)
my_canvas.pack(fill="both", expand=True)
#memasang gambar
my_canvas.create_image(0,0, image=bg1, anchor="nw")
#label xii
my_canvas.create_text(370, 55, text="XII", font=("Times", 75), fill="#FFD700")

#label  
lbnama      = Label(top, text = "NAMA\t:", bg = "#B22222").place(x = 30,y = 10)    
lbfilm      = Label(text = "FILM\t:", bg = "#B22222").place(x = 30, y=40)
lbjam       = Label(text = "JAM\t:", bg = "#B22222").place(x=30, y=110)
lbtiket     = Label(text = "TIKET\t:", bg = "#B22222").place(x=30, y=135)
lbhari      = Label(text = "HARI\t:", bg = "#B22222").place(x=30, y=160)

#input nama user  
stringnama = StringVar()
inama = Entry(top,width = 20, textvariable=stringnama).place(x = 105, y = 10) 
angka =  [str(x) for x in range(0,999999)]

#radio film
film = IntVar()
R1 = Radiobutton(top, text="BLACK PANTHER      ", variable=film, value=1).place(x=105, y=40)  
R2 = Radiobutton(top, text="DOCTOR STRANGE   ", variable=film, value=2).place(x=105, y=60)  
R3 = Radiobutton(top, text="CAPTAIN MARVEL    ", variable=film, value=3).place(x=105, y=80)  

#combobox jam
strjam = StringVar(value='WAKTU')
Cb1 = ttk.Combobox(top, width = 10, textvariable = strjam, state="readonly")
Cb1.place(x=105, y=110)

#list jam
Cb1['values'] = ('12:00','15:30','17:00','20:15','22:00')

#combobox tiket
strtkt = StringVar(value= 'JUMLAH TIKET')
Cb2 = ttk.Combobox(top, width = 20, textvariable = strtkt, state= "readonly")
Cb2.place(x=105, y=135)

#list tiket
Cb2['values'] = ('1','2','3','4','5')

#combobox hari
strhr = StringVar(value= 'HARI')
Cb3 = ttk.Combobox(top, width = 15, textvariable = strhr, state= "readonly")
Cb3.place(x=105, y=160)

#list hari
Cb3['values'] = ('SENIN','SELASA','RABU','KAMIS','JUMAT','SABTU','MINGGU')

#button 
btn1 = Button(top, command = submit,bg= "#B22222", text="KONFIRMASI PEMESANAN").place(x=120,y=200)
btn2 = Button(top, command = top.quit,bg= "#B22222", text="KELUAR").place(x=300,y=200)

top.mainloop()


#function merupakan term umum di bahasa pemrograman
#function adalah konsep dalam programing yang memungkinkan kita menggabungkan beberapa kode dalam satu entitas 
#sehingga kapanpun kita memerlukan gabungan dari beberapa kode, kita tinggal panggil entitas function nya
def luasSegitiga(t,a):
    tinggi=t
    alas=a
    luas=0.5*alas*tinggi
    print (luas)

def voltaseHambatan(I,R):
    arus_listrik=I
    hambatan_listrik=R
    voltasehambatan=I*R
    print(voltasehambatan)

def voltaseDaya(P,I):
    daya_listrik=P
    arus_listrik=I
    voltasedaya=P/I
    print(voltasedaya)

def massaJenis(m,v):
    massa_benda=m
    volume_benda=v
    massajenis=m/v
    print(massajenis)

def energiPotensial(m,g,h):
    massa_benda=m
    gravitasi_bumi=g
    ketinggian_benda=h
    energipotensial=m*g*h
    print(energipotensial)

def energiKinetik(m,v):
    massa_benda=m
    kecepatan_benda=v
    energikinetik=0.5*m*v**2
    print(energikinetik)



class Mahasiswa:
    def __init__(self, nama, npm, ipk, maxsks):
        self.nama = nama
        self.npm = npm
        self.ipk = ipk
        self.maxSKS = maxsks
        self.sks = 0

    def __gt__(self, obj2):
        return self.ipk > obj2.ipk

    def __repr__(self):
        return 'Mahasiswa({}, {}, {}, {})'.format(self.nama, self.npm, self.ipk, self.maxSKS)
        
    def __str__(self):
        return 'Namanya {}'.format(self.nama)
    
    def aturMaxSKS(self,maxbaru):
        self.maxSKS = maxbaru
        print("SKS maksimum untuk {} adalah {} SKS".format(self.nama,self.maxSKS))
    def tambahSKS(self,tambahan):
        if self.sks + tambahan <= self.maxSKS:
            self.sks += tambahan
            print("SKS untuk {} berhasil ditambah menjadi {} SKS".format(self.nama,self.sks))
        else:
            print("SKS untuk {} tidak dapat ditambah kembali".format(self.nama))
    def kurangiSKS(self,kurangan):
        self.sks -= kurangan
        print("SKS untuk {} berhasil dikurangi menjadi {} SKS".format(self.nama,self.sks))
    def aksi(self):
        print("Hidup Mahasiswa, Hidup Rakyat Indonesia!")
            
        

class MahasiswaUI(Mahasiswa):
    def __init__(self,nama,npm,ipk,sks,makara):
        super().__init__(nama,npm,ipk,sks)
        self.makara = makara

    def aksi(self):
        super().aksi()
        print("Kepal jari jadi tinju, UI, UI, Kampusku, Bersatu Almamaterku, UI!")

    def printMakara(self):
        print(self.makara)

    def kurangiSKS(self, kurangan):
        if self.sks - kurangan >= 12:
            super().kurangiSKS(kurangan)
        else:
            print("Tidak Boleh")

    def updateIPK(self,new):
        self.ipk = new
        

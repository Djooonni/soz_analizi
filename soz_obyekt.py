from soz_analizi.shekilci import *
from soz_analizi.shekilciler import *
from operator import itemgetter
from soz_analizi.soz import *

class s_obyekt:

    def __init__(self,soz='asdsa'):
        if  soz=='asdsa':
            self.sozler=[]
        else:
            if hasattr(self,'sozler'):
                self.sozler.append(soz)
            else:
                self.sozler=[soz]

            self.qerar_ver()

    def add(self,soz):
        self.sozler.append(soz)
        self.qerar_ver()

#    def __repr__(self):
#        return {'name':str(self.sozler), 'age':str(len(self.sozler))}

    def __str__(self):
        if hasattr(self,'secilmis'):
            return str(self.secilmis.ozu)+' options: '+str(len(self.sozler))
        else:
            return 'tapilmadi'

    def qerar_ver(self):
        self.secilmis=self.sozler[0]

    def get_class(self):
        if self.secilmis.nitq=='X':
            return 'symbol'
        else:
            return 'word'

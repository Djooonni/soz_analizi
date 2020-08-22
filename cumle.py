from soz_analizi import *
from soz_analizi.soz import *
from soz_analizi.soz_obyekt import *
import nltk

class cumle:
    def __init__(self,metn):
        self.metn=metn
        self.vahidler_s=nltk.word_tokenize(self.metn)
        self.vahidler=[]
        for ak in self.vahidler_s:
            if(ak=='\n'):
                continue
            variantlar=deqiq_olsun(duzelt(ak))

            if len(variantlar)==0:
                soza=sz(ak)
                soza.nitq='X'
                s_o=s_obyekt(soza)
            else:
                s_o=s_obyekt()
                for w in variantlar:
                    s_o.add(w)

            self.vahidler.append(s_o)

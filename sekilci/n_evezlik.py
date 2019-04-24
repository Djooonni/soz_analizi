from soz_analizi.shekilci import *
from soz_analizi.sekilci.stringler import *




ev_cem=[sekilci(['lar','lər'],1,'0',"Cem")]
ev_hal=[sekilci(['nın','nin','nun','nün'],3,'-',"yiyelik"),sekilci(['ya','yə'],1,'-',"yonluk"),sekilci(['nı','ni','nu','nü'],3,'-',"tesirlik"),
       sekilci(['da','də'],1,'0',"yerlik"),sekilci(['dan','dən'],1,'0',"cixisliq")]
ev_men=[sekilci(['ım','im','um','üm'],3,'-',"Mənsubiyyət 1"),sekilci(['ın','in','un','ün'],3,'-',"II"),sekilci(['sı','si','su','sü'],3,'-',"III"),
       sekilci(['ımız','imiz','umuz','ümüz'],3,'-',"IC"),sekilci(['ınız','iniz','unuz','ünüz'],3,'0',"IIC")]
ev_sex=[sekilci(['yam','yəm'],1,'-',"1Tek"),sekilci(['san','sən'],1,'0',"2tek"),sekilci(['dır','dir','dur','dür'],3,'0',"3tek"),
       sekilci(['yıq','yik','yuq','yük'],3,'-',"1cem"),sekilci(['sınız','siniz','sunuz','sünüz'],3,'0',"2cem"),sekilci(['dırlar','dirlər','durlar','dürlər'],3,'0',"3cem")]


for pol in ev_cem:
    pol.sonra=[ev_men,ev_hal,ev_sex]
for pol in ev_men:
    pol.sonra=[ev_hal,ev_sex]
for pol in ev_hal:
    if pol.adi=='yonluk':
        pol.sonra=[[sekilci(['dır','dir','dur','dür'],3,'0',"3tek"),sekilci(['dırlar','dirlər','durlar','dürlər'],3,'0',"3cem")]]
    else:
        pol.sonra=[ev_sex]

"""
for pol in s_isim:
    pol.sonra = [i_sex]
for pol in s_fel:
    pol.sonra  = [i_sex]
"""
n_evezlik = [ev_cem, ev_hal,ev_men,ev_sex] #isimden duzelen

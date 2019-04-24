from soz_analizi.shekilci import *
from soz_analizi.sekilci.stringler import *

i_cem=[sekilci(['lar','lər'],1,'0',"Cem")]
i_hal=[sekilci(['nın','nin','nun','nün'],3,'-',"yiyelik"),sekilci(['ya','yə'],1,'-',"yonluk"),sekilci(['nı','ni','nu','nü'],3,'-',"tesirlik"),
       sekilci(['da','də'],1,'0',"yerlik"),sekilci(['dan','dən'],1,'0',"cixisliq")]
i_men=[sekilci(['ım','im','um','üm'],3,'-',"IT"),sekilci(['ın','in','un','ün'],3,'-',"IIT"),sekilci(['sı','si','su','sü'],3,'-',"IIIT"),
       sekilci(['ımız','imiz','umuz','ümüz'],3,'-',"IC"),sekilci(['ınız','iniz','unuz','ünüz'],3,'-',"IIC")]
i_sex=[sekilci(['yam','yəm'],1,'-',"1Tek"),sekilci(['san','sən'],1,'0',"2tek"),sekilci(['dır','dir','dur','dür'],3,'0',"3tek"),
       sekilci(['yıq','yik','yuq','yük'],3,'-',"1cem"),sekilci(['sınız','siniz','sunuz','sünüz'],3,'0',"2cem"),sekilci(['dırlar','dirlər','durlar','dürlər'],3,'0',"3cem")]

for pol in i_cem:
    pol.sonra=[i_men,i_hal,i_sex[3:]]
for pol in i_men:
    if pol.adi == 'IT' or pol.adi == 'IC':
        pol.sonra=[i_hal,i_sex[1:3]+i_sex[4:]]
        continue
    if pol.adi == 'IIT' or pol.adi == 'IIC':
        pol.sonra=[i_hal,i_sex[0:1]+i_sex[2:4]+i_sex[5:]]
        continue

    if pol.adi == 'IIIT':
        pol.sonra=[i_hal,i_sex]
        pol.sonra[0][1].forma=['na','nə']#bitişdirici samir dəyişir
    else:    
        pol.sonra=[i_hal,i_sex]
    
for pol in i_hal:
    if pol.adi=='yonluk' or pol.adi=='yiyelik' or pol.adi=='tesirlik':
        pol.sonra=[[sekilci(['dır','dir','dur','dür'],3,'0',"3tek"),sekilci(['dırlar','dirlər','durlar','dürlər'],3,'0',"3cem")]]
    else:
        pol.sonra=[i_sex]

n_isim=[i_cem,i_men,i_hal,i_sex]



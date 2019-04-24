from soz_analizi.shekilci import *
from soz_analizi.sekilci.stringler import *


istisnalar = ['bildirmək', 'döyündü', 'yuyundu', 'daranmaq']
f_zaman = [sekilci(['yır','yir','yur','yür'],3,'-',"indiki zaman"),
	sekilci(['dı','di','du','dü'],3,'0',"shuhudi kecmish zaman"),
	sekilci(['mış','miş','muş','müş'],3,'0',"neqli kecmish zaman1"),
	sekilci(['yıb','yib','yub','yüb'],3,'-',"neqli kecmish zaman"),
	sekilci(['yacaq','yəcək'],1,'-',"qeti gelecek zaman"),
	sekilci(['yar','yər'],1,'-',"qeyri-qeti gelecek zaman")]

f_qeyriqeticase = [sekilci(['z','z'],1,'0',"qeyri qeti gelecek zaman")]

f_inkar = [sekilci(['ma','mə'],1,'0',"inkar")] #indiki ve qeyri qeti gelecek zamanda sait dushur

f_tli_tsiz = [sekilci(['dır','dir','dur','dür'],3,'0',"tesirli eden"),
	sekilci(['yış','yiş','yuş','yüş'],3,'-',"tesirsiz eden 1"),
	sekilci(['yın','yin','yun','yün'],3,'-',"tesirsiz eden 2"),
	sekilci(['yıl','yil','yul','yül'],3,'-',"tesirsiz eden 3")
]

f_mena = [sekilci(['yıl','yil','yul','yül'],3,'-',"qayidish1"),
	sekilci(['yın','yin','yun','yün'],3,'-',"qayidish2"),
	#sekilci(['n'],0,'0',"qayidish3"),
	sekilci(['yıl','yil','yul','yül'],3,'-',"mechul1"),
	sekilci(['yın','yin','yun','yün'],3,'-',"mechul2"),
	#sekilci(['n'],0,'0',"mechul3"),
	sekilci(['yış','yiş','yuş','yüş'],3,'-',"qarshiliq-birgelik"),
	sekilci(['dır','dir','dur','dür'],3,'0',"icbar1")]
	#sekilci(['t'],3,'0',"icbar2")]

f_dimish = [sekilci(['dı','di','du','dü'],3,'0',"idi hissecik"),
            sekilci(['mış','miş','muş','müş'],3, '0', "imiş hissecik")]
f_idi = [sekilci(['dı','di','du','dü'],3,'0',"idi hissecik")]
f_imish = [sekilci(['mış','miş','muş','müş'],3, '0', "imiş hissecik")]

f_sual = [sekilci(['mı','mi'],1,'0',"sual hissecik")]
f_ise = [sekilci(['sa','sə'],1,'0',"ise hissecik")]

f_sex=[sekilci(['yam','yəm'],1,'-',"1Tek"),
       sekilci(['san','sən'],1,'0',"2tek"),
       sekilci(['dı','di','du','dü'],3,'0',"3tek"),
       sekilci(['yıq','yik','yuq','yük'],3,'-',"1cem"),
       sekilci(['sınız','siniz','sunuz','sünüz'],3,'0',"2cem"),
       sekilci(['lar','lər'],1,'0',"3cem")]

f_sexcase =[sekilci(['m','m'],1,'0',"1Tek"),
           sekilci(['n','n'],1,'0',"2tek"),
           sekilci(['dı','di','du','dü'],3,'0',"3tek"),
           sekilci(['q','k','q','k'],3,'0',"1cem"),
           sekilci(['ınız','iniz','unuz','ünüz'],3,'-',"2cem"),
           sekilci(['lar','lər'],1,'0',"3cem")]


f_emr = [sekilci(['yım','yim','yum','yüm'],3,'-',"emr sekli 1ci sexs tek"),
         sekilci(['sın','sin','sun','sün'],3,'0',"emr sekli 3ci sexs tek"),
         sekilci(['yaq','yək'],1,'-',"emr sekli 1ci sexs cem"),
         sekilci(['yın','yin'],1,'-',"emr sekli 2ci sexs cem"),
         sekilci(['sınlar','sinlər','sunlar','sünlər'],3,'0',"emr sekli 3cu sexs cem")]

f_arzu =[sekilci(['ya','yə'],1,'-',"arzu sekli")]
f_vacib = [sekilci(['malı','məli'],1,'0',"vacib sekli")]
f_lazim = [sekilci(['yası','yəsi'],1,'-',"lazim sekli")]
f_sert = [sekilci(['sa','sə'],1,'0',"sert sekli")]
f_davam = [sekilci(['maqda','məkdə'],1,'0',"davam sekli")]

for fel in f_tli_tsiz:
    fel.sonra = [f_zaman, f_dimish, f_sex,f_sual]

for fel in f_inkar:
    '''    
    if fel.adi == 'inkar' and fel.adi == 'qeyri-qeti gelecek zaman':
        fel.sonra = [f_qeyriqeticase,f_sual]
        continue
    if fel.adi == 'inkar' and fel.adi == "shuhudi kecmish zaman":
        fel.sonra = [f_zaman, f_sexcase]
    '''
    fel.sonra = [f_ise,f_emr, f_arzu, f_vacib, f_lazim, f_sert, f_davam,f_zaman, f_dimish, f_sual,f_qeyriqeticase]

for fel in f_tli_tsiz:
    fel.sonra = [f_zaman, f_sex, f_sual]
for fel in f_zaman:
    if fel.adi == 'shuhudi kecmish zaman' or fel.adi == "idi hissecik":
        fel.sonra = [f_sexcase, f_sual]
        continue
    if fel.adi == 'neqli kecmish zaman' or fel.adi == 'idi hissecik':
        fel.sonra = [f_sex, f_sual]
        continue
    if fel.adi == 'shuhudi kecmish zaman' and fel.adi == '1Tek':
        fel.sonra = [f_sexcase, f_sual]

    fel.sonra = [f_dimish, f_sex,f_sual]

for fel in f_mena:
    if fel.adi == 'qayidish1' and fel.adi == '1Tek':
        fel.sonra = [f_zaman, f_sexcase, f_sual]
        continue
    if fel.adi == 'icbar1': # and fel.adi == '1Tek':
        fel.sonra = [f_zaman, f_sexcase, f_sual]

    fel.sonra = [f_zaman, f_sex, f_sual]
for fel in f_dimish:
    fel.sonra = [f_sex,f_sual]



n_feil=[f_inkar, f_mena,f_zaman, f_ise,f_emr, f_arzu, f_vacib, f_lazim, f_sert, f_davam]

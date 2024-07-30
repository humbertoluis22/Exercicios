from macaco import Macaco

macaco_1 = Macaco('Cezar',['morango'])
macaco_1.comer('banana')
macaco_1.digerir()
macaco_1.ver_bucho()

macaco_2= Macaco('Otavio',['goiaba'])
macaco_2.comer('uva')
macaco_2.comer('cereja')
macaco_2.comer(macaco_1)
macaco_2.ver_bucho()
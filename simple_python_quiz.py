
questions = [
    {
        'question': 'Asagidakilardan hansi bitkiler alemine aiddir?',
        'options': ['Ordek', 'Gobelek', 'At', 'Sam agaci'],
        'answer': 3
    },
    {
        'question': 'Bunlardan hansi saitdir',
        'options': ['b', 'a', 'r', 'd'],
        'answer': 1
    },
    {
        'question': 'En boyuk materik hansidir',
        'options': ['Antarktika', 'Avstraliya', 'Avrasiya', 'Simali Amerika'],
        'answer': 2
    },
    {
        'question': 'Azerbaycan Respublikasi ne vaxt yaranib?',
        'options': ['1928', '1918', '1500', '1930'],
        'answer': 1
    },
    {
        'question': 'Quvvetin vahidi?',
        'options': ['Newton', 'Vold', 'Watt', 'Metr'],
        'answer': 0
    },
    {
        'question': 'Asagidakilardan hansi radioaktivdir?',
        'options': ['Plutonium', 'Cive', 'Lithium', 'Cupper'],
        'answer': 0
    },
    {
        'question': 'Bextiyar Vahabzedenin ilk seiri',
        'options': ['Leyli ve Mecnun', 'Latin dili', 'Ana ve Sekil', '20 yanvar'],
        'answer': 2
    },
    {
        'question': 'sin90 nece edir?',
        'options': ['1', '2', '3', '4'],
        'answer': 0
    },
]

variants = {"A":0, "B":1, "C":2, "D":3, "E":4}

sual_count = 1
duz_cavab_count = 0


for sual in questions:
    print(str(sual_count)+'.',sual['question'])
    
    print('a)',sual['options'][0])
    print('b)',sual['options'][1])
    print('c)',sual['options'][2])
    print('d)',sual['options'][3])
    cavab = input('Cavab\n').upper()
   
    if cavab in variants:
        if cavab in variants.keys():
            if variants[cavab] == sual['answer']:
                print('Duzdur')
                duz_cavab_count +=1
            else:
                print("Cavabiniz Sehvdir.Duzgun Cavab",list(variants.items())[sual['answer']][0])
    else:
        print("Secile bilecek variantlar A,B,C,D")
        
    sual_count +=1
    print('-'*60)
print(f'Duz cavablarin sayi {duz_cavab_count} ')
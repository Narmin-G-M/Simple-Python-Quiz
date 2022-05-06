
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

question_count = 1
correct_answer = 0


for question in questions:
    print(str(question_count)+'.',question['question'])
    
    print('a)',question['options'][0])
    print('b)',question['options'][1])
    print('c)',question['options'][2])
    print('d)',question['options'][3])
    answer = input('Answer\n').upper()
   
    if answer in variants:
        if answer in variants.keys():
            if variants[answer] == question['answer']:
                print('Great!')
                correct_answer +=1
            else:
                print("Incorrect Answer.Correct Answer",list(variants.items())[question['answer']][0])
    else:
        print("You can choose only A,B,C,D")
        
    question_count +=1
    print('-'*60)
print(f'Your correct answer is {correct_answer} ')
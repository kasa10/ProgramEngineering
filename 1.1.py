import string
import nltk as nl

from nltk.corpus import stopwords




text=['Новости - Отрасли ТЭК Резиденты ТОСЭР "Озерск" '
      'инвестируют в проекты по соглашениям с "Атом-ТОР" более 400 млн рублей 09.11.21 14:50 В 2019 году компания "Интео" '
      'заключила соглашение с управляющей компанией "Атом-ТОР", чтобы реализовать на ТОСЭР "Озерск" в Челябинской области проект'
      ' по производству машин и оборудования для газо- и нефтедобывающих компаний, производителей буровзрывных работ. '
      'К настоящему времени предприятие уже вышло на полную проектную мощность. Для Александра Федотова и его предприятия '
      'эта награда стала первой. "Мы изготавливаем не только машины, но и линии, мини-заводы модульного типа по производству '
      'невзрывчатых компонентов эмульсионных взрывчатых веществ. Эмульсионные взрывчатые вещества в последние годы приобрели '
      'преимущественное развитие для проведения буровзрывных работ в карьерах и шахтах, при строительстве и разработке '
      'месторождений полезных ископаемых. Технология их производства совершенствуется, чтобы отвечать требованиям комплексной '
      'механизации и безопасности взрывных и буровзрывных работ на открытых и подземных разработках", — рассказал генеральный '
      'директор "Интео" . Все этапы производственного процесса, начиная с проектирования, ведутся силами высококлассных '
      'специалистов "Интео" . На рынок машиностроение компание "Интео" удалось выйти благодаря внедрению собственных '
      'разработок. Как пояснил Александр Федотов , изначально расчет был другим. "Сказался пандемийный год. Занимались '
      'конструкторской документацией и разрешительными документами. В прошлом году получили заказ на изготовление мини-завода '
      'по производству взрывчатых веществ. Линия проходит последние испытания, после чего отправится в город Дегтярск '
      'Свердловской области", — сказал он. Специалисты "Интео" используют новое и современное оборудование. '
      'Тот же сварочный аппарат – последней модификации. Сейчас идет сборка трех смесительно-зарядных машин. '
      'Одна на базе КАМАЗа, две – на шасси "IVECO". Отправятся на Ямал и Кузбасс соответственно. '
      'В прошлом году такая же машина была куплена одной из якутских компаний, откуда уже пришел положительный отзыв о'
      ' качестве сборки и возможностях. Более того, идут переговоры о покупке еще нескольких единиц техники. '
      'Генеральный директор АО "Атом-ТОР" Николай Пегин отметил, что производимая компанией "Интео" '
      'техника способна заменить дорогостоящие импортные аналоги. "ТОСЭР, созданные в закрытых атомных городах, создавались '
      'как инструменты для решения актуальной задачи развития этих территорий, создания новых высококвалифицированных '
      'рабочих мест. Сегодня мы видим, что наши резиденты успешно запускают производства и вносят вклад в экономику регионов". '
      'За два года "Интео" доказало высокую конкурентоспособность на рынке производства оборудования для буровзрывных работ.'
      ' Предприятие эффективно осваивает смежные рыночные ниши, такие как проектирование и изготовление штучного оборудования '
      'в соответствии с техническим заданием заказчика, ремонт и модернизацию буровой техники, техническое обслуживание машин и '
      'оборудования. Нужно отметить, что сегодня ТОСЭР "Озерск" , расположенная в Челябинской области, в целом имеет репутацию '
      'территории реализации высокотехнологичных проектов. Здесь работают шесть резидентов, которые планируют создать около 200 '
      'рабочих мест для жителей города. По соглашениям с АО "Атом-ТОР" сумма заявленных инвестиций по проектам составляет более '
      '400 млн рублей. ']

text=text[0]
print(len(text))


#НАХОЖДЕНИЕ СУБЬЕКТОВ
t2=[]
t1 = text.split('"')
for i in range(1,len(t1),2):
      if len(t1[i])<50:
            t2.append(t1[i])
t2=set(t2)

chars1 = string.punctuation + '\n\xa0«»\t—…'


text = "".join([ch for ch in text if ch not in chars1]) #удаляем знаки пунктуации



text_tokens = nl.word_tokenize(text)
len(text_tokens)

nl.download('stopwords')
rus_stopw = stopwords.words("russian")
tokens1 = [word for word in text_tokens if not word in rus_stopw]


text = nl.Text(tokens1)

chast = nl.FreqDist(text) #ЧАСТОТНОСТЬ

print('Частые слова:', chast.most_common(7))
print('Субъекты текста:', t2)


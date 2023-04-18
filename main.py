#константы
if True:
    #сколько рабочих дней всего, сколько сокращённых на час, сколько в месяце
    Д_раб=244
    Д_пр=6
    Количество_рабочих_дней_в_месяце=22
    #годовой эффективный фонд времени ЭВМ
    F_П=(Д_раб*8-Д_пр*1)
    #зарплата в месяц с ндфл, без отчислений во внебюджетные фонды
    Зарплата_тестера=30000
    Зарплата_разработчика=40000
    Зарплата_внедренца=30000
    Зарплата_сисадмина=30000
    Количество_ЭВМ_=1
    Колиечство_разработчиков=1
    Количество_внедренцев=1
    Количество_тестеров=5
    Стоимость_комплекта_ЭВМ=40000
    Стоимость_комплекта_ЭВМ_кассира=40000
    k_У=0.15#уральский коэффициент
    k_ОВФ=0.302#коэффициент отчислений во внебюджетные фонды
    k_Г=0.8#коэфициент использования
    k_М=0.02#коэффициент материальных затрат
    k_ТУН=0.01#транспортировка, установка, наладка
    Н_АВТ=0.1#коэффициент амортизации
    k_рем=0.06#коэффициент ремонта
    Ц_кВтч=6#цена за кВт/час
    Ц_бумага=300
    Ц_ручка=50
    Ц_лампочка=300
    sum_M_p=0.6#суммарная мощность одной ЭВМ(кВт)
    k_проч=0.01
    k_НР=0.05#накладные расходы
    #время разработки
    Т_РПР_всего=112
    Т_РПР_машинное=112
    Т_РПР_месяц=Т_РПР_всего/(Количество_рабочих_дней_в_месяце*8*Колиечство_разработчиков)
    #время внедрения
    Т_ВПР_всего=32
    Т_ВПР_машинное=32
    Т_ВПР_месяц=Т_ВПР_всего/(Количество_рабочих_дней_в_месяце*8*Количество_внедренцев)
    #сама операция
    N_опер_год=2
    МЗ_1=0#стоиость одной операции До
    МЗ_2=0#стоимость одной операции После
#разработка проектного решения
if True:
    #оплата труда и внебюджетные фонды
    if True:
        З_ФОТР=Зарплата_разработчика*Т_РПР_месяц*(1+k_У)
        З_ОВФ=З_ФОТР*k_ОВФ
    #ЭВМ
    if True:
        #балансовая стоимость
        С_Б=Стоимость_комплекта_ЭВМ+Стоимость_комплекта_ЭВМ*k_ТУН
        З_М=С_Б*k_М
        #сколько на заплаты
        З_ЗП=Зарплата_сисадмина*12*(1+k_У)
        #внебюджетные фонды?
        З_нач=З_ЗП*k_ОВФ
        #амортизация в год
        З_АО=С_Б*Н_АВТ
        #износ программных продуктов
        З_ИПП=0
        #ремонт за год
        З_рем=С_Б*k_рем
        #электричества за год
        З_эл=F_П*Ц_кВтч*sum_M_p
        З_сод=З_рем+З_эл
        З_проч=С_Б*k_проч
        З=З_М+З_ЗП+З_нач+З_АО+З_ИПП+З_сод+З_проч
        С_мч=З/(F_П*k_Г*1)
        З_ЭВМ=Т_РПР_машинное*k_Г*1*С_мч
    #специальные программные средства
    З_СПС=0
    #хозяйственные операционные расходы
    З_К=Ц_бумага*1+Ц_ручка*2+Ц_лампочка*1
    #накладные расходы
    Р_Н=З_ФОТР*k_НР
    К_РПР=З_ФОТР+З_ОВФ+З_ЭВМ+З_СПС+З_К+Р_Н
#внедрение проектного решения
if True:
    З_М=0
    З_КТС=108000+15000
    З_ПО=0
    З_ФОТВ=Зарплата_внедренца*Т_ВПР_месяц*(1+k_У)
    З_ОВФ=З_ФОТВ*k_ОВФ
    З_ЭВМ=Т_ВПР_машинное*k_Г*1*С_мч
    Р_ком=5500+(1000*10)+(1500*9)#проживание в гостинице
    Р_накл=З_ФОТВ*k_НР
    К_ВПР=З_М+З_КТС*(1+k_ТУН )+З_ПО+З_ФОТВ+З_ОВФ+З_ЭВМ+Р_ком+Р_накл

#эксплуатационные затраты до
if True:
    t_общ_1=295*N_опер_год
    t_общ_1_мес=t_общ_1/(Количество_рабочих_дней_в_месяце*8*Количество_тестеров)
    ЗП_1=(Зарплата_тестера*Количество_тестеров*12)/F_П *t_общ_1_мес*12*(1+k_У)
    ОТ_вн=ЗП_1*k_ОВФ
    #ЭВМ
    if True:
        #балансовая стоимость
        С_Б=Количество_тестеров*(Стоимость_комплекта_ЭВМ_кассира+Стоимость_комплекта_ЭВМ_кассира*k_ТУН)
        З_М=С_Б*k_М
        #сколько на заплаты
        З_ЗП=Зарплата_сисадмина*12*(1+k_У)
        #внебюджетные фонды?
        З_нач=З_ЗП*k_ОВФ
        #амортизация в год
        З_АО=С_Б*Н_АВТ
        #износ программных продуктов
        З_ИПП=0
        #ремонт за год
        З_рем=С_Б*k_рем
        #электричества за год
        З_эл=F_П*Ц_кВтч*sum_M_p*Количество_тестеров
        З_сод=З_рем+З_эл
        З_проч=С_Б*k_проч
        З=З_М+З_ЗП+З_нач+З_АО+З_ИПП+З_сод+З_проч
        С_мч=З/(F_П*k_Г*Количество_тестеров)
        З_ЭВМ_1=t_общ_1*k_Г*Количество_тестеров*С_мч
    НР_1=ЗП_1*k_НР
    МЗ_1*=N_опер_год
    С_1=ЗП_1+ОТ_вн+З_ЭВМ_1+МЗ_1+НР_1
#эксплуатационные затраты после
if True:
    t_общ_2=90*N_опер_год
    t_общ_2_мес=t_общ_2/(Количество_рабочих_дней_в_месяце*8*Количество_тестеров)
    ЗП_2=(Зарплата_тестера*Количество_тестеров*12)/F_П *t_общ_2_мес*12*(1+k_У)
    ОТ_вн=ЗП_2*k_ОВФ
    #ЭВМ
    if True:
        #балансовая стоимость
        С_Б=Количество_тестеров*(Стоимость_комплекта_ЭВМ_кассира+Стоимость_комплекта_ЭВМ_кассира*k_ТУН)
        З_М=С_Б*k_М
        #сколько на заплаты
        З_ЗП=Зарплата_сисадмина*12*(1+k_У)
        #внебюджетные фонды?
        З_нач=З_ЗП*k_ОВФ
        #амортизация в год
        З_АО=С_Б*Н_АВТ
        #износ программных продуктов
        З_ИПП=0
        #ремонт за год
        З_рем=С_Б*k_рем
        #электричества за год
        З_эл=F_П*Ц_кВтч*sum_M_p*Количество_тестеров
        З_сод=З_рем+З_эл
        З_проч=С_Б*k_проч
        З=З_М+З_ЗП+З_нач+З_АО+З_ИПП+З_сод+З_проч
        С_мч=З/(F_П*k_Г*Количество_тестеров)
        З_ЭВМ_2=t_общ_2*k_Г*Количество_тестеров*С_мч
    НР_2=ЗП_2*k_НР
    МЗ_2*=N_опер_год
    С_2=ЗП_2+ОТ_вн+З_ЭВМ_2+МЗ_2+НР_2
#получить все переменные
"""
vars=locals().copy()
for var in vars:
    print(var,vars[var])"""
print("_"*20)
print("К_РПР={}".format(К_РПР))
print("К_ВПР={}".format(К_ВПР))
print("С1={}".format(С_1))
print("С2={}".format(С_2))
print("Разница={}".format(С_1-С_2))
print("Затраты на разработку и внедрение={}".format(К_ВПР+К_РПР))
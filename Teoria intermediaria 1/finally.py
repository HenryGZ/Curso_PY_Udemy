#o finally é sempre executado quando declarado
#serve para fazer alguma ação mesmo que ocorra um erro ou ele não for tratado, não importa
#ele sempre será , exemplo com erro zerodivison:

try:
    print('divisão por zero, 8/0 no caso')
    8/0
    
except ZeroDivisionError:
    print('não é possivel dividir por zero')
#em python o except pode ter um else, caso ele não ocorra
else:
    print('não ocorreu erro')
finally:
    print('finally executado independendemente se o erro ocorrer ou não')

from math import hypot
catOp = float(input('Digite o valor para o cateto oposto :'))
catAd = float(input('Digite o valor para o cateto adjacente:'))
print(' A hipotenusa deste triagulo é {:.2f}'.format(hypot(catAd, catOp)))
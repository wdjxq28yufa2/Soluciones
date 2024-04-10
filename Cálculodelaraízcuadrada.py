x = 1.0
a = float(input( "Dame el valor de a:\n"))

for k in range(1, 10):
    x = (x + a/x)/2
    print ( "La raiz despues  de ", k, "iteraciones es ", x)
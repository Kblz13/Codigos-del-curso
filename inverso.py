def reverse(num):
    reverse=0
    while num >= 1:
         reverse=reverse*10+num%10
         num=num/10
    return reverse

  def invertir():
    a=int(input("Ingresar un Número: "))
    x=0
    y=(a%10==0)  #Aquí le damos el valor a la variable "y", True, o False, si el N° termina en 0.
    z=len(str(a))
    for i in range(z):
        b=a%10
        a=a//10
        x=x*10+b
    if y:
        x=str(x)
        x='0'+x
    return x
  
  def invertir():
    a=int(input("Ingresar un Número: "))
    x=0
    z=len(str(a))
    for i in range(z):
        b=a%10
        a=a//10
        x=x*10+b
    return x

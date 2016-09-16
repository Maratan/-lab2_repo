a = [2, 4, 5, 7, 10]
print("Массив имеет вид: ",a)

i = 0 					# вводим индекс
ixmin = i   		    # номер минимального элемента
minimum = a[ixmin]	    # собственно минимальный элемент
ixmax = i			    # номер максимального элемента
maximum = a[ixmax] 		# собственно максимальный элемент
razm = len(a) 			# установим размерность для среднего арифметического
summ = 0                # сумма всех элементов массива

while (i < len(a)): 
   if (a[i] < minimum): 
      ixmin = i
      minimum = a[ixmin]
   
   if (a[i] > maximum): 
      ixmax = i
      maximum = a[ixmax]
   summ = summ + a[i]
   i += 1
   
   
print ("Минимальный элемент массива = ", minimum)
print ("Максимальный элемент массива = ", maximum)
arif = summ/razm
print ("Среднее арифметическое массива =",arif)

print('\nЗадане "Словари"')

maxvoz = 18

ivan = {
  "name": "ivan",
  "age": 34,
  "children":[{
       "name": "vasja",
       "age":12,
       },
       {
       "name": "petja",
       "age": 10,
}],
}

darja={
   "name": "darja",
   "age": 41,
   "children": [{
       "name": "kirill",
       "age": 21,
   }, {
       "name": "pavel",
       "age": 15,
   }],
}

emps = [ivan, darja]
print(emps)

filtered = []  
def vozvrast(emps, maxvoz):

	for emp in emps:
		for chil in emp['children']:
			if chil['age'] >= maxvoz:
				filtered.append(emp['name'])
				break
				
	return filtered
	
print(vozvrast(emps, maxvoz))

import redis

r = redis.StrictRedis(host= '93.145.175.242', port= 63213, password='1357642rVi0', db= 0)

# inizializzo la lista delle chiavi del DB
r.keys()

# r.set('chiave, "valore')

image_name= input()
row= input()

r.set(image_name, row)
value = r.get(image_name) 
print(value)
import redis

r = redis.StrictRedis(host= '10.255.237.221', port= 6379, password='1357642rVi0', db= 0, decode_responses=True)

# inizializzo la lista delle chiavi del DB
r.keys()

a = "imagine"

for i in range (1000):
    domanda = input('Vuoi aggiungere una foto? ' )
    if domanda == 'si':
        image_name= input()
        row= input()
        r.set(image_name, row)
        value = r.get(image_name)
        r.zadd(a, {row: image_name})
        n_foto = (r.incr('count'))
        Test= True
    else:
        break

if Test == True:
    print ('Il numero di foto nel database è: ', n_foto)
    ordine = r.zrange(a, 0, -1, withscores=True)
    print('Le immagini ordinate sono:', ordine)
else:
    pass
r.flushdb()
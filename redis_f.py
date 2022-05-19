import redis

r = redis.StrictRedis(host= '93.145.175.242', port= 63213, password='1357642rVi0', db= 0, decode_responses=True)
# inizializzo la lista delle chiavi del DB
r.keys()

graziella=[]
    
giorgio=str(graziella)    

for i in range (3):
     image_name= input()
     row= input()
     r.set(image_name, row)
     value = r.get(image_name)
     graziella.append(value)
     n_foto = (r.incr('count'))
     
print(graziella)
print (n_foto)

res = r.lrange("image_name", 0, -1)

res = r.sort("image_name")
print(res)

'''''       
def cerca():
    str = input("inserisci la foto da cercare: ")
    risultato = r.sismember(giorgio,str)
    print(giorgio)

    if risultato == 1:
        print("trovato!")
    else: print("non trovato!")

cerca()
'''
r.flushdb()
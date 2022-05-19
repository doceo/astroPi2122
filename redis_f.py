import redis

r = redis.StrictRedis(host= '93.145.175.242', port= 63213, password='1357642rVi0', db= 0)

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
     r.incr('count')
     print(r.get('count'))
     

print(graziella)


def insCanc():
    
    if(r.scard(giorgio)>0):
        for i in range(r.scard(giorgio)):  # per ogni riga del file vengono eseguite le righe di codice che seguono
                r.spop(giorgio)
                print(r.scard(giorgio))

    else:
        for line in graziella:  # per ogni riga del file vengono eseguite le righe di codice che seguono
            r.sadd(giorgio, line[:-1])
            print(line[:-1])
            print(r.scard(giorgio))

        
def cerca():
    str = input("inserisci la parola da cercare: ")
    risultato = r.sismember(giorgio,str)
    print(giorgio)

    if (risultato):
        print("trovato!")
    else: print("non trovato!")

insCanc()
cerca()
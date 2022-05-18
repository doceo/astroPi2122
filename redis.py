import redis

r = redis.Redis(host= '93.145.175.242', port= 63213,password='1357642rVi0', db= 0)

r.keys()

f = open(data_file, row)

r.set(image_name, row)
line = f.readline()

value = r.get(image_name)

print(value)
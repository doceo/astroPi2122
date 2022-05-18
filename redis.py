import redis

r = redis.StrictRedis(host= "", port= "", db= 0)

r.keys()

f = open(data_file, row)

r.set(image_name, row)
line = f.readline()

value = r.get(image_name)

print(value)
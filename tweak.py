data = open('/ws3/keras_mnistcode.py','r')
content=data.read()
content=content.splitlines()
content[14]='epochs+=1'
data = open('/ws3/keras_mnistcode.py','w')
data.write('\n'.join(content))
data.close()
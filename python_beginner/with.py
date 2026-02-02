#with
#with statememnt is very helpful to simplify working
#with exception handling


filename='hello.txt'

# try:
#     file = open(filename,'r')
#     content = file.read()
# finally:
#     file.close()

#an alternate way to do this
with open(filename,'r') as file:
    content=file.read()
    print(content)

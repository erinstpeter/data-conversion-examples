#Read from name.txt
with open('name.txt') as f:
    my_name = f.read()

#Write the contents of name.txt and hello
with open('hello.txt', 'w') as f:
    f.write('hello, my name is '+ my_name+".")
    f.write('\n')

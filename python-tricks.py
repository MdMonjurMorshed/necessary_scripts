from string import Template

# using substitute 
t=Template("hello $name, this is test template")
results = t.substitute(name='bob')
print(results)

# using safe_substitute

t2 = Template("hello $name, welcome to $company")
result= t2.safe_substitute(name='mickel',company='gigalogy ltd')
print(result)
import re
text= "it rained for a week this month"
a=re.search("^it. *month$",text)


#re.findall
b=re.findall("i",text)

#re.match
x = re.search("ai", text)
print(x)



#.re.sub
x = re.sub("\s", "9", text)
print(x)
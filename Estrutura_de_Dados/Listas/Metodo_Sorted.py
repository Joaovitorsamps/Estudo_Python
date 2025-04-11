linguagens = ["Python", "js", "java", "CSharp"]

print(sorted(linguagens)) #CSharp, Python, java, js 
#Rastreamento a partir do final da lista

print(sorted(linguagens, key=lambda x: len(x))) #js, java, python, csharp

print(sorted(linguagens, key=lambda x: len(x), reverse=True)) #Pyhton, Csharp, java, js
#Rastreamento a partir do início da lista
print("enter marks obtainedin 4 subjects:")
math = int(input("math :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

sum = math+english+science+hindi
print("sum of math,english,science and hindi =",sum)

perc = (sum/400)*100

print(end="Percentage Mark =")
print(perc)
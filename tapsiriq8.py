print("----------------------------------------------")
print("tapsiriq 8 i yazammadim")
print("----------------------------------------------")


print("----------------------------------------------")
print("tapsiriq 9 u yazammadim")
print("----------------------------------------------")


print("----------------------------------------------")
print("tapsiriq 10")
print("----------------------------------------------")


soz=input("soz daxil edin: ").strip()
if soz=="":
  print("soz daxil edin hec bir soz yoxdur")
else:
  print(f"ilk herf-{soz[0]}")
  print(f"son herf-{soz[-1]}")


print("----------------------------------------------")
print("tapsiriq 11")
print("----------------------------------------------")


soz1=input("soz daxil edin: ").strip().lower()
saitler="aəeioöuüi"
sayi=0

for herf in soz:
  if herf in saitler:
    sayi+=1

print(f"sozde {sayi} sait herf var")


print("----------------------------------------------")
print("tapsiriq 12")
print("----------------------------------------------")


ededler=[1,5,8,3,10,7,14]

cutededler=[]

for eded in ededler:
  if eded%2==0:
    cutededler.append(eded)
print("Cüt ədədlər:",cutededler)


print("----------------------------------------------")
print("tapsiriq 13")
print("----------------------------------------------")


soz2=input("soz daxil edin: ").strip()
sayi1=0
for herf in soz2:
  if herf=="a" or herf=="A":
    sayi1+=1
print(f"sözdə {sayi1} eded 'a' herfi var")


print("----------------------------------------------")
print("tapsiriq 14")
print("----------------------------------------------")


ad=input("isdifadeci adinizi daxil edin: ").strip()

if len(ad)<5:
  print("isdifadeci adi qisadir")
else:
  print("ad uygundu")


print("----------------------------------------------")
print("tapsiriq 15")
print("----------------------------------------------")


secret=7
print("Ədədi tapmaqa calis")

while True:
  texmin=int(input("1 ile 10 arasinda eded daxil ele: "))

  if texmin==secret:
    print("duz tapdiz")
    break
  elif texmin<secret:
    print("biraz böyük eded daxil ele: ")
  else:
    print("biraz kiçik eded daxil ele: ")


print("----------------------------------------------")
print("tapsiriq 16 yazammadim")
print("----------------------------------------------")


print("----------------------------------------------")
print("tapsiriq 17")
print("----------------------------------------------")


soz3=input("soz daxil et: ").strip()
sayi2=soz.count("a") + soz.count("A")
print(f" sözdə {sayi} eded 'a' herfi var")


print("----------------------------------------------")
print("tapsiriq 18")
print("----------------------------------------------")


cumle=input("cumle daxil et: ")
yenicumle=cumle.replace(" ","-")

print("netice:",yenicumle)
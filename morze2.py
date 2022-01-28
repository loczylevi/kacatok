folytkov = True
# szótár:
thisdict = {
  ".-" : "a",
  ".--.-" : "á",
  "-..." : "b",
  "-.-." : "c",       
  "-.." : "d",       
  "." : "e",     
  "..-.." : "é",  
  "..-." : "f", 
  "--." : "g",
  "...." : "h",
  ".." : "i",
  ".---" : "j",
  "-.-" : "k",
  ".-.." : "l",
  "--" : "m",
  "-." : "n",
  "---" : "o",
  "---." : "ö",
  ".--." : "p",
  "--.-" : "q",
  ".-." : "r",
  "..." : "s",
  "-" : "t",
  "..-" : "u",
  "..--" : "ü",
  "...-" : "v",
  ".--" : "w",
  "-..-" : "x",
  "-..-" : "y",
  "--.." : "z",
  "--.--" : "!",
  "-.--.-" : ")",
  "-.--." : "(",
  "--..--" : ",",
  "-....-" : "-",
  ".-.-." : "+",
  ".-.-.-" : ".",
  "-..-." : "/",
  "---..." : ":",
  "..--.." : "?",
  ".-..-." : "\"",
  ".----." : "'",
}
# maga a program (ne piszkálj bele) _________________________________

while folytkov:
    bekeres = input("Kérem a lefordítandó mondatot!\t")
    if bekeres == "Grrr":
        folytkov = False
        print(">>> Program vége <<<")
        break
    bekeres = bekeres.split(" ")
    for szo in bekeres:
        print(thisdict.get(szo,"Nincs ilyen szó a szótárban!"),end=" ")
    print("")
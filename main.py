text = input("Ievadiet tekstu: ")
def deleteE (text):
  if text.count("e")>0:
   text = text.replace("e", " ")
   text = text.upper()
   print(text)
  else:
   text = "TEKST NESATUR VAJADZIGO BURTU."
  print(text)
  return text
deleteE (text)
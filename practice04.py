print("test4")
score = int ( input('score:　'))
if score < 60 and score > 0:
    print("E")
elif score >= 60 and score <= 70:
    print("D")
elif score > 70 and score < 81:
    print("C")
elif score > 80 and score < 91:
    print("B")
elif score > 90 and score < 100:
    print("A")
else:
    print("Erro")
    spec =["C","D","H","S"]
    let = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
    deck = []
    for i in spec:
        for j in let:
            deck.append(i + j)
print(deck)
cards = {   "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "10":10,
            "Jack":11,
            "Queen":12,
            "King":13,
            "Ace":14,
         }

n = 0
sum_val = 0
for i in range(6):
    card = input()
    sum_val += cards.get(card)

print(sum_val / 6)


"""
    *All data will store in list form

        [
            [x7, x8, x9],
            [x4, x5, x6],
            [x1, x2, x3]
        ]
    
    *x and o will be used in game
    

    *Let's divide into some parts 
        1-print form
        2-Win or Lose DONE
        3-data stor
"""
# Part №2 Win or Lose

def win_or_lose(table):
    #8 possible to win
    if table[0][0] == table[0][1] == table[0][2]:
        return (True, f"Winner {table[0][0]}")
    elif table[1][0] == table[1][1] == table[1][2]:
        return (True, f"Winner {table[1][0]}")
    elif table[2][0] == table[2][1] == table[2][2]:
        return (True, f"Winner {table[2][0]}")
    elif table[0][0] == table[1][0] == table[2][0]:
        return (True, f"Winner {table[0][0]}")
    elif table[0][1] == table[1][1] == table[2][1]:
        return (True, f"Winner {table[0][1]}")
    elif table[0][2] == table[1][2] == table[2][2]:
        return (True, f"Winner {table[0][2]}")
    elif table[0][0] == table[1][1] == table[2][2]:
        return (True, f"Winner {table[0][0]}")
    elif table[0][2] == table[1][1] == table[2][0]:
        return (True, f"Winner {table[0][2]}")

# Part №1 Print form
def print_form(table):
    x7 = table[0][0]
    x8 = table[0][1]
    x9 = table[0][2]
    x4 = table[1][0]
    x5 = table[1][1]
    x6 = table[1][2]
    x1 = table[2][0]
    x2 = table[2][1]
    x3 = table[2][2]
    print(f"""
     {x7} | {x8} | {x9}
     ----------
     {x4} | {x5} | {x6}
     ----------
     {x1} | {x2} | {x3}
     """)

# Part №3 Data store
data = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]
count = 0
print("""X start's the game""")
while True:
    print_form(data)
    if count == 0:
        x_turn = int(input("Number's only between 1-9: "))
        while 10 > x_turn > 0: 
            x_position = abs((x_turn-1)//3-2)
            y_position = (x_turn-1)%3
            data[x_position][y_position] = 'X'
        else:
            print("Enter Number between 1-9")
    elif count % 2 == 1:
        o_turn = int(input("Number's only between 1-9: "))



    count += 1
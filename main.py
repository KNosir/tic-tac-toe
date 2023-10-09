"""
    *All data will store in list form

        [
            [x7, x8, x9],
            [x4, x5, x6],
            [x1, x2, x3]
        ]
    
    *x and o will be used in game
    

    *Let's divide into some parts 
        1-print form DONE
        2-Win or Lose DONE
        3-playing game
"""
# Part №2 Win or Lose


def win_or_lose(table):
    # 8 possible to win
    if (
        table[0][0] == table[0][1] == table[0][2] == "X"
        or table[0][0] == table[0][1] == table[0][2] == "O"
    ):
        return str(f"Winner is {table[0][0]}")
    elif (
        table[1][0] == table[1][1] == table[1][2] == "X"
        or table[1][0] == table[1][1] == table[1][2] == "O"
    ):
        return str(f"Winner is {table[0][0]}")
    elif (
        table[2][0] == table[2][1] == table[2][2] == "X"
        or table[2][0] == table[2][1] == table[2][2] == "O"
    ):
        return fstr(f"Winner is {table[0][0]}")
    elif (
        table[0][0] == table[1][0] == table[2][0] == "X"
        or table[0][0] == table[1][0] == table[2][0] == "O"
    ):
        return str(f"Winner is {table[0][0]}")
    elif (
        table[0][1] == table[1][1] == table[2][1] == "X"
        or table[0][1] == table[1][1] == table[2][1] == "O"
    ):
        return str(f"Winner is {table[0][0]}")
    elif (
        table[0][2] == table[1][2] == table[2][2] == "X"
        or table[0][2] == table[1][2] == table[2][2] == "O"
    ):
        return str(f"Winner is {table[0][0]}")
    elif (
        table[0][0] == table[1][1] == table[2][2] == "X"
        or table[0][0] == table[1][1] == table[2][2] == "O"
    ):
        return str(f"Winner is {table[0][0]}")
    elif (
        table[0][2] == table[1][1] == table[2][0] == "X"
        or table[0][2] == table[1][1] == table[2][0] == "O"
    ):
        return str(f"Winner is {table[0][0]}")
    else:
        return False


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
    print(
        f"""
     {x7} | {x8} | {x9}
     ----------
     {x4} | {x5} | {x6}
     ----------
     {x1} | {x2} | {x3}
     """
    )


# Part №3 Data store
free_templ = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
data = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
count = 0
list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("""X start's the game""")
while True:
    print_form(data)

    if win_or_lose(data) == False:
        number = "text"
        while True:
            number = int(input())
            if number in list2:
                break
            else:
                print("Enter a valid number")
        count += 1
        try:
            list2.remove(number)
        except:
            pass
        if count % 2 == 1:
            if number < 4:
                data[2][number - 1] = "X"
            elif number < 7:
                data[1][number - 4] = "X"
            else:
                data[0][number - 7] = "X"
        else:
            if number < 4:
                data[2][number - 1] = "O"
            elif number < 7:
                data[1][number - 4] = "O"
            else:
                data[0][number - 7] = "O"

    elif count == 10:
        print("No one is winner")
        data = free_templ
        list2 = list_number
        count = 0

    else:
        print(win_or_lose(data))
        print("Start the new game")
        data = free_templ
        list2 = list_number
        count = 0

def is_winning_list(mark_list):
    types = {"X":0,"O":0,"T":0,".":0}
    for c in mark_list:
        types[c] += 1
    has_t = types["T"] == 1
    if types["X"] == 4 or (types["X"] == 3 and has_t):
        return (True, "X")
    elif types["O"] == 4 or (types["O"] == 3 and has_t):
        return (True, "O")
    #print "%d Os present in list %s" % (types["O"], str(mark_list))
    return (False,"XO")

def determine_game_status(state):
    b, unfinished = state
    lists = [b[i] for i in range(4)]
    lists.extend([[b[i][j] for i in range(4)] for j in range(4)])
    lists.append([b[i][i] for i in range(4)])
    lists.append([b[3-i][i] for i in range(4)])
    for l in lists:
        resp = is_winning_list(l)
        if resp[0]:
            return resp[1] + " won"
    if unfinished:
        return "Game has not completed"
    else:
        return "Draw"



def read_game(f):
    board = [[],[],[],[]]
    chars = ["X","O",".","T"]
    contains_dot = False
    for i in range(4):
        line = f.readline()
        for c,j in zip(line,range(4)):
            if c == ".":
                contains_dot = True
            if c in chars:
                board[i].append(c)
    return board, contains_dot

def main():
    output = []
    with open("tictac_in.txt","r") as f:
        trials = f.readline()
        for i in range(int(trials.strip())):
            state = read_game(f)
            f.readline()
            outline = "Case #%d: %s" % (i+1, determine_game_status(state))
            print outline
            output.append(outline)
    with open("tictac_out.txt","w") as f:
        f.write("\n".join(output))

if __name__ == "__main__":
    main()
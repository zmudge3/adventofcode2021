#!/usr/bin/env python3

def column_wise(row_wise_board):
    return [[el[i] for el in row_wise_board] for i in range(len(row_wise_board))]

with open("input.txt", "r") as f:
    moves = f.readline().rstrip().split(",")
    f.readline()    # Skip to first line of first board
    board_dict = {}
    boards = []
    board_num = 0
    board = []
    row = 0
    for line in f:
        line = line.strip()
        if line == "":
            boards.append(board)
            board_num += 1
            board = []
            row = 0
        else:
            nums = list(filter(lambda el: el != '',line.split(" ")))
            board.append(nums)
            for i in range(len(nums)):
                if nums[i] in board_dict:
                    board_dict[nums[i]].append((board_num,row,i))
                else:
                    board_dict[nums[i]] = [(board_num,row,i)]
            row += 1
    boards.append(board)

marked = []
for _ in range(len(boards)):
    l = []
    for _ in range(len(boards[0])):
        l.append([0]*len(boards[0]))
    marked.append(l)

remaining = [i for i in range(len(boards))]
for move in moves:
    if remaining == []:
        break
    boards_to_mark = board_dict[move]
    for board in boards_to_mark:
        board_num,row,el = board[0],board[1],board[2]
        marked[board_num][row][el] = 1
        for i in range(len(boards)):
            if (([1]*len(boards[0]) in marked[i]) or ([1]*len(boards[0]) in column_wise(marked[i]))) and i in remaining:
                remaining.remove(i)
                print(f"Board number: {i}")
                print(f"Last number called: {move}")
                print(f"Winning board: {boards[i]}")
                print(f"Marked/unmarked on winning board: {marked[i]}")
                print("\n")

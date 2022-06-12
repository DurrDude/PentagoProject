def rd652_h(self, board):
    # ---------------------------------------------------------------------------
    # Heuristic evaluation of board, presuming it is player's move.
    # Student code needed here.
    # Heuristic should not do further lookahead by calling miniMax.  This
    # function estimates the value of the board at a terminal node.
    # ---------------------------------------------------------------------------
    heuristic = 0
    secondTierList = [1, 2, 3, 4]
    firstTierList = [2, 3]
    oppositeToken = 'w' if self.token == 'b' else 'b'
    distanceList = [-1, 0, 1]
    for y in range(board.BOARD_SIZE):
        for x in range(board.BOARD_SIZE):
            if board.board[y][x] != '.':
                foundToken = board.board[y][x]
                otherToken = 'w' if foundToken == 'b' else 'b'
                for yChange in distanceList:
                    for xChange in distanceList:
                        winPossible = False
                        if (yChange != 0) or (xChange != 0):
                            try:
                                if y + yChange < 0 or x + xChange < 0:
                                    raise Exception
                                if board.board[y + yChange][x + xChange] == foundToken:
                                    startWin = -1
                                    endWin = -1
                                    winCountdown = 5
                                    winPossible = True
                                    moveMultiple = 4
                                    while winPossible and winCountdown > 0:
                                        try:
                                            if y + (moveMultiple * yChange) < 0 or x + (moveMultiple * xChange) < 0:
                                                raise Exception
                                            winPeg = board.board[y + (moveMultiple * yChange)][
                                                x + (moveMultiple * xChange)]
                                            '''print('successful winPeg = [{y}][{x}]'.format(y=y + (moveMultiple * yChange),
                                                                               x=x + (moveMultiple * xChange)))'''
                                            if winPeg != otherToken:
                                                if winCountdown == 5:
                                                    startWin = moveMultiple
                                                if winCountdown == 1:
                                                    endWin = moveMultiple
                                                winCountdown -= 1
                                                moveMultiple -= 1
                                            elif winPeg == otherToken:
                                                # print('win stopped by opponent')
                                                winPossible = False
                                        except:
                                            '''print(
                                                'unsuccessful winPeg = [{y}][{x}]'.format(y=y + (moveMultiple * yChange),
                                                                                        x=x + (moveMultiple * xChange)))'''
                                            if moveMultiple >= 0:
                                                moveMultiple -= 1
                                            else:
                                                winPossible = False
                                    if winPossible:
                                        chainMultipleList = list(range(startWin, endWin - 1, -1))
                                        chainMultipleList.remove(0)
                                        for chainMultiple in chainMultipleList:
                                            if board.board[y + (chainMultiple * yChange)][
                                                x + (chainMultiple * xChange)] == foundToken:
                                                if foundToken == self.token:
                                                    '''print('+1.5 to {color} for chain at [{yNode}][{xNode}] for original y,x: [{y}][{x}]. Completed list: {chainList}'.format(
                                                        color=self.token,
                                                        yNode=y+(chainMultiple*yChange),
                                                        xNode=x+(chainMultiple*xChange), y=y, x=x,
                                                        chainList=chainMultipleList)
                                                    )'''
                                                    heuristic += 1.5
                                                elif foundToken == oppositeToken:
                                                    '''
                                                    print(
                                                        '-1.75 to {color} for opponent chain at [{yNode}][{xNode}] for original y,x: [{y}][{x}]. Completed list: {chainList}'.format(
                                                            color=self.token,
                                                            yNode=y + (chainMultiple * yChange),
                                                            xNode=x + (chainMultiple * xChange), y=y, x=x,
                                                            chainList=chainMultipleList)
                                                    )'''
                                                    heuristic -= 1.75
                            except:
                                pass
                                # print('unsuccessful link [{y}][{x}]'.format(y=y+yChange,x=x+xChange))
            if y in secondTierList and x in secondTierList:
                if board.board[y][x] == self.token:
                    # print('+1 to {color} for secondTier'.format(color=self.token))
                    heuristic += 1
                elif board.board[y][x] == oppositeToken:
                    # print('-1 to {color} for opponent secondTier'.format(color=self.token))
                    heuristic -= 1
            if y in firstTierList and x in firstTierList:
                if board.board[y][x] == self.token:
                    # print('+1 to {color} for firstTier'.format(color=self.token))
                    heuristic += 1
                elif board.board[y][x] == oppositeToken:
                    # print('-1 to {color} for opponent firstTier'.format(color=self.token))
                    heuristic -= 1
    return heuristic
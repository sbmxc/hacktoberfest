def checkLowercase(inStr):
    charLCState = []
    for charVal in inStr:
        charLCState.append(charVal.islower())
    return charLCState.count(True) == len(inStr)

inGrammer = input('Enter Grammer :: ')
cfgSplit = inGrammer.replace(' ', '').split('->')
cfgProds = cfgSplit[1].split('|')
newSymbol, lrList, terminalStates, nonTerminalStates = f'{cfgSplit[0]}\'', [], [], []
if len(cfgProds) >= 2:
    for i in cfgProds:
        if len(i) != 1:
            if i.startswith(cfgSplit[0]):
                nonTerminalStates.append(f'{i}')
            else:
                if checkLowercase(i):
                    terminalStates.append(f'{i}{newSymbol}')
            lrList.append(i.startswith(cfgSplit[0]))
        else:
            terminalStates.append(f'{i}{newSymbol}')
else:
    lrList.append(False)

if True in lrList:
    newSymbolProductions = []
    for i in nonTerminalStates:
        newSymbolProductions.append(f'{i[1:]}{newSymbol}')
    newSymbolProductions.append('ε')
    print(f'\nAfter eliminating left recursion:')
    print(f'{cfgSplit[0]} -> {" | ".join(terminalStates)}')
    print(f'{newSymbol} -> {" | ".join(newSymbolProductions)}')
else:
    print(f'\n{inGrammer} Is Not Left Recursive.')

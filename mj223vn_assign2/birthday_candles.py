YEARS_TO_LIVE = 100
NEW_CANDLE_BOX = 24
candleInBox = 0
numOfBoxes = 0
totalNumOfBoxes = 0

for year in range(1,YEARS_TO_LIVE + 1):
    if candleInBox < year:
        while candleInBox < year:
            candleInBox += NEW_CANDLE_BOX
            numOfBoxes += 1
        print(f"Before birthday {year}, buy {numOfBoxes} box(es)")
        totalNumOfBoxes += numOfBoxes
        numOfBoxes = 0
    candleInBox -= year
print(f"\nTotal number of boxes: {totalNumOfBoxes}, Remaining candles: {candleInBox}")

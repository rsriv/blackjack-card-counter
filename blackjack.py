import random

#blackjack card counting simulation
#dealer is indexed numPlayers-1
#player is indexed 0
def getMax(A, n):
    index = 0
    while(n>=A[index]  and index<10):
        index+=1;
    return index
numGames = 0
betUnit = 10
minBet = 10
pocket = 500
numDecks = 6
cards = [None]*10
numCards = 0
for i in range(0,9):
    cards[i] = 4*numDecks
    numCards+=cards[i]
cards[9] = 16*numDecks
numCards+=cards[9] 
numPlayers = int(raw_input("Number of Players: "))
numPlayers+=1;
score = [None]*numPlayers
for l in range(0,numPlayers):
    score[l] = 0
dist = [None]*10
numten = 0
runCount = 0
trueCount = 0
while(numCards>numPlayers*2 + numPlayers):
    numGames += 1
    #initialize scores
    for l in range(0,numPlayers):
        score[l] = 0
    bet = trueCount-betUnit
    if bet<minBet:
        bet = minBet
    pocket -= bet
    #initial deal
    for j in range(0,2):
        for k in range(0,numPlayers):
            #draw card
            #1. develop distribution
            sum = 0;
            for i in range(0,10):
                dist[i] = sum+float(cards[i])/float(numCards)
                sum=dist[i]
                #print sum
            #2. get card
            card = random.uniform(0,1)
            numCards-=1
            card = getMax(dist,card) + 1
            cards[card-1] -=1
            score[k] += card
            
            if k == numPlayers-1 and j == 1:
                #don't count
                dealerCard = card
            else:
                if card>1 and card<7:
                    runCount +=1
                elif card == 10 or card == 1:
                    runCount -=1

            trueCount = runCount/numCards/(52)
    for k in range(0,numPlayers):
        if(k==0):#is player
            done = False
            while done==False:
                if score[0]<12 or (score[0]<17 and dealerCard>6):
                    #hit
                    #draw card
                    #1. develop distribution
                    sum = 0;
                    for i in range(0,10):
                        dist[i] = sum+float(cards[i])/float(numCards)
                        sum=dist[i]
                        #print sum
                    #2. get card
                    card = random.uniform(0,1)
                    numCards-=1
                    card = getMax(dist,card) + 1
                    cards[card-1] -=1
                    score[k] += card
                    if card>1 and card<7:
                        runCount +=1
                    elif card == 10 or card == 1:
                        runCount -=1
   
                else:
                    done = True
                trueCount = runCount/numCards/52
                
                
        else:#not player
            while(score[k]<17):
                #hit
                #draw card
                #1. develop distribution
                sum = 0;
                for i in range(0,10):
                    dist[i] = sum+float(cards[i])/float(numCards)
                    sum=dist[i]
                    #print sum
                #2. get card
                card = random.uniform(0,1)
                numCards-=1
                card = getMax(dist,card) + 1
                cards[card-1] -=1
                score[k] += card
                if card>1 and card<7:
                    runCount +=1
                elif card == 10 or card == 1:
                    runCount -=1
            decks = float(numCards)/52.0
            trueCount = int(runCount/decks)
    if score[0]>score[numPlayers-1] and score[0]<=21 and score[numPlayers-1]<=21 or score[numPlayers-1]>21 and score[0]<=21:
        #player win
        pocket+=2*bet
        print "WIN: ",2*bet,"Dealer: ",score[numPlayers-1],"Me: ",score[0]
    elif score[0] == score[numPlayers-1] and score[0]<=21 and score[numPlayers-1]<=21:
        pocket+=bet
        print "Push: ",bet,"Dealer: ",score[numPlayers-1],"Me: ",score[0]
    else:
        print "LOSE: ",bet,"Dealer: ",score[numPlayers-1],"Me: ",score[0]
    print runCount,trueCount
print pocket, "after ", numGames,"rounds"

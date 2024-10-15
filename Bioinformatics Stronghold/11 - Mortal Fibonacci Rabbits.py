def mFibRabbits(months, lifespan):
    RabbitsBorn = [1]
    AdultRabbitsAlive = [0]
    RabbitsAlive = []
    for i in range(months):
        if i > 0:
            #Rabbits Grow Up
            AdultRabbitsAlive.append(RabbitsBorn[i-1] + AdultRabbitsAlive[i-1])
            #Babies are born
            RabbitsBorn.append(AdultRabbitsAlive[i-1])
            #Rabbits die of old age
            if i >= (lifespan):
                AdultRabbitsAlive[i] -= RabbitsBorn[i-lifespan]
        #Count Rabbits
        RabbitsAlive.append(RabbitsBorn[i] + AdultRabbitsAlive[i])
        print(RabbitsAlive[i])

mFibRabbits(93, 18)
# Pseudocode for Homework Four
# Emily Heffernan

# In this experiment, participants will have to categorize flowers. These flowers will have different colours, inner and outer petal shapes, and inner
# and outer circle colours. Participants will categorize the flowers as "likes sun" or "likes shade" and will receive feedback on their response.
# The flowers follow a "rule plus exception" categorization structure.
# There are eight possible flower stimuli. Anchors will be presented two times more than non-anchor stimuli, and exceptions will not be introduced until
# the 2nd block, unless participants are in the "early exceptions" condition. Participants will receive one break halfway through the experiment.
# Each block will contain 24 trials, and there will be six blocks.

# I broke down my psuedo code into a bunch of pseudo functions (sorry if this is confusing!)
# I've provided brief descriptions for less clear functions

def displayCrossHair(time):
    display(crossHairImage)
    delay(time)
    clearScreen()

def getResponse():
    while(key != pressed):
        sample(key)
    return(key, reactionTime)

def createList(numProto, numExceptions):
    # create a list with the specific number of exceptions and prototypes for that trial
    # alternatively, subjects will all follow the exact same item order
    # this needs some fleshing out still
    return stimList

def getRule(): # Asks the participant to describe their strategy after they've finished all six trial blocks
    rule = response
    return(rule)

def saveData(stimulus, response, correct, reactionTime):
    #writes the data from each trial to a global data frame variable that will be saved as a csv file.
    return

def trial(image, category, response):
    displayCrossHair(2000)
    display(image)
    response, reactionTime = getResponse()
    if response == category:
        correct = 1
    else:
        correct = 0
    saveData(stimulus, response, correct, reactionTime)
    return
    
def block(numProto, numExceptions):
    stimulusList = createList(numProto, numExceptions)
    for stimulus in stimulusList:
        trial(stimulus.image, stimulus.category, stimulus.response)
    return

def takeBreak():
    display(breakMessage)
    while(spaceBar != pressed):
        sample(spaceBar)

def subject(earlyExceptions):
    # Get subject information
    getSubjectData()

    # Display experiment instructions
    instructionsImage = read(path)

    while(spaceBar != pressed):
        display(instructionsImage)
        sample(spaceBar)

    #block one
    if(earlyExceptions == True):
        block(12, 4)
    else:
        block(12, 0)
    
    # block two
    block(12,4) 

    # block three
    block(12, -1) #-1 yields random number of exceptions

    takeBreak()

    #blocks four through six:
    for num in range(3):
        block(12, -1)

    getRule() #asks the participant to enter their categorization rule

    #export all data as .csv

    # Finished!
    display(doneMessage)

    return



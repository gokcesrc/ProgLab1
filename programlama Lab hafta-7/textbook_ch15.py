#!/usr/bin/env python
# coding: utf-8

# In[69]:


import random


# In[70]:


def rollDie():
    """Returns a random int between 2 and 6"""
    return random.choice([1,2,3,4,5,6])


# In[71]:


def rollN(n):
    result = ''
    for i in range(n):
        result=result + str(rollDie())
    print(result)


# In[72]:


rollN(5)


# In[73]:


def flip(numFlips):
    """Assumes numFlips a positive int"""
    heads=0
    for i in range(numFlips):
        if random.choice(('H','T'))=='H':
            heads+=1
    return heads/numFlips


# In[74]:


flip(1)


# In[75]:


def flipSim(numFlipsPerTrial,numTrials):
    """Assumes numFlipsPerTrial and numTrials(Kaç deney?) positive ints"""
    fracHeads=[]
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean=sum(fracHeads)/len(fracHeads)
    return mean


# In[76]:


flipSim(1000,1000)


# In[77]:


import pylab


# In[78]:


def regressToMean(numFlips,numTrials):
    #Get fraction of heads for each trial of numFlips
    fracHeads=[]
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))
    #Find trials with extreme results and for each the next trial
    extremes,nextTrials=[], []
    for i in range(len(fracHeads)-1):
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i+1])
    #Plot results
    pylab.plot(range(len(extremes)), extremes, 'ko',label='Extreme')
    pylab.plot(range(len(nextTrials)),nextTrials,'k^',label='Next Trial')
    pylab.axhline(0.5)
    pylab.ylim(0,1)
    pylab.xlim(-1,len(extremes)+1)
    pylab.xlabel('Extreme Example and Next Trial')
    pylab.ylabel('Fractions Heads')
    pylab.title('Regression to the Mean')
    pylab.legend(loc='best')


# In[79]:


regressToMean(15,40)


# In[80]:


def flipPlot(minExp,maxExp):
    """Assumes minExp and maxExp positive integers; minExp>max
       Plots results of 2**minExp to 2**maxExp coin flips"""
    ratios, diffs,xAxis = [],[],[]
    #xAxis=Kaç deney yapıldığını yatay sutundaki değerleri gösterir.
    for exp in range(minExp,maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads=0
        for n in range(numFlips): #Kaç  defa deney yapılacagını söyler
            if random.choice(('H','T')) == 'H':
                numHeads += 1
        numTails = numFlips-numHeads
        try:
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads - numTails))
        except ZeroDivisionError:
            continue
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis,diffs,'k')
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads - #Tails')
    pylab.plot(xAxis,ratios,'k')


# In[81]:


random.seed(0)
flipPlot(4,20)


# In[82]:


def variance(X):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X"""
    mean=sum(X)/len(X)
    tot=0.0
    for x in X:
        tot += (x-mean)**2
    return tot/len(X)

def stdDev(X):
    """Assumes that X is a list of numbers.
    Returns the standard deviation of X"""
    return variance(X)**0.5


# In[83]:


def makePlot(xVals,yVals,title,xLabel,yLabel,style,logX=False,logY=False):
    pylab.figure()
    pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.plot(xVals,yVals,style)
    if logX:
        pylab.semilogx()
    if logY:
        pylab.semilogy()


# In[84]:


def runTrial(numFlips):
    numHeads=0
    for n in range(numFlips):
        if random.choice(('H','T'))== 'H':
            numHeads +=1
    numTails=numFlips-numHeads
    return(numHeads,numTails)
            


# In[89]:


def flipPlot1(minExp,maxExp,numTrials):
    """Assumes minExp,maxExp,numTrials ints > 0; minExp < maxExp
    Plots summaries of results of numTrials of 2**minExp to 2**maxExp coin flips"""
    ratiosMeans,diffsMeans,ratiosSDs,diffsSDs=[],[],[],[]
    xAxis=[]
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios,diffs=[],[]
        for t in range(numTrials):
            numHeads,numTails = runTrial(numFlips)
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads-numTails))
        ratiosMeans.append(sum(ratios)/numTrials)
        diffsMeans.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
    numTrialsString= ' ('+ str(numTrials)+' Trials)'
    title= 'Mean Heads/Tails Ratios ' + numTrialsString
    makePlot(xAxis,ratiosMeans,title,'Number of flips',
            'Mean Heads/Tails','ko',logX=True)
    title='SD Heads/Tails Ratios'+numTrialsString
    makePlot(xAxis,ratiosSDs,title,'Number of Flips',
            'Standard Deviation','ko',logX=True,logY=True)


# In[90]:


flipPlot1(4,10,5)


# In[ ]:





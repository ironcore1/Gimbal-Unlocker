#Jonny Robinson - Name ideas: Gimbal Unlocker, Euler Can Get FUuuuuucked, Gimlock

import pymel.core as pm

#get the selection
controllerSelected = pm.ls(selection = 1)[0]

#check what the current rotation order 
CurrentRotationOrder = controllerSelected.getRotationOrder()

print(' --- The current rotation order is ' + str(CurrentRotationOrder) + ' --- ')

#All values of each rotation are going to be store in the dictonary
rotationFrameValue = {'X': [],'Y': [], 'Z': []}

#Frame Range set by animator
frameRangeMin = pm.playbackOptions(query=True,minTime=True)
frameRangeMax = pm.playbackOptions(query=True,maxTime=True)


#Get grab all the frame numbers which have been keyed 
rotXFrames = pm.keyframe(controllerSelected.rotateX, q=True)
rotYFrames = pm.keyframe(controllerSelected.rotateY, q=True)
rotZFrames = pm.keyframe(controllerSelected.rotateZ, q=True)

rotXFramesValue = []
rotYFramesValue = []
rotZFramesValue = []

#get the attribute value of a set frame and store them in a list
for rotXFrame in rotXFrames:
    rotXAttribute = pm.getAttr(controllerSelected.rotateX, time= rotXFrame)
    rotXFramesValue.append(rotXAttribute)

for rotYFrame in rotYFrames:
    rotYAttribute = pm.getAttr(controllerSelected.rotateY, time= rotYFrame)
    rotYFramesValue.append(rotYAttribute)

for rotZFrame in rotZFrames:
    rotZAttribute = pm.getAttr(controllerSelected.rotateZ, time= rotZFrame)
    rotZFramesValue.append(rotZAttribute)

rotationFrameValue['X'] = zip(rotXFrames, rotXFramesValue)
rotationFrameValue['Y'] = zip(rotYFrames, rotYFramesValue)
rotationFrameValue['Z'] = zip(rotZFrames, rotZFramesValue)

def highestFrameVal(rotDictKeyVal):
    
    #You need to pass it the dict key name
    
    #compair all the frame values by their absolute value and the highest value is what we need
    firstValue = 0
    frameNumber = None

    #check the frame Attribute value and get the biggest number by absolute value
    for frameNum, attributeValue in rotationFrameValue.get(rotDictKeyVal):
        
        # -----Print below if you want to debug--------
        #print (frameNum, abs(attributeValue))
        
        if abs(attributeValue) > firstValue:
            
            firstValue = abs(attributeValue)
            frameNumber = frameNum
            
    print('For ' + rotDictKeyVal + ' the highest value is ' + str(firstValue) + ' on frame ' + str(frameNumber))
    
    return firstValue


#this dict now has the highest values from the controller

#----
rotationsWithHighestValues = {}

for rotations in rotationFrameValue.keys():
    
    rotationsWithHighestValues[rotations] = highestFrameVal(rotations)
    

#this will look at the key's value and order it by value    
rotationValueOrder = sorted(rotationsWithHighestValues.items(), key=lambda x: x[1])

#this will now reorder the rotations so they match what I want
rotationValueOrder[0], rotationValueOrder[1] = rotationValueOrder[1], rotationValueOrder[0]

print(rotationValueOrder)

theOrderInAList = []
for rota, vala in rotationValueOrder:

    theOrderInAList.append(rota)

theOrder = ''.join(theOrderInAList)

#Set the rotation order
print('I would recommend this Rotation Order for your animation ' + theOrder)

controllerSelected.setRotationOrder(theOrder, True)
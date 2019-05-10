import math 
import pygame
import time
import random
import concretegame
# steering behavior
# why this wont work bruh
position = None
orientation= None
velocity= None
rotation= None
def update(steering, maxSpeed, time):
    position += velocity * time
    orientation += rotation * time
    velocity += steering.linear * time
    orientation += steering.angular * time
    if velocity.length() > maxSpeed:
        velocity.normalize()
        velocity *= maxSpeed

class Seek:
    def __init__(self):
        self.character= None
        self.target= None
        self.maxAcceleration= None
    def getSteering(self):
        steering = steeringOutput()
        steering.linear = target.position - character.position
        steering.linear.normalize()
        steering.linear *= maxAcceleration
        steering.angular = 0
        return steering

class Arrive:
    def __init__(self):
        self.character= None
        self.maxAcceleration= None
        self.maxSpeed= None
        self.targetRadius= None
        self.slowRadius= None
    timeToTarget = 0.1
    steering = steeringOutput()
    direction = target.position - character.position
    distance = direction.length()
    if distance < targetRadius:
        return None 
    if distance > slowRadius:
        targetSpeed = maxSpeed
    else:
        targetSpeed = maxSpeed * distance / slowRadius
        targetVelocity = direction
        targetVelocity.normalize()
        targetVelocity *= targetSpeed
        steering.linear = targetVelocity - character.velocity
        steering.linear /= timeToTarget
        if steering.linear.length() > maxAcceleration:
            steering.linear.normalize()
            steering.linear *= maxAcceleration
        steering.angular = 0
        return steering

class Align:
    def __init__ (self):
        self.character= None
        self.target= None
        self.maxAngularAcceleration= None
        self.maxRotation= None
        self.targetRadius= None
        self.slowRadius= None
    timeToTarget = 0.1
    def getSteering(target):
        steering = steeringOutput()
        rotation = target.orientation - character.orientation
        rotation = mapToRange(rotation)
        rotationSize = abs(rotationDirection)
        if rotationSize < targetRadius:
            return None
        if rotationSize > slowRadius:
            targetRotation = maxRotation
        else:
            targetRotation = maxRotation * rotationSize / slowRadius
            targetRotation *= rotation / rotationSize
            steering.angular = targetRotation - character.rotation
            steering.angular /= timeToTarget
            if maxAngularAcceleration is abs(steering.angular):
                steering.angular /= maxAngularAcceleration
                steering.angular *= maxAngularAcceleration
        steering.linear = 0
        return steering

class VelocityMatch:
    def __init__(self):
        self.character= None
        self.target= None
        self.maxAcceleration= None
    def getSteering(target):
        steering = steeringOutput()
        steering.linear = (target.velocity - character.velocity) / timeToTarget
        if steering.linear.normalize():
            steering.linear *= maxAcceleration
    steering.angular = 0
    return steering

class Pursue (Seek):
    def __init__(self):
        self.maxPrediction= None
        self.target= None
    def getSteering():
        direction = target.position = character.position
        distance = direction.length()
        speed = character.velocity.length()
        if speed <= distance / maxPrediction:
            prediction = maxPrediction
        else:
            prediction = distance / speed
            Seek.target = explicitTarget
            Seek.target.position += target.velocity * prediction
            return Seek.getSteering()

class Face (Align):
    def __init__ (self):
        self.target= None
    def getSteering():
        direction = target.position - character.position
        if direction.length() == 0:
            return target 
        Align.target = explicitTarget
        Align.target.orientation = atan2(-direction.x, direction.z)
        return Align.getSteering()

class LookWhereYourGoing (Align):
    def getSteering():
        if character.velocity.length() == 0:
            return target.orientation == atan2(character.velocity.x, character.velocity.z)
            return Align.getSteering()

class Wander (Face):
    def __init__ (self):
        self.wanderOffset = None
        self.wanderRate= None
        self.wanderOrientation= None
        self.maxAcceleration= None
    def getSteering():
        wanderOrientation += (random(0.1) - random(0.1)) * wanderRate
        targetOrientation = wanderOrientation + character.orientation
        target = character.position + wanderOffset * character.orientation.asVector()
        target += wanderRadius * targetOrientation.asVector()
        steering = Face.getSteering()
        steering.linear = maxAcceleration * character.orientation.asVector()
        return steering

class FollowPath (Seek):
    def __init__(self):
        self.path = None
        self.pathOffset = None
        self.currentParam= None
    predictTime = 0.1
    def getSteering():
        futurePos = character.position + character.velocity * predictTime
        currentParam = path.getParam(futurePos, currentPos)
        targetParam = currentParam + pathOffset
        target.position = path.getPosition(targetParam)
        return Seek.getSteering()

# linear 
strength = maxAcceleration * (threshold - distance) / threshold
# inverse square
strength = min(decayCoefficient / (distance * distance), maxAcceleration)

class Separation:
    def __init__ (self):
        self.character= None
        self.targets= None
        self.threshold= None
        self.decayCoefficient= None
        self.maxAcceleration= None
    def getSteering():
        steering = steering
        for target in targets:
            direction = target.position - character.position
            distance = direction.length()
            if distance < threshold:
                strength = min(decayCoefficient / (distance * distance), maxAcceleration)
                direction.normalize()
                steering.linear += strength * direction
            return steering

class CollisionAvoidance:
    def __init__ (self):
        self.character= None 
        self.targets= None
        self.maxAcceleration= None
        self.radius = None # collision threshold
    def getSteering(self):
        shortestTime = infinity
        firstTarget = None # target that will collide first
        firstMinSeparation= None 
        firstDistance= None
        firstRelativePos= None
        firstRelativeVel= None
        for target in self.targets:
            relativePos = target.position − self.character.position
            relativeVel = target.velocity − self.character.velocity
            relativeSpeed = relativeVel.length()
            timeToCollision = (relativePos * relativeVel) / (relativeSpeed * relativeSpeed)
            distance = relativePos.length()
            minSeparation = distance − relativeSpeed * shortestTime
            if minSeparation > 2 * radius: 
                continue
            if timeToCollision > 0 and timeToCollision < shortestTime:
                shortestTime = timeToCollision
                firstTarget = target
                firstMinSeparation = minSeparation
                firstDistance = distance
                firstRelativePos = relativePos
                firstRelativeVel = relativeVel
            if not firstTarget: 
                return None
            if firstMinSeparation <= 0 or distance < 2 * radius: # colliding
                relativePos = firstTarget.position − character.position
            else:
                relativePos = firstRelativePos + firstRelativeVel * shortestTime
                relativePos.normalize()
            steering.linear = relativePos * maxAcceleration
            return steering

class ObstacleAvoidance(Seek):
    def __init__(self):
        self.collisionDetector= None
        self.avoidDistance= None
        self.lookahead= None
# ... Other data from superclass ...
    def getSteering(self):
        rayVector = character.velocity
        rayVector.normalize()
        rayVector *= lookahead
        collision = collisionDetector.getCollision(character.position, rayVector)
        if not collision: 
            return None
            target = collision.position + collision.normal * avoidDistance
            return Seek.getSteering()
            
'''EXAMPLE MAIN'''
from concretegame import ConcreteGame

def main():
    '''main execution func'''
    game = ConcreteGame("Concrete Game")
    # make gameobjects to participate in game
    game.run()

if __name__ == "__main__":
    main()
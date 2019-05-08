import math 
import pygame
import time
from Vec2D import vec
import random


position
orientation
velocity
rotation
def update(steering, maxSpeed, time):
    position += velocity * time
    orientation += rotation * time
    velocity += steering.linear * time
    orientation += steering.angular * time
    if velocity.length() > maxSpeed:
        velocity.normalize()
        velocity *= maxSpeed

class Seek:
    character
    target
    maxAcceleration
    def getSteering():
        steering = new steeringOutput()
        steering.linear = target.position - character.position
        steering.linear.normalize()
        steering.linear *= maxAcceleration
    steering.angular = 0
    return steering

class Arrive:
    character
    maxAcceleration
    maxSpeed
    targetRadius
    slowRadius
    timeToTarget = 0.1
    steering = new steeringOutput()
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
        steering linear /= timeToTarget
        if steering.linear.length() > maxAcceleration:
            steering.linear.normalize()
            steering.linear *= maxAcceleration
        steering.angular = 0
        return steering

class Align:
    character
    target
    maxAngularAcceleration
    maxRotation
    targetRadius
    slowRadius
    timeToTarget = 0.1
    def getSteering(target):
        steering = new steeringOutput()
        rotation = target.orientation - character.orientation
        rotation = mapToRange(rotation)
        rotationSize = abs(roationDirection)
        if rotationSize < targetRadius:
            return None
        if rotationSize > slowRadius:
            targetRotation maxRotation
        else:
            targetRotation = maxRotation * rotationSize / slowRadius
            targetRotation *= rotation / rotationSize
            steering.angular = targetRotation - character.rotation
            steering.angular /= timeToTarget
            if angularAcceleration = abs(steering.angular):
            steering.angular /= angularAcceleration
            steering.angular *= maxAngularAcceleration
        steering.linear = 0
        return steering

class VelocityMatch:
    character
    target
    maxAcceleration
    def getSteering(target):
        steering = new steeringOutput()
        steering.linear = (target.velocity - character.velocity) / timeToTarget
        if steering.linear.normalize()
        steering.linear *= maxAcceleration
    steering.angular = 0
    return steering

class Pursue (Seek):
    maxPrediction
    target
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
    target
    def getSteering:
        direction = target.position - character.position
        if direction.length() == 0:
            return target 
        Align.target = explicitTarget
        Align.target.orientation = atan2(-direction.x, direction.z)
        return Align.getSteering()

class LookWhereYourGoing (Align):
    def getSteering():
        if character.velocity.length() == 0:
            return target.orientation = atan2(=character.velocity.x, character.velocity.z)
            return Align.getSteering()

class Wander (Face):
    wanderOffset 
    wanderRate
    wanderOrientation
    maxAcceleration
    def getSteering():
        wanderOrientation += (random(0.1) - random(0.1)) * wanderRate
        targetOrientation = wanderOrientation + character.orientation
        target = character.position + wanderOffset * character.orientation.asVector()
        target += wanderRadius * targetOrientation.asVector()
        steering = Face.getSteering()
        steering.linear = maxAcceleration * character.orientation.asVector()
        return steering

class FollowPath (Seek):
    path 
    pathOffset 
    currentParam
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
    character
    targets
    threshold
    decayCoefficient
    maxAcceleration
    def getSteering():
        steering = new steering
        for target in targets:
            direction = target.position - character.position
            distance = direction.length()
            if distance < threshold:
                strength = min(decayCoefficient / (distance * distance), maxAcceleration)
                direction.normalize()
                steering.linear += strength * direction
            return steering
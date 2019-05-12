import math
import pygame
import time
import random
import concretegame
# steering behavior
# why this wont work bruh
# teacher say
# start over... make free functions for the desired behaviours
# agent class calls those functions to update its velocity
class GameObject:
    '''this should draw the guy'''
    def __init__(self, position, orientation, velocity, rotation, steering):
        self.position = position
        self.orientation = orientation
        self.velocity = velocity
        self.rotation = rotation
        self.steering = steering

    def update(self, steering, maxSpeed, time, dt):
        self.position += self.velocity * time
        self.orientation += self.rotation * time
        self.velocity += steering.linear * time
        self.orientation += steering.angular * time
        if self.velocity.length() > maxSpeed:
            self.velocity.normalize()
            self.velocity *= maxSpeed
        if self.target is None:            
            return        
            distance = self.target - Vector2(self.x, self.y)        
            steering = distance * self.speed - self.velocity        
            steering = truncate(steering, self.max_force)        
            self.velocity = truncate(self.velocity + steering, self.max_velocity)        
            self.position += self.velocity * dt

'''these are the functions to use for the guy'''
def seek(myposition, destination, speed):
    self.myposition = (x, y)
    self.destination = None
    self.speed = 2
    return (destination - myposition).normalized

def wander(velocity, circle_radius, circle_distance, angle_change):
   self.velocity = Vector2(0, 0)
   self.circle_distance = 50
   self.circle_radius = 10
   self.angle_change = math.pi / 4
   return (velocity - angle_change).normalized

def arrive(velocity, slow_radius, position):
    self.velocity = Vector2(0, 0)
    self.slow_radius = 200
    self.position = (x, y)
    return (velocity - slow_radius).normalized

def pursuit(max_force, future_position, truncate):
    if self.target is None:            
        return        
        pos = self.target.position        
        future_pos = pos + self.target.velocity * 1       
        distance = future_pos - eu.Vector2(self.x, self.y)        
        steering = distance * self.speed - self.velocity        
        steering = truncate(steering, self.max_force)        
        self.velocity = truncate(self.velocity + steering, self.max_velocity)        
        self.position += self.velocity * dt

def evade(max_force, future_position, truncate, actor):
    self.target = ps.Sun()        
    self.target.position = (40, 40)        
    self.target.start_color = ps.Color(0.2, 0.7, 0.7, 1.0)        
    self.target.velocity = Vector2(50, 0)        
    self.add(self.target)        
    self.actor = Actor(320, 240)        
    self.actor.target = self.target        
    self.add(self.actor)        
    self.schedule(self.update)

def flee(desired_velocity, max_velocity, target, speed):




class TheAgent:
    '''this is the guy that uses the functions'''
    def __init__(self):
        self.position = pygame.Vector2(0,0)
        self.velocity = pygame.Vector2(1,0)
        self.target = pygame.Vector2(100, 100)
    def update(self):
        self.velocity += seek(self.position, self.target) 
        self.position = self.position + self.velocity

#'''EXAMPLE MAIN'''
#def main():
 #   '''main execution func'''
 #   game = ConcreteGame("Concrete Game")
    # make gameobjects to participate in game
 #   game.run()


#if __name__ == "__main__":
#    main()

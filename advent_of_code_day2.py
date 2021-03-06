import pandas as pd

path = 'day2.csv'
with open(path, 'r') as f:
    data = [i for i in f.read().splitlines()]

def p1(data):    
    position = {        
        'forward': 0,        
        'depth': 0    
    }    
    for move in data:
        direction, distance = move.split(' ')        
        distance = int(distance)        
        match direction:            
            case 'forward':                
                position['forward'] += distance            
            case 'up':                      
                position['depth'] -= distance            
            case 'down':                
                position['depth'] += distance        
    
    return position['forward'] * position['depth']

print(p1(data))

def p2(data):
    position = {
        'aim': 0,
        'forward': 0,
        'depth': 0
    }

    for move in data:
        direction, value = move.split(' ')
        value = int(value)
        match direction:
            case 'forward':
                position['forward'] += value
                position['depth'] += position['aim'] * value
            case 'up':
                position['aim'] -= value
            case 'down':
                position['aim'] += value
    return position['forward'] * position['depth']

print(p2(data))


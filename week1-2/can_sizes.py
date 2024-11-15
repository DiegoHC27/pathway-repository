import math 

pi = math.pi 

def main(): 
    # List of the values for radius, height, and name of the twelve 
    # can sizes to be able to iterate through its values 
    cans = [ 
        (6.83, 10.16, '#1 Picnic', 0.28), 
        (7.78, 11.91, '#1 Tall', 0.43), 
        (8.73, 11.59, '#2', 0.45), 
        (10.32, 11.91, '#2.5', 0.61), 
        (10.79, 17.78, '#3 Cylinder', 0.86), 
        (13.02, 14.29, '#5', 0.83), 
        (5.40, 8.89, '#6Z', 0.22), 
        (6.83, 7.62, '#8Z short', 0.26), 
        (15.72, 17.78, '#10', 1.53), 
        (6.83, 12.38, '#211', 0.34), 
        (7.62, 11.27, '#300', 0.38), 
        (8.10, 11.11, '#303', 0.42) 
    ]
    best_storage_efficiency = 0
    best_cost_efficiency = 0
    for radius, height in cans: 
	    if compute_storage_efficiency(radius,height)> best_storage_efficiency: 
                best_storage_efficiency = compute_storage_efficiency(radius,height) 
    for radius, height in cans: 
	    if compute_cost_efficiency(radius,height)> best_cost_efficiency: 
                best_cost_efficiency = compute_cost_efficiency(radius,height) 
    # For loop to iterate through my list and its values 
    for radius, height, name, cost in cans: 
        if compute_storage_efficiency(radius,height) == best_storage_efficiency:
            print(f'{name}: {compute_storage_efficiency(radius, height):.2f} ' 
                f'{compute_cost_efficiency(radius, height, cost):.2f}'
                f'{best_storage_efficiency}')
        elif  compute_cost_efficiency(radius,height) == best_cost_efficiency:
            print(f'{name}: {compute_storage_efficiency(radius, height):.2f} ' 
                f'{compute_cost_efficiency(radius, height, cost):.2f}'
                f'{best_cost_efficiency}')
        else:
            print(f'{name}: {compute_storage_efficiency(radius, height):.2f} ' 
                f'{compute_cost_efficiency(radius, height, cost):.2f}')
        
def compute_volume(radius, height): 
    # Compute and return the volume of a cylinder 
    volume = pi * radius**2 * height 
    return volume 
def compute_surface_area(radius, height): 
    # Compute and return the surface area of a cylinder 
    surface_area = 2 * pi * radius * (radius + height) 
    return surface_area 
def compute_storage_efficiency(radius, height): 
    storage_efficiency = (compute_volume(radius, height) / 
                          compute_surface_area(radius, height)) 
    return storage_efficiency 
def compute_cost_efficiency(radius, height, cost): 
    result = compute_volume(radius, height) / cost 
    return result 
main() 

 

 
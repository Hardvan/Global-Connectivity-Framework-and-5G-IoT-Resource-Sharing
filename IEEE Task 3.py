import random
import matplotlib.pyplot as plt


def getLowerandUpper():
    
    lower = round(random.uniform(1,3), 2)
    upper = 0
    while(upper <= lower):
        upper = round(random.uniform(1,20), 2)
    
    return lower, upper


def doBaseStation(slno):
    
    base_stations_name = [] # Storing Base Station Names
    lower_limit_list = []   # Storing Lower Limit time
    upper_limit_list = []   # Storing Upper Limit time
    success_list = []       # Storing No. of Successful Itertions
    ratios_list = []        # Storing Ratios


    n = 10                  # No. of Base Stations
    total_iterations = 20   # Total Iterations
    TIME = 5                # Time Limit for each task


    # Assigning Lower Limit, Upper Limit and Name for Base Stations
    for i in range(n):
        lower, upper = getLowerandUpper()
        lower_limit_list.append(lower)
        upper_limit_list.append(upper)
        
        base_stations_name.append("BS"+str(i+1))


    for i in range(n): # Each Base Station
        lower_limit = lower_limit_list[i]
        upper_limit = upper_limit_list[i]
        success = 0
        
        for j in range(total_iterations): # Each Iteration
            current_time = round(random.uniform(lower_limit, upper_limit),2)
            if current_time <= TIME:
                success += 1
        
        # Outside inner loop, we know no. of successful iterations
        success_list.append(success)
        ratios_list.append(success/total_iterations)


    # Plotting the graph

    # x-coordinates of left sides of bars 
    left = list(range(1,n+1))
      
    # Heights of bars: ratios_list
      
    # Labels for bars: base_stations_name
      
    # Plotting a Bar Chart
    plt.bar(left, ratios_list, tick_label = base_stations_name,
            width = 0.8, color = ["blue"])
      
    # Naming the x-axis
    plt.xlabel("Base Stations")

    # Naming the y-axis
    plt.ylabel("Ratios")

    # Plot Title
    plt.title("Ratio v/s Base Station of Controller {} Bar Chart".format(slno))
      
    # function to show the plot
    plt.show()
    
    return



controllers_name = []     # Storing Controller Names
c_lower_limit_list = []   # Storing Lower Limit time
c_upper_limit_list = []   # Storing Upper Limit time
c_success_list = []       # Storing No. of Successful Itertions
c_ratios_list = []        # Storing Ratios


n = 3                     # No. of Controllers
total_iterations = 20     # Total Iterations
TIME = 5                  # Time Limit for each task


# Assigning Lower Limit, Upper Limit and Name for Controllers
# and Performing Iterations

for i in range(1,n+1): # Each Controller

    doBaseStation(i)

    lower, upper = getLowerandUpper()
    c_lower_limit_list.append(lower)
    c_upper_limit_list.append(upper)
    
    controllers_name.append("CO"+str(i))
    
    success = 0
    
    for j in range(total_iterations): # Each Iteration
        current_time = round(random.uniform(lower, upper),2)
        if current_time <= TIME:
            success += 1
    
    # Outside inner loop, we know no. of successful iterations
    c_success_list.append(success)
    c_ratios_list.append(success/total_iterations)


# Plotting the graph for Controllers

# x-coordinates of left sides of bars 
left = list(range(1,n+1))
  
# Heights of bars: c_ratios_list
  
# Labels for bars: base_stations_name
  
# Plotting a Bar Chart
plt.bar(left, c_ratios_list, tick_label = controllers_name,
        width = 0.8, color = ["blue"])
  
# Naming the x-axis
plt.xlabel("Controllers")

# Naming the y-axis
plt.ylabel("Ratios")

# Plot Title
plt.title("Ratio v/s Controllers Bar Chart")
  
# function to show the plot
plt.show()

















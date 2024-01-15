#Run timing

def run_timing():
    
    number_of_runs = 0
    time_of_run = 0
    one_run = 0
    
    number_of_runs = int(input('How many runs? '))
    
    for one_run in range(0, number_of_runs):
        
        if number_of_runs > 0:
            
            try:
                one_run = float(input('Enter 10 km run time: '))
                #print(f'one_run = {one_run}')
                
            except ValueError as e: 
                print('Hey! Thats not a valid number!')
                
        time_of_run += float(one_run)
        
    
    avg = time_of_run / number_of_runs
    
    print(f'Average of {avg}, over {number_of_runs} runs')
      
run_timing()

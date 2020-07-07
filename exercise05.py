import csv
from operator import itemgetter



def read_file(fp):
    '''Docstring'''
    
    output_list = []
    reader = csv.reader(fp) # attaches a reader to the file fp
    next(reader,None) # skips a line, such as a header line
    for line_list in reader: # line_lst is a list
        if line_list[1] == 'Michigan':
            output_list.append(line_list)
        elif line_list[1] == 'New York':
            output_list.append(line_list)
        elif line_list[1] == 'Arizona':
            output_list.append(line_list)
        elif line_list[1] == 'Texas':
            output_list.append(line_list)
        elif line_list[1] == 'California':
            output_list.append(line_list)
       

    return output_list 

def get_totals(states,data):
    output = []
    for output_list in data:
        if output_list[0] == '6/20/20':
            if output_list[1] in states:
                output.append((output_list[1], int(output_list[3])))
    return output

    

def get_spike_dates(states,data):
    output = []
    max_spikes = [0,0,0,0,0]
    prev_cases = [0,0,0,0,0]
    dates = [0,0,0,0,0]
    for output_list in data:
        if output_list[1] == states[0]:
            state_index = 0
        if output_list[1] == states[1]:
            state_index = 1
        if output_list[1] == states[2]:
            state_index = 2
        if output_list[1] == states[3]:
            state_index = 3
        if output_list[1] == states[4]:
            state_index = 4
        cases = int(output_list[3])
        spike = cases - prev_cases[state_index]
        if spike > max_spikes[state_index]:
            max_spikes[state_index] = spike
            dates[state_index] = output_list[0]
        prev_cases[state_index] = cases
            
    for state, date, max_spike in zip(states, dates, max_spikes):
        output.append((state, date, max_spike))
    return output 
   

def main():    
    states = ['Michigan','New York','Arizona','Texas','California']

    fp = open("covid-19-us-states.csv")
    file_data = read_file(fp)
    
    
    state_totals = get_totals(states, file_data)

    if state_totals:  # if their values are not None
        print("\nTotal Coronavius cases by state\n")
        print("{:24s} {:10s}".format("State","#Cases"))
        for tup in state_totals:
            print("{:24s} {:2d}".format(tup[0],tup[1]))

    state_spikes = get_spike_dates(states, file_data)
    if state_spikes:  # if their values are not None
        print("\nDate of Coronavius spike by State \n")
        print("{:24s} {:10s} {:>8s}".format("State","Date","#Cases"))
        for tup in state_spikes:
            print("{:24s} {:10s} {:8d}".format(tup[0],tup[1],tup[2]))

if __name__ == "__main__":
    main()

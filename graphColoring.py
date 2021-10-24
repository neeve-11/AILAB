import copy

colors = ['Red', 'Blue', 'Green']

states = ['WA', 'NT', 'SA', 'QL', 'NSW', 'VC', 'TS']

graph = {}

graph['WA'] = ['SA', 'NT']
graph['NT'] = ['WA', 'SA', 'QL']
graph['SA'] = ['WA', 'NT', 'QL', 'NSW', 'VC']
graph['QL'] = ['NT', 'SA', 'NSW']
graph['NSW'] = ['SA', 'QL', 'VC']
graph['VC'] = ['SA', 'NSW']
graph['TS'] = []

stateColor = {}


def pickColor(stateColor, state):
    colorAvailable = copy.deepcopy(colors)
    for neighbour in graph[state] :
        for key, value in stateColor.items():
            if key == neighbour:
               colorAvailable.remove(stateColor[neighbour])
    return colorAvailable[0]            
    
    
def pickState(states):
    for state in states :
        stateColor[state] = pickColor(stateColor, state)

def main() :
    pickState(states) 
    print("Final Colored Graph :")
    print(stateColor)
    

    
if __name__ == "__main__" :
    main()


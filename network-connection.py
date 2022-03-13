
# a set where each person has assigned a list of friends
network1 = {
    'A' : ['C','M','X','Y'],
    'B' : ['K','O','R','Z'],
    'C' : ['A','D','M','X'],
    'D' : ['M','O','R','X'],
    'K' : ['B','R'],
    'M' : ['A','C','Y','Z'],
    'O' : ['B','D','Y'],
    'R' : ['B','D','K'],
    'X' : ['A','C','D','Z'],
    'Y' : ['A','K','M','O'],
    'Z' : ['B','M','X']
}
network2 = {
    'A' : ['C','D','E'],
    'B' : ['F','G','H'],
    'C' : ['A','D','E'],
    'D' : ['A','C','E'],
    'E' : ['A','C','D'],
    'F' : ['B','G','H'],
    'G' : ['B','F','H'],
    'H' : ['B','F','G'],
}

def BFS(network):
    persons_queue = []
    first_position_in_queue = 0
    last_position_in_queue = 0
    visited_persons = []

    # remember the path from A to B
    fathers_set = {}

    # we start from 'A' so we visit him because because otherwise it would make me an infinite loop and add him to father set
    persons_queue.append('A')
    visited_persons.append('A')
    fathers_set['A'] = 'A'

    # while we have no persons in persons_queue
    while first_position_in_queue <= last_position_in_queue:
        current_person = persons_queue[first_position_in_queue]
        first_position_in_queue += 1

        # trying to find 'B' or add the new persons to our queue
        for person in network[current_person]:
            if person == 'B': # if we find B just mark his father and return fathers set
                fathers_set[person] = current_person
                return fathers_set

            # if the person is not 'B' we try to add the person in queue for checking
            if person not in visited_persons:
                persons_queue.append(person)
                visited_persons.append(person)
                last_position_in_queue += 1
                fathers_set[person] = current_person
    return fathers_set

father_set = BFS(network2)

# we just go through all fathers starting from B till we reach A
def find_path(last_child):
    if last_child != 'A':
        find_path(father_set[last_child])
    print(last_child)

if 'B' in father_set.keys():
    find_path('B')
else:
    print("There is no connexion between A and B")
from bidict import bidict

'''Voters are presented with the official list of candidates. '''

#TODO import candidates from file
#TODO maybe combine candidate list and seats into an object

candidates = {1: 'Bob',
              2: 'Carol',
              3: 'Alice',
              4: 'Dave',
              5: 'Eve',
              6: 'Frank'}
seats_available = 3

#TODO let the ballots be presented to the voter in random order rather than alphabetically

ballots = []

'''
class ValidBallot:
    def __init__(self, id, candidates):
        self.id = id
        self.candidates = candidates
        self.preferences = bidict(candidates)}
    
'''

'''Issue: return error if anything other than the set {1,2,3.., candidates.length}



'''

def convert_ballot(ballot):
    preference_list = []
    current_search_number = 1
    while current_search_number <= len(candidates):
        for key in ballot:
            if ballot[key] == current_search_number:
               preference_list.append(key)
        current_search_number+= 1
    return preference_list 

print(convert_ballot({1:2,2:1,3:5,4:4,5:3}))

    


print(candidates)


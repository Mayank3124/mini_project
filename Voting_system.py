print("Options are: BJP, SP, CNG, BSP, AAP")

def vote(v, c):
    if c in v:
        v[c] += 1
    else:
        print(f'Error: {c} is not a valid candidate')

def tally(v):
    total = sum(v.values())
    for c, count in v.items():
        print(f'{c}: {count} votes')
    print(f'Total votes: {total}')

candidates_input = input('Enter the candidates (separated by commas): ')
candidates = [c.strip() for c in candidates_input.split(',')]
votes = {c: 0 for c in candidates}

vote(votes, 'BJP')
vote(votes, 'CNG')
vote(votes, 'SP')
vote(votes, 'AAP')
vote(votes, 'BSP')

tally(votes)

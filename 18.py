import pickle
from collections import defaultdict

def intersect (l1 ,l2 ):
    sol = []
    try :
        it1 = iter (l1)
        it2 = iter (l2)
        n1 = next (it1 )
        n2 = next (it2 )
        while True :
            if n1 == n2:
                sol. append (n1)
                n1 = next (it1 )
                n2 = next (it2 )
            else :
                if n1 < n2:
                    n1 = next ( it1 )
                else :
                    n2 = next ( it2 )
    except StopIteration :
        return sol
def main():
    
    post_dict = defaultdict(list)
    docs = pickle.load(open('docs.pickle', 'rb'))
    words = []
    newlist = []

  
    for k, v in docs.items():
        try:
            words.append(v[2].split())
        except:
            continue
    for item in words:
        try:
            newlist = newlist + item
        except:
            continue
    print(newlist)

main()

import random

names = ['Kev','Sam','Sean','Caro','Ren']
ppl_scores = {person:random.randint(1,100) for person in names}

print(ppl_scores)

#loop through dictionary, figure out who has a thing over 60 and put it into a new dict

passed_scores = {pkey:pvalue for (pkey,pvalue) in ppl_scores.items() if pvalue > 60}
print(passed_scores)
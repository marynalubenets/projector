#creating an empty list for cats
cats = []
#fill out the list with cats without hats
for i in range(0, 100):
    cats.append(False)

def count_cats(step, cats):
    while step < 101: #outre loop to track and update iterations counter
        for cat in range(0, len(cats), step): #inner loop to check cats
            cats[cat] = not cats[cat] #if cat has hat remove it, if not - place it
        step =  step + 1 # updaeting iteration step to be 1, 2, 3...100
    else: #when all iterations are done
        for index, cat in enumerate(cats): #loop to check cats that have hats
            if cat:
                print(f'Cat number {index} has a hat')

count_cats(1, cats) #call the function
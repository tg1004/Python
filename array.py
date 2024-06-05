#Statement1

exp=[2200,2350,2600,2130,2190]


# question_1 (in feb how many dollars you spent extra compare to january)

extra_dollars = exp[1]-exp[0]
print ("extra dollars spent on feb is:",extra_dollars)

# question_2Find out your total expense in first quarter (first three months) of the year.
total_expense_firstquarter = exp[0]+exp[1]+exp[2]
print("total expense in quarter:",total_expense_firstquarter)

# question3Find out if you spent exactly 2000 dollars in any month
for i in range(len(exp)):
    if exp[i]==200:
        print("exactly 200 dolars spent in:",(i+1))

    else:
        continue

# question4  June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.insert(5,1980)
print (exp)

#question5You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list
#based on this
exp[3]=exp[3]-200
print(exp)


#Statement2
heros=['spider man','thor','hulk','iron man','captain america']

#Length of the list
n=len(heros)
print (n)

#Add 'black panther' at the end of this list
heros.append('black panther')
print("list 2:",heros)

#You realize that you need to add 'black panther' after 'hulk',
  # so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print("list 3:",heros)

#Now you don't like thor and hulk because they get angry easily :)
  # So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
  # Do that with one line of code.

heros[1:3]=['doctor strange']
print(heros)

#Sort the heros list in alphabetical order
heros.sort()
print(heros)

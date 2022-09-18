counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

Temperature=int(input("what is the temp right now?"))
if Temperature>80:
    print("Switch on the AC")
else:
    print("Open the windows")

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
    #checking the while loops
x=0
while x<=5:
    print(x)
    x=x+1
# checking the for loop
for county in counties:
    print(county)
# checking the range function
# numbers=[0,1,2,3,4]
for i in range(len(counties)):
    print(counties[i])
# using f string
candidate_votes=int(input("how many votes did you get"))
total_votes=int(input("how many total votes were received"))
message_to_candidate=(f"you received a total number of {candidate_votes}. "
f"the total votes cast were {total_votes}. "
f"you recieved {candidate_votes/total_votes *100:.2f} % of votes")
print(message_to_candidate)








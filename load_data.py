import csv
file = 'D:\libmelee-openai-gym/rewards/rewards_callback.csv'
data = list(csv.reader(open(file)))

final_score = []
for row in range(len(data) - 1):
    if data[row + 1] == ['New Game'] and data[row] != ['Reward']:
        final_score.append(int(int(data[row][0]) > 0))

print(final_score)
print(sum(final_score)/len(final_score ))
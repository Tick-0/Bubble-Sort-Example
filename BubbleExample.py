seq = [64, 34, 25, 12, 22, 90, 11,1]
solved = False
while solved == False:
  solved = True
  for i in range(len(seq)-1):
    if seq[i] > seq[i+1]:
      seq[i], seq[i+1] = seq[i+1], seq[i]
      solved = False
print(seq)

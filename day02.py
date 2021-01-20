def validatepassword(mini, maxi, letter, password):
  count = 0
  for char in password:
    if char == letter:
      count += 1
  return maxi >= count >= mini

def newvalidatepassword(pos1, pos2, letter, password):
  #Wanted to use index(), but index would return the first occurance of the char so the script would fail on cccccccccc only returning the index of 0
  def split(word):
    return [char for char in word]
  count = 0
  ls_password = split(password)
  # print(ls_password)
  for x in range(len(ls_password)):
    if ls_password[x] == letter:
      if x + 1 == pos1:
        # print("match")
        count += 1
      elif x + 1 == pos2:
        # print("match")
        count += 1
  return count == 1


total_count_1 = 0
total_count_2 = 0
with open("day02_puzzle.txt") as file:
  for line in file:
    # print(line)
    freq, line, password = line.split(" ")
    # print(freq, line[0], password)
    letter = line[0]
    mini, maxi = map(int, freq.split('-'))
    # print(mini, maxi)
    if validatepassword(mini, maxi, letter, password):
      total_count_1 += 1
    #only thing that changes here is mini and maxi now are pos1 and pos2
    #pos1 parameter is mini variable
    if newvalidatepassword(mini, maxi, letter, password):
      total_count_2 += 1

print(total_count_1)
print(total_count_2)

# print(newvalidatepassword(1,3,"a", "abcde"))
# print(newvalidatepassword(2,9,"c", "ccccccccc"))


    
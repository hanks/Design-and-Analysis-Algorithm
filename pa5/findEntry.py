import collections

target_sums = [231552,234756,596873,648219,726312,981237,988331,1277361,1283379]

def buildEntryFromFile(file):
    entries = collections.defaultdict(lambda:0)
    f = open(file)
    for line in f:
        line = line.strip()
        num = int(line)
        entries[num] += 1
    return entries

def findEntries(sum, entries):
    can_sum = False
    if sum % 2 == 0:
        if entries.get(sum / 2) >= 2:
            can_sum = True
            return can_sum
    
    for i in entries.keys():
        if entries.get(sum - i) > 0:
            can_sum = True
            break
    return can_sum
    
def getResult(sums, entries):
    result = ""
    for i in sums:
        if findEntries(i, entries):
            result += "1"
        else:
            result += "0"
    return result

if __name__ == "__main__":
    entries = buildEntryFromFile("HashInt.txt")
    print getResult(target_sums, entries)

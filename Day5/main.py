with open(r"/content/drive/MyDrive/Colab Notebooks/testData.txt") as file:
  data = file.read()

data = data.split("\n\n")
data

seedInfo = data[0].split(":")[1].strip().split(" ")
seedInfo

def getMap(data,numberToCheck:list):
  dictionaryData = data.split(":")[1].strip().split("\n")
  outputDict = {}
  for dataLine in dictionaryData:
    data = dataLine.split(" ")
    source_start = int(data[1])
    dest_start = int(data[0])
    length = int(data[2])
    sourceList = list(range(source_start,source_start+length))
    destList = list(range(dest_start,dest_start+length))
  
  output = [0]*len(numberToCheck)
  for idx,num in enumerate(numberToCheck):
    if num in sourceList:
      src_idx = sourceList.index(num)
      output[idx] = destList[src_idx]
    else:
      output[idx] = num
  
  return output


outputList = [int(seed) for seed in seedInfo]

for map in data[1:]:
  mappedList = getMap(map,outputList) 
  print(f"input:{outputList} mapped:{mappedList}")
  outputList = mappedList
  

outputList 

min(outputList)

class BinarySearch(list):


  # Create a list length a and steps b
  def __init__(self, a, b):
    self.a = a
    self.b = b
         
    for i in range(self.a):
      list.append(self, self.b)
      self.b +=b
      i +=1
  
    self.length = i
    
    
  # the binary search algorithm
  def search(self,value):
    firstvalue = 0
    lastvalue = self.length-1
    isfound = False
    count = 0
    in_list = False
    
    #if number appears on  list set index to lowest index
    try:
      index = self.index(value)
      in_list = True
    except ValueError:
      index = -1
      in_list = False

    # compare middle element of list with target value
    while firstvalue<=lastvalue and not isfound and in_list and value != self[lastvalue]:
        midpoint = (firstvalue+lastvalue)//2
        mid_value = self[midpoint]
        if mid_value == value:
            isfound = True
            count +=1
            index = midpoint
        else:
            if value < mid_value:
                lastvalue = midpoint - 1
                count +=1
            else:
                firstvalue = midpoint + 1
                count +=1
    
    		# return number of iterations & index of value found in list
                return {"count": count, "index": index}

# Test Function
#print(BinarySearch(10, 3)) 
 

def reverse(S):
  input_string = S.split(" ")
  input_string = input_string[-1::-1]
  output = ' '.join(input_string)
  return output
if __name__ =='__main__':
  S='hello world'
  print (reverse(S))

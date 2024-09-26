import sys

argument = sys.argv

inputfile = open(argument[2])
input_string = inputfile.read()
inputfile.close()

if len(argument) < 4:
  print("引数が不足しています。")
else:
  if argument[1] == "reverse":
    if(argument[2] == "" or argument[3] == ""):
      print("無効なパスです。")
    else:
      reversed_string_list = list(reversed(input_string))
      reversed_string = "".join(reversed_string_list)
      outputfile = open(argument[3], "w")
      outputfile.write(reversed_string)
      outputfile.close()
  elif argument[1] == "copy":
    if(argument[2] == "" or argument[3] == ""):
      print("無効なパスです。")
    else:
      outputfile = open(argument[3], "w")
      outputfile.write(input_string)
      outputfile.close()
  elif argument[1] == "duplicate-contents":
    if(argument[2] == "" or int(argument[3]) <= 0):
      print("無効な入力です。")
    else:
      for i in range(int(argument[3])):
        dot_location = argument[2].find(".")
        outputfile = open(argument[2][0:dot_location] + f"({i + 1})" + argument[2][dot_location:len(argument[2])], "w")
        outputfile.write(input_string)
        outputfile.close()
  elif argument[1] == "replace-string":
    if len(argument) < 5:
      print("引数が不足しています。")
    elif(argument[2] == "" or input_string.find(argument[3]) == -1):
      print("無効な入力です。")
    else:
      replace_string = input_string.replace(argument[3], argument[4])
      outputfile = open(argument[2], "w")
      outputfile.write(replace_string)
      outputfile.close()
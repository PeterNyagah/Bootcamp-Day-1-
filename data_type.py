def data_type(data):

  if type(data) == str:
    return len(data)

  elif data == None:
    return "no value"

  elif data == True or data == False:
    return data

  elif type(data) == int:

    if data < 100:
      return "less than 100"

    elif data > 100:
      return "more than 100"

    else:
      return "equal to 100"

  elif type(data) == list:

    if len(data) >= 3:
      return data[2]
    else:
      return None
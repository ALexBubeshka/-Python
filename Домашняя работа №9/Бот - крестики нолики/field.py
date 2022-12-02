
field = []

def print_field (field_print):
      global field
      f1 = ''
      for i in range (3):
            print("  ".join(field_print[i]))
            f1 +="  ".join(field_print[i])
            f1 += '\n'
      # bot.send_message(message.chat.id,f1)      
      return f1

for i in range (3):
      
      fieldrow = []
      for j in range (3):
            fieldrow.append ('-')
      field.append (fieldrow)
print_field(field)

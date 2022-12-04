from easygui import *
def start_inteface():
      msg ="Добро пожаловать в калькулятор\nВыберете один из пунтов"
      title = "Калькулятор"
      choices = ["Операции с рациональными числами", "Операции над комплексными числами"]
      choice = choicebox(msg, title, choices)
      return str(choice)

def choice_interface (choice):
      if choice == "Операции с рациональными числами":
            try:
                  text = "Введите данные через пробел\nПример: "
                  title = "Операции с рациональными числами"
                  d_text = "5 / 4 * 6 / 7 + 3 / 2 - 9" # Тут берем данные
                  output = enterbox(text, title, d_text)
                  if output:
                        message = str(output) + "=" + "подставить решение\n\nХотите рассчитать снова?"# тут передать данные из функции Вадима
                        title = "Решение" 
                        output = ynbox(message, title,("Да","Нет"))
                        if output:     
                              choice_interface("Операции с рациональными числами")
                        else:     
                              choice_interface(start_inteface())
                  else:
                        choice_interface(start_inteface())               
            except:
                  exceptionbox()
      elif choice == "Операции над комплексными числами":
            try:
                  text = "Введите данные через пробел\nПример: "
                  title = "Операции над комплексными числами"
                  d_text = "( x1 + iy 1 ) + ( x2 + iy2 ) = ( x1 + x2 ) + i( y1 + y2 )" # Тут берем данные
                  output = enterbox(text, title, d_text)
                  if output:
                        message = str(output) + "=" + "подставить решение\n\nХотите рассчитать снова?" # тут передать данные из функции Вадима
                        title = "Решение"
                        output = ynbox(message, title,("Да","Нет"))
                        if output:     
                              choice_interface("Операции над комплексными числами")
                        else:     
                              choice_interface(start_inteface())
                  else:
                        choice_interface(start_inteface())
            except:
                        exceptionbox()
choice_interface(start_inteface())



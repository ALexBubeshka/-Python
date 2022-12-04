Telegram bot для работы с базой данных работников предприятия
==============
Всем привет. Рад Вам представить программу по решению проблем с хранением данных работников на предприятии.
Данные всех сотрудних хранятся в JSON формате, что позволяет с легкотью использовать не только в telegram.

<a href="https://files.fm/f/svnh93h5p"><img src="https://files.fm/thumb_show.php?i=svnh93h5p"></a>

<a href="https://files.fm/f/f74jnbgj2"><img src="https://files.fm/thumb_show.php?i=f74jnbgj2"></a>

Блок по добавлению работника в базу данных
------------------------------------------
Для добавления нового работника необходимо вводить данные которые запрашивает бот.


<a href="https://files.fm/f/hsqy6jjfk"><img src="https://files.fm/thumb_show.php?i=hsqy6jjfk"></a>
        
        def fio_empl(message):
             global new_empl_info
             new_empl_info['Full name'] = message.text
             msg = bot.send_message(message.chat.id, 'Введите пол (F / M) нового работника')
             bot.register_next_step_handler(msg, sex_empl)

        def sex_empl(message):
            new_empl_info['Sex'] = message.text
            msg = bot.send_message(message.chat.id, 'Введите дату рождения нового работника (dd.mm.year)')
            bot.register_next_step_handler(msg, age_empl)

        def age_empl(message):
            new_empl_info['Birth date'] = message.text
            msg = bot.send_message(message.chat.id, 'Введите семейное положение нового работника')
            bot.register_next_step_handler(msg, marital_status_empl)

        def marital_status_empl(message):
            new_empl_info['Marital status'] = message.text
            msg = bot.send_message(message.chat.id, 'Введите должность нового работника')
            bot.register_next_step_handler(msg, job_title_empl)

        def job_title_empl(message):
            new_empl_info['Job title'] = message.text
            msg = bot.send_message(message.chat.id, 'Введите заработную плату нового работника')
            bot.register_next_step_handler(msg, salary_empl)

        def salary_empl(message):
            new_empl_info['salary'] = int(message.text)
            msg = bot.send_message(message.chat.id, 'Введите первый телефонный номер нового работника')
            bot.register_next_step_handler(msg, phone_1)

        def phone_1(message):
            global phones
            ph_1 = message.text
            phones.append(int(ph_1))
            msg = bot.send_message(message.chat.id, 'Введите второй телефонный номер нового работника')
            bot.register_next_step_handler(msg, phone_2)

        def phone_2(message):
            global phones
            ph_2 = message.text
            phones.append(int(ph_2))
            ending_dict(message)

        def ending_dict(message):
            new_empl_info['Phone numbers'] = phones
            adding_id(message)

        def adding_id(message):
            with open('employees.json', 'r') as file:
                data = json.load(file)
                for k, v in data.items():
                    keys.append(k)
            new_empl_key = int(keys[-1]) + 1
            data[new_empl_key] = new_empl_info
            with open('employees.json', 'w')as file:
                json.dump(data, file, indent=4)
            bot.send_message(message.chat.id, "Новый сотрудник добавлен.")
            bot.send_message(message.chat.id, json.dumps(data, indent=4

Блок по удалению работника из базы данных
-----------------------------------------
Для удаления необходимо ввести полностью ФИО работника.

<a href="https://files.fm/f/hazpmhjvj"><img src="https://files.fm/thumb_show.php?i=hazpmhjvj"></a>

        def del_el(exempl_1):
            global del_element
            with open('employees.json', 'r') as file:
                data = json.load(file)
                for k, v in data.items():
                    if v['Full name'] == exempl_1:
                        del data[k]
                        break
            with open('employees.json', 'w')as file:
                json.dump(data, file, indent=4)


Блок по отбору информации по критериям
---------------------------------------

<a href="https://files.fm/f/6y6gxr8m7"><img src="https://files.fm/thumb_show.php?i=6y6gxr8m7"></a>

          results = {}
          def searching_el(msg):
              global results
              with open('employees.json', 'r') as file:
                  data = json.load(file)

                  for k, v in data.items():
                      for i in range(len(msg)):
                          if v['Full name'] == msg:
                              results[k] = v
                          elif v['Sex'] == msg:
                              results[k] = v
                          elif v['Birth date'] == msg:
                              results[k] = v
                          elif v['Marital status'] == msg:
                              results[k] = v
                          elif v['Job title'] == msg:
                              results[k] = v
                          elif str(v['salary']) == msg:
                              results[k] = v
                          elif str(v['Phone numbers'][0]) == msg:
                              results[k] = v
                          elif str(v['Phone numbers'][1]) == msg:
                              results[k] = v
              print(results)


Над проектом работал
---------------------------------------
Бубешко Александр (https://github.com/ALexBubeshka)

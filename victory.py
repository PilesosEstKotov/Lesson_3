
import random

famous_people = {
    "Михаил Горшенев (Князь)": "07.08.1973",
    "Андрей Князев (Княzz)": "13.02.1975",
    "Александр Балунов (Балу)": "15.07.1972",
    "Александр Щиголев (Щур)": "22.09.1970",
    "Яков Цветков (Яша)": "01.04.1974",
    "Андрей Лапин (Лапа)": "03.06.1971",
    "Дмитрий Гордеев (Грязный)": "10.11.1969",
    "Алексей Жидков (Жид)": "12.05.1974",
    "Павел Семёнов (Паук)": "09.03.1976",
    "Игорь Дорофеев (Гарик)": "18.11.1973"
}

def main():
    selected_people = random.sample(list(famous_people.keys()), 5)

    correct_answers = 0

    print("Угадайте дату рождения следующих участников группы 'Король и Шут':")
    for person in selected_people:
        user_answer = input(f"Когда родился {person}? (в формате день(dd).месяц(mm).год(yyyy)): \n")
        if user_answer == famous_people[person]:
            print("Правильно!")
            correct_answers += 1
        else:
            date_correct = famous_people[person].split(".")
            print(f"Неправильно. Правильный ответ: {date_correct[0]} {num_to_month(date_correct[1])} {date_correct[2]} года.")

    print(f"\nИгра окончена. Правильных ответов: {correct_answers}. Неправильных ответов: {5 - correct_answers}.")
    if input("Хотите начать снова? (да/нет): ").lower() == "да":
        main()

def num_to_month(num):
    months = {
        "01": "января",
        "02": "февраля",
        "03": "марта",
        "04": "апреля",
        "05": "мая",
        "06": "июня",
        "07": "июля",
        "08": "августа",
        "09": "сентября",
        "10": "октября",
        "11": "ноября",
        "12": "декабря"
    }
    return months.get(num, "неправильный месяц")

if __name__ == "__main__":
    main()
def display_intro():
    print("Добро пожаловать на тест DISC!")
    print("Пожалуйста, ответьте на следующие вопросы, выбирая число от 1 до 4:")
    print("1 - Совершенно не согласен")
    print("2 - Не согласен")
    print("3 - Согласен")
    print("4 - Совершенно согласен")
    print("")

def ask_questions(questions):
    scores = {'D': 0, 'I': 0, 'S': 0, 'C': 0}
    for question in questions:
        print(question['text'])
        while True:
            try:
                answer = int(input("Ваш ответ (1-4): "))
                if answer < 1 or answer > 4:
                    raise ValueError
                scores[question['type']] += answer
                break
            except ValueError:
                print("Пожалуйста, введите число от 1 до 4.")
    return scores
def display_results(scores):
    max_score = max(scores.values())
    traits = [k for k, v in scores.items() if v == max_score]
    # Вывод результатов
    print("\nРезультаты теста DISC:")
    for trait, score in scores.items():
        print(f"{trait}: {score}")
    if len(traits) > 1:
        print("Ваши доминирующие стили: " + ", ".join(traits))
    else:
        print(f"Ваш доминирующий стиль: {traits[0]}")
        print(get_description(traits[0]))
def get_description(trait):
    descriptions = {
        'D': "Доминация (D): Вы ориентированы на результат, стремитесь к власти и контролю. Вы уверены в своих силах и предпочитаете принимать решения быстро.",
        'I': "Влияние (I): Вы динамичны и общительны. Вам нравится быть в центре внимания, и вы умеете вдохновлять других.",
        'S': "Стабильность (S): Вы цените гармонию и спокойствие. Вы заботитесь о других и стремитесь создать коллективную атмосферу.",
        'C': "Согласие (C): Вы ориентируетесь на детали и точность. Вы стремитесь к качеству и анализируете информацию перед принятием решений."
    }
    return descriptions.get(trait, "Описание отсутствует.")

def main():
    display_intro()
    questions = [
        {'text': "Я предпочитаю принимать решения быстро.", 'type': 'D'},
        {'text': "Я люблю быть в центре внимания.", 'type': 'I'},
        {'text': "Я ценю стабильность и порядок.", 'type': 'S'},
        {'text': "Я ориентируюсь на детали и факты.", 'type': 'C'},
        {'text': "Я люблю брать на себя ответственность.", 'type': 'D'},
        {'text': "Я вдохновляю людей своими идеями.", 'type': 'I'},
        {'text': "Я работаю лучше, когда есть четкие инструкции.", 'type': 'C'},
        {'text': "Я проявляю терпение в сложных ситуациях.", 'type': 'S'},
        {'text': "Я люблю бросать вызовы другим.", 'type': 'D'},
        {'text': "Я предпочитаю работу в команде.", 'type': 'S'},
        {'text': "Я стремлюсь к общественному признанию.", 'type': 'I'},
        {'text': "Я профессионал в своей области и ценю компетентность.", 'type': 'C'},
    ]
    scores = ask_questions(questions)
    display_results(scores)

if __name__ == "__main__":
    main()
import database

MENU_PROMPT = """

==============================
    --Registro de cafés--

Eliga una opcion:

1) Agregar un café.
2) Ver todos los cafés.
3) Encontrar café por nombre.
4) Ver mejor método de preparación de un grano de café.
5) Salir.

Tu selección: """


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            prompt_add_new_bean(connection)
        elif user_input == "2":
            prompt_see_all_beans(connection)
        elif user_input == "3":
            prompt_find_bean(connection)
        elif user_input == "4":
            prompt_find_best_method(connection)
        else:
            print("Valor inválido, intente de nuevo.")



def prompt_add_new_bean(connection):
    name = input("Ingrese nombre del grano de café: ")
    method = input("Ingrese modo de preparación: ")
    rating = int(input("Ingrese la calificacion que recibió (0-100): "))

    database.add_bean(connection, name, method, rating)


def prompt_see_all_beans (connection):
    beans = database.get_all_beans(connection)

    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")


def prompt_find_bean(connection):
    name = input("Ingrese nombre del grano de café a encontrar: ")
    beans = database.get_beans_by_name(connection, name)

    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")


def prompt_find_best_method(connection):
    name = input("Ingrese nombre del grano de café a encontrar: ")
    best_method = database.get_best_preparation_for_bean(connection, name)
    
    print(f"El mejor metodo de preparacion para {name} es: {best_method[2]}")

menu()
def allowed_to_attend_python_class(name):


    match name:
        case "dell":
            print("you have entered dell")
        case "himanth":
            print("you have entered himanth")

        case "vikas":
            print("you have entered vikas")

        case _:
            print("no idea")


allowed_to_attend_python_class("vikas")

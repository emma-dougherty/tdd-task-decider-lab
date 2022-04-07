def get_preferred_option(task1, task2):
    if task1 == "Wash Dishes" and task2 == "Cook Dinner":
        if task1 == "Cook Dinner" and task2 == "Wash Dishes":
            if task1 == "Wash Dishes" and task2 == "Wash Clothes":
                if task1 =="Wash Clothes" and task2 == "Wash Dishes" :
                    return "Wash Dishes"

    elif task1 == "Cook Dinner" and task2 == "Clean Windows":
        if task1 == "Clean Windows"and task2 == "Cook Dinner":
            if task1 == "Cook Dinner"and task2 == "Do Ironing":
                if task1 == "Do Ironing" and task2 == "Cook Dinner":
                    return "Cook Dinner"

    elif task1 == "Clean Windows" and task2 == "Wash Dishes":
            if task1 == "Wash Dishes"and task2 == "Clean Windows":
                    if task1 == "Do Ironing" and task2 == "Clean Windows":
                        if task1 == "Clean Windows" and task2 == "Do Ironing":
                            return "Clean Windows"

    elif task1 == "Wash Clothes" and task2 == "Cook Dinner":
            if task1 == "Cook Dinner" and task2 == "Wash Clothes":
                if task1 == "Wash Clothes"and task2 == "Clean Windows":
                    if task1 == "Clean Windows" and task2 == "Wash Clothes":
                            return "Wash Clothes"
    
    elif task1 == "Do Ironing" and task2 == "Wash Clothes":
            if task1 == "Wash Clothes"and task2 == "Do Ironing":
                if task1 == "Wash Dishes"and task2 == "Do Ironing":
                    if task1 == "Do Ironing" and task2 == "Wash Dishes":
                            return "Do Ironing"



    # elif task1 == "Wash Dishes"and task2 == "Clean Windows":
    #     return "Clean Windows"

# elif task2 == "Cook Dinner" and task2 == "Wash Dishes":
    #     return "Wash Dishes"
    # elif task1 == "Clean Windows"and task2 == "Cook Dinner":
    #     return "Cook Dinner"
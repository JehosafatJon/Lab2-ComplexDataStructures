def main():

    # Step 2 - Create a complex data structure
    about_me = {
        'full_name':"Jonathan Hughes",
        'student_id':10297309,
        'pizza_toppings':[
            "PEPPERONI",
            "BACON",
            "PINEAPPLE"
        ],
        'movies':[
            {
                'title':"dune",
                'genre':"sci-fi"
            },
            {
                'title':"the big short",
                'genre':"drama"
            }
        ]
    }

    # Step 3 - Add another movie to the data structure
    about_me['movies'].append({
        'title':"monty python and the holy grail",
        'genre':"comedy"
        })

    # Step 4-8 function calls
    print_student_name_and_id(about_me)

    print_pizza_toppings(about_me)
    
    new_toppings = ("JALAPENOS","MUSHROOMS")
    add_pizza_toppings(about_me, new_toppings)

    print_pizza_toppings(about_me)

    print_movie_genres(about_me)

    print_movie_titles(about_me['movies'])

    return

# Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):

    print(f"My name is {about_me['full_name']}, but you can call me His Majesty {about_me['full_name'].split()[0]}.")
    print(f"My student ID is {about_me['student_id']}.\n")

    return
    
# Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    
    about_me['pizza_toppings'].extend(toppings)

    about_me['pizza_toppings'].sort()

    for i,t in enumerate(about_me['pizza_toppings']):
        about_me['pizza_toppings'][i] = t.lower()
    return

# Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):

    print(f"My favourite pizza toppings are:")
    for t in about_me['pizza_toppings']:
        print(f"- {t}")
    print()

    return

# Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):

    print(f"I like to watch ", end="")
    for i,g in enumerate(about_me['movies']):
        if i < len(about_me['movies'])-1:
            print(f"{g['genre']}, ", end="")
        else:
            print(f"and {g['genre']} movies.\n")
    
    return 

# Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):

    print(f"Some of my favourite movies are ", end="")
    for i,t in enumerate(movie_list):
        if i < len(movie_list)-1:
            print(f"{t['title'].title()}, ", end="")
        else:
            print(f"and {t['title'].title()}!\n")
    
    return 
    
if __name__ == '__main__':
    main()
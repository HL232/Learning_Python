
shopping_list = ["apple","pear","bananna"]

def is_in_shopping_list(candidate):
    clean_candidate = candidate.strip()
    for item in shopping_list:
        if item == clean_candidate:  
            return True

    return False
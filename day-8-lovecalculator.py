def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    first_count = sum(lower_names.count(c) for c in "true")
    #print("Count from TRUE:", first_count)

    second_count = sum(lower_names.count(c) for c in "love")
    #print("Count from LOVE:", second_count)
    
    score = int(str(first_count) + str(second_count))
    
    print(score)
    
calculate_love_score("Kanye West", "Kim Kardashian")

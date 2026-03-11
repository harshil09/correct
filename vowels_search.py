def vowels(func):
    def main_method(name):
        vowels="aieouAEIOU"
        
        found=[char for char in name if char in vowels]
        
        print(f"vowels= {found}")
        func(name)
      
    return main_method
        

@vowels
def calling_function(name):
    print("original text=" +name)
name=str(input("enter a string == "))
calling_function(name)
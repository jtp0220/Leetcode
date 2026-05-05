from test import Test
        
def main():    
    print("\nLeetcode Solutions (Python)\n")
    Test.show_problems()
    
    while(True):
        print("=" * 55)
        print("\nMenu:\n - [number] to run a problem\n - q to quit\n - p to show problems")
        print("\nInput: ", end="")
        str = input()

        if(str.lower() == 'q'):
            return
        
        if(str.lower() == 'p'):
            print()
            Test.show_problems()
            continue
        
        try:
            problem = int(str)
            print()
            Test.run(problem)
        except ValueError:
            print("\nPlease enter a valid menu option.\n")
    
if __name__ == "__main__":
    main()
    
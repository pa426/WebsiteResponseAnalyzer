import os

# WebsiteResponseAnalyzer is a terminal application that returns a JSON file
# with information about the http response for each adress inserted as a input.

class Analyzer:
    'Main Class'
    def display_title_bar(self):
        # Clear the terminal screen, and display title bar.
        os.system('clear')

        print("\t**********************************************")
        print("\t***         Analyze Web Site v0.1          ***")
        print("\t**********************************************")

    def get_user_choice(self):
        # Let users know what they can do.
        print("\n[1] Insert web site")
        print("[2] Show me history")
        print("[q] Quit.")

        return input("What would you like to do? ")

    def quit(self):
        # This function dumps the names into a file, and prints a quit message.
        try:
            print("\n Quit.")
        except Exception as e:
            print("\n Quit.")
            print(e)

    def main(self):
        # Set up a loop where users can choose what they'd like to do.1

        choice = ''
        self.display_title_bar()
        while choice != 'q':

            choice = self.get_user_choice()

            # Respond to the user's choice.
            self.display_title_bar()
            if choice == '1':
                print("\n Website")
            elif choice == '2':
                print("\n History")
            elif choice == 'q':
                self.quit()
                print("\nThanks for playing. Bye.")
            else:
                print("\nI didn't understand that choice.\n")


Analyzer().main()

#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# AZhong, 2021-Mar-07, added actual code to CD Inventory file 
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
e = '' # error

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # Info about CD class
    
    def __init__(self, cd_id, cd_title, cd_artist):
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
    
    @property
    def cd_id(self): 
        return self.__cd_id
    @cd_id.setter
    def cd_id(self, cd_id):
        if cd_id == int:
            self.__cd_id = cd_id
        else:
            raise Exception ('ID has to be an interger.')
    
    @property
    def cd_title(self):
        return self.__cd_title
    @cd_title.setter
    def cd_title(self, title):
        self.__cd_title = title
            
    @property
    def cd_artist(self):
        return self.__cd_artist
    @cd_artist.setter
    def cd_artist(self, artist):
        self.__cd_artist = artist
    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        add_entry_to_table(entry, table) > (a list of CD objects)
        write_file(file_name, table): -> None
        read_file(file_name, table): -> (a list of CD objects)

    """
    # TODO Add code to process data from a file
    # TODO Add code to process data to a file
    @staticmethod
    def add_entry_to_table(cd, table):
        """Method to add user entries to the table

        Args:
            cd (list): user input from ask_new_entry().
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """  
        dicRow = {'ID': cd.cd_id, 'Title': cd.cd_title, 'Artist': cd.cd_artist}
        table.append(dicRow)

    
    @staticmethod
    def read_file(file_name, table):
        """Method to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        try:
            objFile = open(file_name, 'r')
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                table.append(dicRow)
            objFile.close()
        except FileNotFoundError:
            print('ERROR: file does not exist.')

    @staticmethod
    def write_file(file_name, table):
        """Method to write save entries to an external text file
        
        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            True: file has been saved
        """
        objFile = open(file_name, 'w')
        for row in table:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    """input and output:

    properties:

    methods:
        print_menu(): -> None
        menu_choice(): -> None
        show_inventory(table):: -> (a list of CD objects)
        ask_new_entry(): -> None

    """
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('\nMenu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    # captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform?\n[l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    # display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print()
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    # get CD data from user
    @staticmethod
    def ask_new_entry():
        """Ask the user to enter the CD ID, title and artist name

        Args:
            cd_id: ID value
            cd_title: song title
            cd_artist:  artist name

        Returns: list of user inputs in order of ID, Title, and Artist name
            
        """
        
        cd_id = ''
        while True:
            try:
                cd_id = int(input('Enter ID: ').strip())
                break
            except ValueError:
                print('ERROR: Please enter a number only.')
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
        return CD(cd_id, cd_title, cd_artist)

# -- Main Body of Script -- #
# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program

# 1. load data from file into a list of CD objects on script start
FileIO.read_file(strFileName, lstTbl)


# 2 start main loop
while True:
      try:
        # 2.1 Display Menu to user and get choice
        IO.print_menu()
        strChoice = IO.menu_choice()
        # 3. Process menu selection
        # 3.1 process exit first
        if strChoice == 'x':
            print('Thanks for using the program. See you later!')
            break
        # 3.2 process load inventory
        if strChoice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled ')
            if strYesNo.lower() == 'yes':
                print('reloading...')
                FileIO.read_file(strFileName, lstTbl)
                IO.show_inventory(lstTbl)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstTbl)
            continue  # start loop back at top.
        # 3.3 process add a CD
        elif strChoice == 'a':
            # 3.3.1 Ask user for new ID, CD Title and Artist
            cd = IO.ask_new_entry()
            # 3.3.2 Add item to the table
            FileIO.add_entry_to_table(cd, lstTbl)
            IO.show_inventory(lstTbl)
            continue  # start loop back at top.
        # 3.4 process display current inventory
        elif strChoice == 'i':
            IO.show_inventory(lstTbl)
            continue  # start loop back at top.
        # 3.5 process save inventory to file
        elif strChoice == 's':
            # 3.6.1 Display current inventory and ask user for confirmation to save
            IO.show_inventory(lstTbl)
            strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
            # 3.6.2 Process choice
            if strYesNo == 'y':
                # 3.6.2.1 save data
                FileIO.write_file(strFileName, lstTbl)
                print('The inventory has been saved to file.')
            else:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            continue  # start loop back at top.
        # 3.6 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
        else:
            print('General Error')
      except Exception as e: # catch all
        print(e.__doc__)


import pandas as pd

# This class extends pandas.Dataframe. Some of the definitions in this class require 
# single-index DataFrames.
class CRUD(pd.DataFrame):
    """
    A class that extends pandas.DataFrame and provides CRUD (Create, Read, Update, Delete) operations.
    
    Parameters:
    -----------
    *args, **kwargs: Arguments and keyword arguments to initialize the DataFrame.
    
    Attributes:
    -----------
    Inherits all attributes from the parent class pandas.DataFrame.
    
    
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize a CRUD DataFrame.
        
        Parameters:
        -----------
        *args, **kwargs: Arguments and keywords arguments used to initialize the DataFrame.
        
        
        """
        super(CRUD, self).__init__(*args, **kwargs)
        
    def create(self, *args):
        """
        CREATE: Adds new rows to the DataFrame.
        
        Parameters:
        -----------
        *args: Variable length argument list representing the data for the new record.
        
        Returns:
        -----------
        CRUD: Updated DataFrame with the new record added.
        
        """
        new_record = pd.DataFrame(*args)
        return pd.concat([self, new_record], ignore_index=True, axis=0)

    def read(self):
        """
        READ: Retrieves the current state of the DataFrame.
        
        Returns:
        -----------
        CRUD: Current state of the DataFrame.
        
        
        """
        display(self)
    
    def update(self, index, new_data):
        """
        UPDATE: Modifies rows in the DataFrame
        
        Parameters: 
        -----------
        index: int
            Index of the row to be updated.
        new_data: array-like
            New data to replace the existing row.
            
        Returns:
        -----------
        None
        
        Notes: 
        -----------
        This definition overloads the 'update' definition from the parent class pd.DataFrame.
        
        
        """
        self.loc[index] = new_data
    
    def delete(self, index):
        """
        DELETE: Removes rows from the DataFrame.
        
        Parameters:
        -----------
        index: int
            Index of the row to be deleted.
            
        Returns:
        -----------
        None
        
        
        """
        self.drop(index, inplace=True)
        self.reset_index(drop=True, inplace=True)
        
    def kaboom(self):
        """
        DELETE: Removes all rows from the DataFrame.
        
        Parameters:
        -----------
        None
            
        Returns:
        -----------
        None
        
        
        """
        self.drop(self.index, inplace=True)
        
        
        
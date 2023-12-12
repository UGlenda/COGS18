import pytest
import random
import pandas
from classes import *
from functions import *

# create three lists for employee name, id, and salary
song_title = ["Fly Me to the Moon", "Avatar's Love", "His Theme", "Fur Elise", "Houdini"] 
musician = ["Frank Sinatra", "Avatar: L.A.", "Undertale", "Beethoven", "Foster the People"] 
difficulty = ["Easy", "Medium", "Medium", "Hard", "Hard"] 
     
# initialize a dictionary with the three lists
dict = {'Song Title': song_title, 'Musician': musician, 'Difficulty': difficulty}  
       
# create a Pandas DataFrame from the dictionary
df = pd.DataFrame(dict) 
df.index += 1

def test_CRUD_create():
    
    crud = CRUD(df)
    test = CRUD(crud.create({'Song Title':["test"],'Musician':["tester"],'Difficulty':["Easy"]}))
    assert len(test) == 6

def test_CRUD_delete():
    test = CRUD(df)
    old_len = len(test)
    test.delete(1)
    assert len(test) == (old_len-1)

def test_CRUD_update():
    test = CRUD(df)
    test.update(1, {'Song Title':["up"],'Musician':["date"],'Difficulty':["Hard"]})
    assert test.at[1, "Song Title"][0] == "up"

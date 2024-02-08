# Boggle

## What I want

PLAY FUNCTION
- Given a boggle board state, a list of 16 characters I want the program to
  - Create a file with:
    1. Image of the board
    2. List of all words (ordered shortest to longest, alphetebiacally)
    3. Num of 3,4,5,6,... letter words
    4. Num of total words
  - Return data object: [board, big total, small totals]

- Generate a random boogle board state (using boggle dice).

- Greate a list of all 3,4,5,6,7,8,9,10 letter words that are possible given 
boggle dice array.



## TODO

- [x] Get a list of all english words.
- [ ] Make boggle word list. 
  - [ ] Clean the english list. 
    - [ ] Remove all words starting with capital letter.
    - [ ] Remove all words containing non [a-z]
    - [ ] Remove all words with length not in range 3-16
    - [ ] Rename new list `boggle_master_list.txt`
    - [ ] OPTIONAL Reduce the list even further.
- [ ] 

- [ ] Write function that prints and returns a new scrambled boggle board.

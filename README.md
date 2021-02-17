# EE 5450 Module 1, Homework 2
Securing and Authenticating your FastAPI-based Web API for Multi-user, Multi-game Blackjack

# Introduction

In this assignment, you'll be making adding HTTPS/TLS support and user authentication (account creation/login) to your 
Blackjack server Web API.  To facilitate this, I've created a folder named `keys` where you should put your self-signed 
public/private keys made with [mkcert](https://github.com/FiloSottile/mkcert/releases).  The public certificate 
should be named `public.pem` and the private key should be named `private.pem`.  I've also made a new Python module 
named `user_db.py`, which will guide you through writing authentication middleware for your Web API.  Then, when you are
done writing the authentication middleware, you will add usage of the authentication middleware to your Web API.

To get started, make sure all packages in `requirements.txt` are installed: `conda install --file requirements.txt`

Then, open up `user_db.py` and `test_user_db.py`.  The UserDB class will 

However, this time you will write your own unit tests for `user_db.py` inside `test_user_db.py`.  I will have my
own unit tests, but this lets you practice another new skill.  


# Web API HTTP Paths and Responses

## home()
```
GET /
returns: {'message': 'Welcome to Blackjack!'}
```
Just returns a friendly message.

## create_game()
```
GET /game/create/{num_players: int}
returns: {'success': True, 'game_id': game_uuid, 'termination_password': the_password}
```
Asks the database object to create a new game `game_id`, then returns the UUID of the game in the `game_id` key and the password needed for termination in the `termination_password` key.

## init_game()
```
POST /game/{game_id}/initialize
returns: {'success': True, 'dealer_stack': dealer_stack, 'player_stacks': player_stacks}
```
Asks the database for the pointer to the game `game_id`, calls `initial_deal()` on the game, then returns the stacks (hands) from `get_stacks()` on the game.

## get_stacks()
```
GET /game/{game_id}/stacks
returns: {'success': True, 'dealer_stack': dealer_stack, 'player_stacks': player_stacks}
```
Asks the database for the pointer to the game `game_id`, then returns the stacks (hands) from `get_stacks()` on the game.

## player_hit()
```
POST /game/{game_id}/player/{player_idx}/hit
returns: {'player': player_idx, 'drawn_card': str(drawn_card), 'player_stack': player's stack}
```
Asks the database for the pointer to the game `game_id`, hits for the player `player_idx`, then returns the result of the hit and the new stack (hand).

## player_stack()
```
GET /game/{game_id}/player/{player_idx}/stack
returns: {'player': player_idx, 'player_stack': player's stack}
```
Returns the current stack (hand) of the player specified by `player_idx` in the game `game_id`.

## dealer_play()
```
POST /game/{game_id}/dealer/play
returns: {'player': 'dealer', 'player_stack': dealer's stack}
```
Plays the dealer (call `dealer_draw()` on the game until the dealer can stop), then return the dealer's hand.

## get_winners()
```
GET /game/{game_id}/winners
returns: {'game_id': game_id, 'winners': winner_list}
```
Computes the winners of game `game_id` using `compute_winners()`, then returns the winners.

## delete_game()
```
POST /game/{game_id}/terminate?password=...
returns: {'success': True, 'deleted_id': game_id}
```
Terminates the game `game_id` and authorizes the termination with the password provided as `password` query key.

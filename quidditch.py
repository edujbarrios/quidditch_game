import random
import time
import sys

class QuidditchGame:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.player1_position = (0, 0)
        self.player2_position = (0, 0)
        self.snitch_position = (0, 0)
		self.quaffle_position = (0, 0)
		self.bludger_position = (0, 0)
		
		
		#Exceptions
		if player_num == 1:
        player_position = self.player1_position
    elif player_num == 2:
        player_position = self.player2_position
    else:
        print("Invalid player number")
        return
		
		  self.controls = {
            'move_left': False,
            'move_right': False,
            'move_up': False,
            'move_down': False,
            'accelerate': False,
            'decelerate': False,
            'catch_quaffle': False,
            'shoot_quaffle': False,
            'dodge_bludger': False,
            'block_bludger': False,
        }
        
    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.controls['move_left'] = True
            elif event.key == pygame.K_RIGHT:
                self.controls['move_right'] = True
            elif event.key == pygame.K_UP:
                self.controls['move_up'] = True
            elif event.key == pygame.K_DOWN:
                self.controls['move_down'] = True
            elif event.key == pygame.K_SPACE:
                self.controls['accelerate'] = True
            elif event.key == pygame.K_LSHIFT:
                self.controls['decelerate'] = True
            elif event.key == pygame.K_c:
                self.controls['catch_quaffle'] = True
            elif event.key == pygame.K_x:
                self.controls['shoot_quaffle'] = True
            elif event.key == pygame.K_d:
                self.controls['dodge_bludger'] = True
            elif event.key == pygame.K_b:
                self.controls['block_bludger'] = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.controls['move_left'] = False
            elif event.key == pygame.K_RIGHT:
                self.controls['move_right'] = False
            elif event.key == pygame.K_UP:
                self.controls['move_up'] = False
            elif event.key == pygame.K_DOWN:
                self.controls['move_down'] = False
            elif event.key == pygame.K_SPACE:
                self.controls['accelerate'] = False
            elif event.key == pygame.K_LSHIFT:
                self.controls['decelerate'] = False
            elif event.key == pygame.K_c:
                self.controls['catch_quaffle'] = False
            elif event.key == pygame.K_x:
                self.controls['shoot_quaffle'] = False
            elif event.key == pygame.K_d:
                self.controls['dodge_bludger'] = False
            elif event.key == pygame.K_b:
                self.controls['block_bludger'] = False
		
	class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.score = 0
        
    def add_point(self):
        self.score += 1
		
	class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
		
		self.player_team = player_team
        self.teams = ["Griffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
        self.opponent_team = None
		self.grifindor = Team("Grifindor", [Player(f"Grifindor Player {i}", "Grifindor") for i in range(1,8)])
        self.slytherin = Team("Slytherin", [Player(f"Slytherin Player {i}", "Slytherin") for i in range(1,8)])
        self.hufflepuff = Team("Hufflepuff", [Player(f"Hufflepuff Player {i}", "Hufflepuff") for i in range(1,8)])
        self.ravenclaw = Team("Ravenclaw", [Player(f"Ravenclaw Player {i}", "Ravenclaw") for i in range(1,8)])
        self.teams = [self.grifindor, self.slytherin, self.hufflepuff, self.ravenclaw]
        self.quaffle = Quaffle(random.choice([(0,0), (0,1), (1,0), (1,1)]))
        self.bludger1 = Bludger(random.choice([(0,0), (0,1), (1,0), (1,1)]))
        self.bludger2 = Bludger(random.choice([(0,0), (0,1), (1,0), (1,1)]))
        self.snitch = Snitch(random.choice([(0,0), (0,1), (1,0), (1,1)]))
        self.current_team = self.grifindor
        self.other_team = self.slytherin
		
    def choose_opponent_team(self):
        self.opponent_team = random.choice([team for team in self.teams if team != self.player_team])
        return self.opponent_team

    print("Team: {0}".format(teams[selected_team]))
    action = input("Player {0}: (c)atch the snitch or (s)core a goal? ".format(player_num))
	
	def start_match(team1, team2):
    teams = [team1, team2]
    random.shuffle(teams)
    team1, team2 = teams

    # Create 7 players for each team
    team1_players = [Player(f"Player {i}", team1, (0, 0), random.randint(1, 3)) for i in range(1, 8)]
    team2_players = [Player(f"Player {i}", team2, (0, 0), random.randint(1, 3)) for i in range(1, 8)]

    # Assign players to teams
    team1.players = team1_players
    team2.players = team2_players
	
	
    
    def start(self):
        # initialize the positions of the players and the snitch
        self.player1_position = (random.randint(0, 10), random.randint(0, 10))
        self.player2_position = (random.randint(0, 10), random.randint(0, 10))
        self.snitch_position = (random.randint(0, 10), random.randint(0, 10))
		self.quaffle_position = (random.randint(0, 10), random.randint(0, 10))
		self.bludger_position = (random.randint(0, 10), random.randint(0, 10))
    
    def move_players(self):
        # simulate the movement of the players
        self.player1_position = (self.player1_position[0] + random.randint(-1, 1), 
                                 self.player1_position[1] + random.randint(-1, 1))
        self.player2_position = (self.player2_position[0] + random.randint(-1, 1), 
                                 self.player2_position[1] + random.randint(-1, 1))
    
    def move_snitch(self):
        # simulate the movement of the snitch
        self.snitch_position = (self.snitch_position[0] + random.randint(-1, 1), 
                                self.snitch_position[1] + random.randint(-1, 1)).
    
								
	 def move_quaffle(self):
        # simulate the movement of the Quaffle
        self.quaffle_position = (self.quaffle_position[0] + random.randint(-1, 1), 
                                 self.quaffle_position[1] + random.randint(-1, 1))
        
    def move_bludger(self):
        # simulate the movement of the Bludger
        self.bludger_position = (self.bludger_position[0] + random.randint(-1, 1), 
		self.bludger_position[1] + random.randint(-1, 1))
		
		
		
    def update_game_state(self):
        self.move_players()
        self.move_snitch()
		self.move_quaffle()
		self.move_bludger()
		input_key = get_input()
    if input_key == "p":
        if self.game_paused:
            self.resume_game()
        else:
            self.pause_game()
    else:
        self.handle_input(input_key)

	def display_game_state(self):
    grid = []
    for i in range(11):
        grid.append(["."] * 11)

    grid[0][0] = "G"
    grid[10][10] = "G"
    grid[self.snitch_position[0]][self.snitch_position[1]] = "S"
    grid[self.player1_position[0]][self.player1_position[1]] = "1"
    grid[self.player2_position[0]][self.player2_position[1]] = "2"

    # Add the quaffle (obstacle)
    grid[self.quaffle_position[0]][self.quaffle_position[1]] = "Q"
    
    # Add the bludger (obstacle)
    grid[self.bludger_position[0]][self.bludger_position[1]] = "B"

    print("   0 1 2 3 4 5 6 7 8 9 10")
    print("  -----------------------")
    for i, row in enumerate(grid):
        print("{0} |".format(i), end="")
        for item in row:
            print("{0} ".format(item), end="")
        print("|")
    print("  -----------------------")
    
    def handle_input(self, player_num):
        # handle user input for team 1 1 or team 2
        if player_num == 1:
            player_position = self.player1_position
        elif player_num == 2:
            player_position = self.player2_position
        else:
            print("Invalid player number")
            return
        
        action = input("Player {0}: (c)atch the snitch or (s)core a goal? ".format(player_num))
        
        if action == "c":
            if player_position == self.snitch_position:
                print("Player {0} caught the snitch!".format(player_num))
                if player_num == 1:
                    self.player1_score += 150
                elif player_num == 2:
                    self.player2_score += 150
            else:
                print("Player {0} missed the snitch...".format(player_num))
        elif action == "s":
            if player_position == (0, 0) or player_position == (10, 10):
                print("Player {0} scored a goal!".format(player_num))
                if player_num == 1:
                    self.player1_score += 10
                elif player_num == 2:
                    self.player2_score += 10
            else:
                print("Player {0} can't score from this position".format(player_num))
        else:
            print("Invalid action")
			
	if input_key == "w":
        # move player up
    elif input_key == "s":
        # move player down
    elif input_key == "a":
        # move player left
    elif input_key == "d":
			
		def display_score(team1, team2):
    print(f"{team1.name}: {team1.score}")
    print(f"{team2.name}: {team2.score}")
	

	def stop_game_after_time(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        update_game_state()
        display_game_state()
    print("El tiempo ha terminado.")
	
	def catch_snitch_with_time_limit(time_limit):
    start_time = time.time()
    while not game_over:
        update_game_state()
        display_game_state()
        if time.time() - start_time > time_limit:
            print("Se ha agotado el tiempo para atrapar la Snitch.")
            break
			
	def shoot_with_time_limit(team, time_limit):
    start_time = time.time()
    while time.time() - start_time < time_limit:
        update_game_state()
        display_game_state()
        if team.shoot():
            break
    print("Se ha agotado el tiempo para hacer un tiro a gol.")
	
			
	def play(self):
    self.start()
    while True:
        self.update_game_state()
        self.display_game_state()
        self.handle_input(1)
        self.handle_input(2)
        if self.player1_score >= 150 or self.player2_score >= 150:
            print("Player 1 score: {0}".format(self.player1_score))
            print("Player 2 score: {0}".format(self.player2_score))
            if self.player1_score > self.player2_score:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            break
			
	def pause_game(self):
    self.game_paused = True
    print("Juego pausado.")

	def resume_game(self):
    self.game_paused = False
    print("Juego reanudado.")

	def update_game(game state):
    if not self.game_paused:
		
	 # Update the positions of the players and the ball (Quaffle or Bludger)
	 
    for player in game_state["players"]:
		
        # Update the position of the player based on their velocity
        player["position"][0] += player["velocity"][0]
        player["position"][1] += player["velocity"][1]

        # Check if the player has caught the ball
        if is_collision(player["position"], game_state["ball"]["position"]):
            player["has_ball"] = True
            game_state["ball"]["holder"] = player
    
    # Check if a goal has been scored
    for goal in game_state["goals"]:
        if is_collision(game_state["ball"]["position"], goal["position"]):
            game_state["scored_goal"] = True
            game_state["ball"]["holder"] = None

def is_collision(player_position, object_position):
    # Check if the player has collided with an object (ball or goal)
    distance = ((player_position[0] - object_position[0]) ** 2 +
                (player_position[1] - object_position[1]) ** 2) ** 0.5
				return distance < COLLISION_DISTANCE
				
# Adding time control
def update_time(time_passed):
    global time_left
    time_left -= time_passed

# Adding score
def update_score(team):
    global score
    if team == "griffindor":
        score["griffindor"] += 10
    elif team == "slytherin":
        score["slytherin"] += 10
    elif team == "hufflepuff":
        score["hufflepuff"] += 10
    elif team == "ravenclaw":
        score["ravenclaw"] += 10

# Adding collision detection
def detect_collision(obstacle_x, obstacle_y, player_x, player_y):
    if abs(obstacle_x - player_x) < 50 and abs(obstacle_y - player_y) < 50:
        return True
    return False

# Adding speed control
def update_speed(player_speed, acceleration):
    player_speed += acceleration

# Adding sound effects
def play_sound(action):
    if action == "goal":
        # Play goal sound effect (take a personalized audio)
    elif action == "collision":
        # Play collision sound effect (take a personalized audio)
        
  def handle_input(self, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:  # Supongamos que la tecla para salir es Esc
            sys.exit()
			
	#Displays a Menú
	if __name__ == "__main__":
    game = QuidditchGame()
    teams = ["Griffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    print("Welcome to the Quidditch game!")
    print("Select your team:")
    for i, team in enumerate(teams):
        print("{0}: {1}".format(i, team))
    selected_team = int(input("Enter the number of your team: "))

    print("Starting the match...")
    game.start()
    while True:
        game.update_game_state()
        game.display_game_state()
        game.handle_input(1)	
			

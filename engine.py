import libtcodpy as libtcod

def main():
	screen_width = 80
	screen_height = 50

	player_x = int(screen_width / 2)
	player_y = int(screen_height / 2)

	key = libtcod.Key()
	mouse = libtcod.Mouse()

	libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD) #Takes the font from the image file and uses it in the console
	libtcod.console_init_root(screen_width, screen_height, "rougelike", False) #initalizes console with size and name (fullscreen set to false)
	con = libtcod.console_new(screen_width, screen_height) #lets me make new consoles later on

	while not libtcod.console_is_window_closed():
		libtcod.console_set_default_foreground(con, libtcod.white) 
		libtcod.console_put_char(con, player_x, player_y, '@', libtcod.BKGND_NONE) #writes the character at the cooridinates (1, 1)
		libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
		libtcod.console_flush() #show the console
		libtcod.console_put_char(con, player_x, player_y, ' ', libtcod.BKGND_NONE)
		
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

		action = handle_keys(key)
		move = action.get("move")
		exit = action.get("exit")
		fullscreen = action.get("fullscreen")


		if move: #moves the player
			dx, dy = move
			player_x += dx
			player_y += dy
		if exit: #exits the game
			return True
		if fullscreen: #fullscreen
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


def handle_keys(key): #putting keys into a dictonary (its debatable if this belongs in the engine, i could just put it in a sperate file for input handlers later)
	if key.vk == libtcod.KEY_UP: #movement
		return {"move" : (0, -1)}
	elif key.vk == libtcod.KEY_DOWN:
		return {"move" : (0, 1)}
	elif key.vk == libtcod.KEY_LEFT:
		return {"move" : (-1, 0)}
	elif key.vk == libtcod.KEY_RIGHT:
		return {"move" : (1, 0)}

	
	elif key.vk == libtcod.KEY_ESCAPE:#escape
		return {"exit" : True}
	elif key.vk == libtcod.KEY_TAB: #fullscreen
		return {"fullscreen" : True}

	return {} #No key is pressed


################################################################################################
if __name__ == "__main__":
	main()
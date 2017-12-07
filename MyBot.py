"""
Welcome to your first Halite-II bot!
This bot's name is Settler. It's purpose is simple (don't expect it to win complex games :) ):
1. Initialize game
2. If a ship is not docked and there are unowned planets
2.a. Try to Dock in the planet if close enough
2.b If not, go towards the planet
Note: Please do not place print statements here as they are used to communicate with the Halite engine. If you need
to log anything use the logging module.
"""
# Let's start by importing the Halite Starter Kit so we can interface with the Halite engine
import hlt
# Then let's import the logging module so we can print out information
import logging

# GAME START
# Here we define the bot's name as Settler and initialize the game, including communication with the Halite engine.
game = hlt.Game("Settler")
# Then we print our start message to the logs
logging.info("Starting my Settler bot!")

while True:
    # TURN START
    # Update the map for the new turn and get the latest version
    game_map = game.update_map()

    # Here we define the set of commands to be sent to the Halite engine at the end of the turn
    largest_planet = max(planet.radius for planet in game_map.all_planets())

    # Send our set of commands to the Halite engine for this turn
    command_queue = []
    planets = game_map.all_planets()
    ships = game_map.get_me().all_ships()

    for current in range(0, len(ships)):

        # entities_by_distance = game_map.nearby_entities_by_distance(ships[current])
        # nearest_planet = None
        # for distance in sorted(entities_by_distance):
        #     if nearest_planet.is_owned():
        #         continue
        #     else:
        #         nearest_planet = next((nearest_entity for nearest_entity in entities_by_distance[distance] if
        #                                isinstance(nearest_entity, hlt.entity.Planet)), None)

        if ships[current].can_dock(planets[current % len(planets)]):
            # if planets[current % len(planets)] == largest_planet:
            #     command_queue.insert(0, ships[current].dock(planets[current % len(planets)]))
            # else:
            command_queue.append(ships[current].dock(planets[current % len(planets)]))
        else:
            navigate_command = ships[current].navigate(ships[current].closest_point_to(planets[current % len(planets)]),
                                                        game_map,
                                                        speed=int(hlt.constants.MAX_SPEED),
                                                        ignore_ships=True)
            if navigate_command:
                command_queue.append(navigate_command)

        # #if ships[current].can_dock(nearest_planet):
        # command_queue.append(ships[current].dock(nearest_planet))
        # #elif navCommand:
        # #    command_queue.append(navCommand)

    game.send_command_queue(command_queue)
    # TURN END
# GAME END

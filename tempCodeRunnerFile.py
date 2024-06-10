      race_cars = []
            for individual in population.individuals:
                race_cars.append(Car(individual, INITIAL_X, INITIAL_Y))
        
        end_generation = False
        
        timer_var += 1/FPS
        timer_text = font.render(f'Time: {int(timer_var)}', True, (0, 0, 0))
        
        max_car = max(race_cars, key=lambda x: x.individual.fitness)
        
        for race_car in race_cars:
            if race_car != max_car:
                race_car.show_radar = False
        max_car.show_radar = True
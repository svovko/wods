

class Wendler:

    def __init__(self):
        self.cycle_count = 0
        self.week_count = -1
        self.day_count = -1
        self.workout_count = -1

        self.lifts = ['Deadlift', 'Bench press', 'Squat', 'Press']

        self.warmup_sets = [[30, 40, 50, 60],
                            [35, 45, 55, 65],
                            [40, 50, 60, 70],
                            [30, 40]]

        self.warmup_set_reps = [['10 x ', '8 x ', '6 x ', '4 x '],
                                ['10 x ', '8 x ', '6 x ', '4 x '],
                                ['10 x ', '8 x ', '6 x ', '4 x '],
                                ['10 x ', '8 x ']]

        self.main_sets = [[65, 75, 85],
                          [70, 80, 90],
                          [75, 85, 95],
                          [40, 50, 60]]

        self.main_set_reps = [['5 x ', '5 x ', '5+ x '],
                              ['3 x ', '3 x ', '3+ x '],
                              ['5 x ', '3 x ', '1+ x '],
                              ['5 x ', '5 x ', '5 x ']]

    def get_workout_name(self):
        return self.lifts[(self.day_count + 1) % 4]

    def get_workout(self):
        strength = []

        self.day_count += 1  # 0, 1, 2, 3, 4, 5, 6, 7, 8 ...

        if self.day_count % 4 == 0:  # start of a new week
            self.week_count += 1
            self.workout_count += 1
            self.day_count = 0

        if self.workout_count == 4:
            self.workout_count = 0

        if self.week_count + 1 == 5:  # start of a new cycle
            self.cycle_count += 1
            self.week_count = 0
            self.day_count = 0

        dlsq_inc = 5
        spbp_inc = 2.5

        str_inc = ''
        if self.cycle_count > 0:
            if self.day_count in [0, 2]:
                str_inc = ' + ' + str(dlsq_inc * self.cycle_count) + 'kg'
            else:
                str_inc = ' + ' + str(spbp_inc * self.cycle_count) + 'kg'

        for i in range(len(self.warmup_sets[self.workout_count])):
            strength.append(
                self.warmup_set_reps[self.workout_count][i] + str(self.warmup_sets[self.workout_count][i]) + '%' + str_inc)

        for i in range(len(self.main_sets[self.workout_count])):
            strength.append(
                self.main_set_reps[self.workout_count][i] + str(self.main_sets[self.workout_count][i]) + '%' + str_inc)

        return strength

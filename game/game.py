class Game:

    def __init__(self):
        self.end = False
        self.score = 0
        self.frames = []
        self.strikes = []
        self.spares = []
        self.points = [10, 3, 7, 6, 1, 10, 10, 10, 2, 8, 9, 0, 7, 3, 10, 10, 10]

    def run(self):
        frame_index = 0
        point_index = 0
        while frame_index < 10:
            self.frames.append({'points': [], 'frame_score': 0})
            self.process_point(frame_index, point_index)

            if self.points[point_index] == 10:
                self.strikes.append({'frame_index': frame_index, 'point_index': point_index})
            else:
                point_index += 1
                self.process_point(frame_index, point_index)
                if self.frames[frame_index]['points'][0] + self.frames[frame_index]['points'][1] == 10:
                    self.spares.append({'frame_index': frame_index, 'point_index': point_index})

            if len(self.frames) == 10:  # last frame
                self.end = True
                if len(self.strikes) or len(self.spares):
                    point_index += 1
                    self.process_point(frame_index, point_index)
                if len(self.strikes):
                    point_index += 1
                    self.process_point(frame_index, point_index)

            frame_index += 1
            point_index += 1

        for frame in self.frames:
            print(frame)

        print('Score: %s' % self.score)
        
    def process_point(self, frame_index, point_index):
        point = self.points[point_index]
        self.handler_strike(point, point_index)
        self.handler_spare(point, point_index)
        self.frames[frame_index]['points'].append(point)

        if not self.end:
            self.score += point
            self.frames[frame_index]['frame_score'] += point

    def handler_strike(self, point, point_index):
        for strike in self.strikes[:]:
            strike_end_index = strike['point_index'] + 2

            if strike_end_index >= point_index:
                self.score += point
                self.frames[strike['frame_index']]['frame_score'] += point
            else:
                self.strikes.remove(strike)

    def handler_spare(self, point, point_index):
        for spare in self.spares[:]:
            spare_end_index = spare['point_index'] + 1

            if spare_end_index >= point_index:
                self.score += point
                self.frames[spare['frame_index']]['frame_score'] += point
            else:
                self.spares.remove(spare)

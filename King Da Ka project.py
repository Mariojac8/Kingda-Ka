class Train:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.height = 0
        self.locked = False

    def load(self):
        print(self.name, 'is loading riders.')
        self.locked = True
        print('Safety restraints are locked.')

    def launch(self):
        if self.locked:
            self.speed = 128
            print('The train launches to 128 mph!')
        else:
        print('Cannot launch. Lock restraints first.')

    def rollback(self):
        print('ROLLBACK! The train does not make it over the top.')
        print('The train rolls backward and stops.')
        self.speed = 0
        self.height = 0

    def finish(self):
        self.height = 456
        print('The train reaches the top at 456 feet!')
        print('The train drops down the tower.')
        self.height = 0
        self.speed = 0
        print('The train brakes and stops.')


class KingdaKa:
    def __init__(self):
        self.train = Train('Kingda Ka Train')

    def run_ride(self, choice):
        self.train.load()
        self.train.launch()

        if choice == '2':
            self.train.rollback()
            print('The train is ready to try again.')
            self.train.launch()

        self.train.finish()
        print('Ride complete!\n')

    def start(self):
        print('Welcome to Kingda Ka!')
        while True:
            print('1. Normal ride')
            print('2. Ride with rollback')
            print('3. Exit')
            choice = input('Choose 1, 2, or 3: ').strip()

            if choice == '1' or choice == '2':
                self.run_ride(choice)
            elif choice == '3':
                print('Thanks for riding!')
                break
            else:
                print('Please enter 1, 2, or 3.\n')


if __name__ == '__main__':
    ride = KingdaKa()
    ride.start()

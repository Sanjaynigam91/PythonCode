class Pycharm:
    def execute(self):
        print('compiling')
        print("running")

class VSCode:
    def execute(self):
        print('compiling')
        print("running")
        print("Spell Checking")
        print("Suggestions")


class Laptop:
    def code(self,ide):
        ide.execute()

ide=VSCode()

lap=Laptop()
lap.code(ide)



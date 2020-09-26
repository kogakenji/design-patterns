class Installer():

    def __init__(self, src, root):
        self.choices = []
        self.root = root
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.root)
            else:
                print("No operation")
    

if __name__ == "__main__":
    installer = Installer('python3.8.gzip', '/usr/local/bin')
    installer.preferences({'python': True})
    installer.preferences({'java': False})
    installer.execute()
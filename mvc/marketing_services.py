class Model():
    services = {
        "email": {"number": 1000, "price": 2},
        "sms": {"number": 1000, "price": 10},
        "voice": {"number": 1000, "price": 15}
    }

class View():
    def list_services(self, services):
        for service in services:
            print(service)
    
    def list_prices(self, services):
        for service in services:
            print(f"For {Model.services[service]['number']}, message you pay $ {Model.services[service]['price']}")

class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_services(self):
        services = self.model.services.keys()
        return(self.view.list_services(services))

    def get_pricing(self):
        services = self.model.services.keys()
        return(self.view.list_prices(services))

class Client():
    controller = Controller()
    print("Services provided:")
    controller.get_services()
    print("Pricing for Services:")
    controller.get_pricing()

if __name__ == "__main__":
    client = Client()

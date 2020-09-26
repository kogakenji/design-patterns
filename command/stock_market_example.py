from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    """
    Command object: offers an interface for Concrete command to implement behaviour
    execute() method will be defined by Concrete command classes
    """


    @abstractmethod
    def execute(self):
        pass


class BuyStockOrder(Order):
    """
    Concrete command to execute buy order
    """
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    """
    Concrete command to execute sell order
    """
    def __init__(self, stock):
        self.stock = stock
    
    def execute(self):
        self.stock.sell()


class StockTrade:
    """
    Receiver object which defines actions to execute requests represented by
    Concrete commander objects. The buy and sell methods are called by BuyStockOrder
    and SellStockOrder to buy and sell stocks in the stockmarket.
    """
    def buy(self):
        print("Buy stock")
    
    def sell(self):
        print("Sell stock")


class Agent:
    """
    Caller class. This is the intermediate between the client and the stockmarket
    Executes the requests from the client stored in a list.
    """

    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()


if __name__ == "__main__":
    # Client
    stock = StockTrade()
    buystock = BuyStockOrder(stock)
    sellstock = SellStockOrder(stock)

    # Caller
    agent = Agent()
    agent.placeOrder(buystock)
    agent.placeOrder(sellstock)
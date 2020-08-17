#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ticket_table = {}
    for ticket in tickets:
        ticket_table[ticket.source] = ticket.destination
    destination = ticket_table["NONE"]
    route = []
    while destination != None:
        route.append(destination)
        if destination == "NONE":
            destination = None
        else:
            destination = ticket_table[destination]
    return route

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

tickets = [
    Ticket( "PIT", "ORD" ),
    Ticket( "XNA", "CID"),
    Ticket( "SFO", "BHM"),
    Ticket( "FLG", "XNA"),
    Ticket( "NONE", "LAX"),
    Ticket( "LAX", "SFO"),
    Ticket( "CID", "SLC"),
    Ticket( "ORD", "NONE"),
    Ticket( "SLC", "PIT"),
    Ticket( "BHM", "FLG")
]

print(reconstruct_trip(tickets, 10))
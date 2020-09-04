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
    tickets_dict = {ticket.source: ticket.destination for ticket in tickets}
    route = [tickets_dict['NONE']]
    for i in range(1, length):
        route.append(tickets_dict[route[i-1]])

    return route

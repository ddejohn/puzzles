from enum import Enum
from typing import List


class Events(Enum):
    APP_PASSIVE_OPEN = 1
    APP_ACTIVE_OPEN = 2
    APP_SEND = 3
    APP_CLOSE = 4
    APP_TIMEOUT = 5
    RCV_SYN = 6
    RCV_ACK = 7
    RCV_SYN_ACK = 8
    RCV_FIN = 9
    RCV_FIN_ACK = 10


class States(Enum):
    CLOSED = 1
    LISTEN = 2
    SYN_SENT = 3
    SYN_RCVD = 4
    ESTABLISHED = 5
    CLOSE_WAIT = 6
    LAST_ACK = 7
    FIN_WAIT_1 = 8
    FIN_WAIT_2 = 9
    CLOSING = 10
    TIME_WAIT = 11


transitions = {
    (States.CLOSED,         Events.APP_PASSIVE_OPEN):   States.LISTEN,
    (States.CLOSED,         Events.APP_ACTIVE_OPEN):    States.SYN_SENT,
    (States.LISTEN,         Events.RCV_SYN):            States.SYN_RCVD,
    (States.LISTEN,         Events.APP_SEND):           States.SYN_SENT,
    (States.LISTEN,         Events.APP_CLOSE):          States.CLOSED,
    (States.SYN_RCVD,       Events.APP_CLOSE):          States.FIN_WAIT_1,
    (States.SYN_RCVD,       Events.RCV_ACK):            States.ESTABLISHED,
    (States.SYN_SENT,       Events.RCV_SYN):            States.SYN_RCVD,
    (States.SYN_SENT,       Events.RCV_SYN_ACK):        States.ESTABLISHED,
    (States.SYN_SENT,       Events.APP_CLOSE):          States.CLOSED,
    (States.ESTABLISHED,    Events.APP_CLOSE):          States.FIN_WAIT_1,
    (States.ESTABLISHED,    Events.RCV_FIN):            States.CLOSE_WAIT,
    (States.FIN_WAIT_1,     Events.RCV_FIN):            States.CLOSING,
    (States.FIN_WAIT_1,     Events.RCV_FIN_ACK):        States.TIME_WAIT,
    (States.FIN_WAIT_1,     Events.RCV_ACK):            States.FIN_WAIT_2,
    (States.CLOSING,        Events.RCV_ACK):            States.TIME_WAIT,
    (States.FIN_WAIT_2,     Events.RCV_FIN):            States.TIME_WAIT,
    (States.TIME_WAIT,      Events.APP_TIMEOUT):        States.CLOSED,
    (States.CLOSE_WAIT,     Events.APP_CLOSE):          States.LAST_ACK,
    (States.LAST_ACK,       Events.RCV_ACK):            States.CLOSED
}


def traverse_TCP_states(events: List[str]) -> str:
    state = States["CLOSED"]
    for event in events:
        state = transitions.get((state, Events[event]), "ERROR")
        if state == "ERROR":
            return state
    return state.name


print(traverse_TCP_states(["APP_ACTIVE_OPEN"]), "SYN_SENT")

print(traverse_TCP_states(["APP_ACTIVE_OPEN",
                           "RCV_SYN_ACK",
                           "RCV_FIN"]), "CLOSE_WAIT")

print(traverse_TCP_states(["APP_PASSIVE_OPEN",
                           "RCV_SYN",
                           "RCV_ACK"]), "ESTABLISHED")

print(traverse_TCP_states(["APP_ACTIVE_OPEN",
                           "RCV_SYN_ACK",
                           "RCV_FIN",
                           "APP_CLOSE"]), "LAST_ACK")

print(traverse_TCP_states(["APP_PASSIVE_OPEN",
                           "RCV_SYN",
                           "RCV_ACK",
                           "APP_CLOSE",
                           "APP_SEND"]), "ERROR")

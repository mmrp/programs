#!/usr/bin/python

def shortener(message):
    newmsg = message.split()[::-1]
    msglen = len(message)

    cwords = msglen - 160
    if cwords > 0:
        for p,v in enumerate(newmsg):
            newmsg[p] = v[0].upper() + v[1:]
            cwords -= 1
            if cwords == 0:
                break
    msg = newmsg[::-1]
    if p > 0:
        p    = len(msg) - p
        return ' '.join(msg[0:p-1]) + ''.join(msg[p-1:])
    else:
        return ' '.join(msg)


print shortener("No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! And that will be it.")





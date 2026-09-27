def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30, 
                           requestsPerConnection=100,
                           pipeline=False,
                           engine=Engine.THREADED
                           )

    # Correctly loops and queues the intercepted request (target.req)
    for i in range(1000):
        engine.queue(target.req)

def handleResponse(req, interesting):
    # Correctly adds the request results back to the Burp UI table
    table.add(req)

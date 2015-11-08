#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 5 """

import csv
import argparse
import urllib2


url_parser = argparse.ArgumentParser()
url_parser.add_argument("--file", help='enter url ', type=str)
url_parser.add_argument("--servers", type=int, help="number of servers")
args = url_parser.parse_args()


class Queue(object):

    def __init__(self):
        self.items = []

    def ifempty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Server(object):

    def __init__(self, name):
        self.name = name
        self.currentrequest = None
        self.timeremaining = 0

    def tick(self):

        if self.currentrequest != None:
            self.timeremaining -= 1

            if self.timeremaining <= 0:
                self.currentrequest = None

    def busy(self):

        if self.currentrequest != None:
            return True
        else:
            return False

    def startnext(self, newrequest):

        self.currentrequest = newrequest
        self.timeremaining = newrequest.get_processingtime()



class Request(object):

    def __init__(self, request):
        self.timestamp = time
        self.get_processingtime = processingtime

    def get_stamp(self):
        return self.timestamp

    def get_processtime(self):
        return self.processingtime

    def wait_time(self, current_sec):
        return current_sec - self.timestamp


def simulateOneServer(filerequested):

    server = Server()
    queue = Queue()

    request_dict = {}
    waiting_times = []


    for r in filerequested:
        newSec = int(r[0])
        queue.enqueue(r)

        if upsec in requestdict:
            request_dict[upsec].append(r)
        else:
            request_dict[upsec] = [r]

    for cursec in request_dict:
        for r in request_dict[cursec]:
            r(req)
            queue.dequeue()


        if (not server.busy()) and (not queue.isEmpty()):
            comreq = Request(queue.dequeue())
            waiting_times.append(comreq.wait_Time(comreq))
            server.startNext(comreq)

        server.tick()

    wait_average =sum(waiting_times)/float(len(waiting_times))
    print("Average Wait %6.2f secs for %3d requests"%(wait_average,len(waiting_times)))


def simulateManyServers(filerequested, server_num):

    servers = Server()
    queue = Queue()

    coreq = 1
    request_dict = {}
    waiting_times = []


    for cursec, frequest in filerequested.iteritems():

        for r in frequest:
            timestamp = int(r[0])
            processingtime = int(r[2])

            request = Request(coreq, timestamp, processingtime)
            queue.enqueue(request)
            coreq += 1

        for s in servers:
            if (not s.busy()) and (not queue.is_empty()):
                comreqe = Request(queue.dequeue())
                waiting_times.append(comreqe.wait_Time(cursec))
                servers.startNext(comreqe)

            server.tick()

    wait_average =sum(waiting_times)/float(len(waiting_times))
    print("Average Wait %6.2f secs for %3d requests"%(wait_average,len(waiting_times.Queue.server_num())))

def main():

    if args.file:

        filereq = csv.reader(urllib2.urlopen(args.file))
        simulateOneServer(filereq)

    else:
        filereq = csv.reader(urllib2.urlopen(args.file))

        simulateManyServers(filereq, int(args.servers))


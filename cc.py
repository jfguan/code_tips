import math
import os
import random
import re
import sys

import heapq
TIME = 0
CLIENT_ID = 1
DIRECTION = 2
SIZE = 3
TYPE = 4
PRICE = 5

buyHeap = []
sellHeap = []

# Custom order comparator first by price, second by time
class BuyOrder(object):
    def __init__(self, info):
        self.info = info

    def __lt__(self, other):
        condOne = self.info[PRICE] > other.info[PRICE]
        condTwo = self.info[PRICE] == other.info[PRICE] and self.info[TIME] < other.info[TIME]
        return condOne or condTwo

class SellOrder(object):
    def __init__(self, info):
        self.info = info

    def __lt__(self, other):
        condOne = self.info[PRICE] < other.info[PRICE]
        condTwo = self.info[PRICE] == other.info[PRICE] and self.info[TIME] < other.info[TIME]
        return condOne or condTwo

# Record the order in the orderbook
def recordOrders(info: list):
    if(info[DIRECTION] == 'b'):
        heapq.heappush(buyHeap, BuyOrder(info))
    elif(info[DIRECTION] == 's'):
        heapq.heappush(sellHeap, SellOrder(info))
    else:
        print("Error in order direction")

def execOrder(priceTraded, info, bot, direction):
    sizeTraded = min(info[SIZE], bot.info[SIZE])
    info[SIZE] -= sizeTraded
    bot.info[SIZE] -= sizeTraded
    if(direction == 'b'):
        print(info[TIME], info[CLIENT_ID], bot.info[CLIENT_ID], priceTraded, sizeTraded)
    elif(direction == 's'):
        print(info[TIME], bot.info[CLIENT_ID], info[CLIENT_ID], priceTraded, sizeTraded)

def solve():
    sys.stdin.readline().strip()

    for line in sys.stdin:
        info = line.split()
        info[SIZE] = int(info[SIZE])
        info[PRICE] = float(info[PRICE])
        # Fill the order if possible
        if(info[DIRECTION] == 'b'):
            while(len(sellHeap) > 0 and info[SIZE] > 0):
                # Lowest limit sell order on the sell heap
                bot = sellHeap[0]
                if(info[TYPE] == 'm'):
                    priceTraded = bot.info[PRICE]
                    execOrder(priceTraded, info, bot, info[DIRECTION])
                elif(info[PRICE] >= bot.info[PRICE]):
                    priceTraded = min(info[PRICE], bot.info[PRICE])
                    execOrder(priceTraded, info, bot, info[DIRECTION])
                else:
                    break
                if(bot.info[SIZE] == 0):
                    heapq.heappop(sellHeap)

        elif(info[DIRECTION] == 's'):
            while(len(buyHeap) > 0 and info[SIZE] > 0):
                # Highest limit buy order on the buy heap
                top = buyHeap[0]
                if(info[TYPE] == 'm'):
                    priceTraded = top.info[PRICE]
                    execOrder(priceTraded, info, top, info[DIRECTION])
                elif(info[PRICE] >= top.info[PRICE]):
                    priceTraded = min(info[PRICE], top.info[PRICE])
                    execOrder(priceTraded, info, top, info[DIRECTION])
                else:
                    break
                if(top.info[SIZE] == 0):
                    heapq.heappop(buyHeap)

        # Record unfilled limit orders, cancel market orders
        if (info[SIZE] != 0 and info[TYPE] == 'l'):
            recordOrders(info)
            
if __name__ == '__main__':
    solve()

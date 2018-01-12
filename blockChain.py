#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by ziqi on 12/1/2018
# This the blockChain script in the tryBlockChain project.
import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timeStamp, data, previousHash ):
        '''

        :param index: the index of this block in the BlockChain system
        :param timestanp: the time that this block created
        :param data: the data that this block stored
        :param previousHash: the hash value of the last block
        '''
        self.index = index
        self.timeStamp = timeStamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.hashBlock()

    def hashBlock(self):
        '''

        :return: the hash value of this block
        '''
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timeStamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previousHash).encode('utf-8'))
        return sha.hexdigest()

    def message(self):
        '''

        :return: a str object, the message from this block
        '''
        return("Hey! I'm block" + str(self.index))



class Chain:
    def __init__(self, initData, name):
        '''

        :param initData: the data stored in the genesis block
        :param name: the name of this BlockChain system
        '''
        self.blockChain = [self._CreateGenesisBlock(initData)]
        self.length = 1
        self.createTime = date.datetime.now()
        self.description = ""
        self.name = name

        print(f"A new BlockChain system {self.name} has been created!")
        print(f"The hash of this genesis block is {self.blockChain[0].hash}")
        print(f"The genesis block says: {self.blockChain[0].message()}")
        print(f"The data it includes: {self.blockChain[0].data}")
        print("\n")

    def _CreateGenesisBlock(self, initData):
        '''

        :return: a genesis block
        '''
        return Block(0, date.datetime.now(), initData, "0")

    def addNewBlock(self, data):
        '''

        :return: add a new block to the blockchain
        '''
        if self.thereIsNewBlock():
            lastBlock = self.blockChain[-1]

            thisIndex = lastBlock.index + 1
            thisTimeStamp = date.datetime.now()
            thisData = data
            lastHash = lastBlock.hash

            thisBlock = Block(thisIndex, thisTimeStamp, thisData, lastHash)
            self.blockChain.append(thisBlock)
            self.length += 1

            print(f"Block #{thisBlock.index} has been added to the {self.name} at {thisBlock.timeStamp}")
            print(f"The hash of this new block is {thisBlock.hash}")
            print(f"This block says: {thisBlock.message()}")
            print(f"The data it includes: {thisBlock.data}")
            print("\n")

    def thereIsNewBlock(self):
        '''

        :return: examine if there should be a new block
        '''
        return True

    def isLegal(self):
        '''

        :return: examine if this chaine is logal
        '''

        for block in self.blockChain:

            if block.hashBlock() != block.hash:
                print(f"Ooops! the data in {self.name} system has been changed!")
                print(f"The hash value cannot match the data in #{block.index} block!")
                return False

            if block.index > 0:
                lastBlock = self.blockChain[block.index-1]
                if lastBlock.hash != block.previousHash:
                    print(f"Ooops! the data in {self.name} system has been changed.")
                    print(f"The previousHash value in #{block.index} block is different from the hash value in the last block!!")
                    return False

        print(f"The {self.name} BlockChain system is legal. The data is safe.")
        return True

if __name__ == '__main__':

    zzChain = Chain("hello world!", "zzChain")

    for i in range(10):
        zzChain.addNewBlock("1")

    zzChain.isLegal()


    zzChain.blockChain[5].data = 2
    zzChain.isLegal()
    
    pass
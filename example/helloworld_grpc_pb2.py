# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: helloworld.proto
# plugin: asyncgrpc.plugin.main
from abc import ABCMeta, abstractmethod

from asyncgrpc.server import Method

import helloworld_pb2


class Greeter(metaclass=ABCMeta):

    @abstractmethod
    async def SayHello(self, request, context):
        pass

    def __mapping__(self):
        return {
            '/helloworld.Greeter/SayHello': Method(
                self.SayHello,
                helloworld_pb2.HelloRequest,
                helloworld_pb2.HelloReply,
            ),
        }

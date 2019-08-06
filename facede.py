# _*_ coding=utf-8 _*_


"""
外观模式：为子系统中的一组接口提供一个一致的界面。
        外观模式提供了一个高层接口，这个接口使得子系统更加容易的调用。
"""


class CPU:
    def run(self):
        print("CPU is running....")

    def stop(self):
        print("CPU is stopping...")


class Memory:
    def run(self):
        print("Memory is running...")

    def stop(self):
        print("Memory is stopping...")


class Disk:

    def run(self):
        print("Disk is running...")

    def stop(self):
        print("Disk is stopping...")


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


computer = Computer()
computer.run()


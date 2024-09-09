from models.command import Command
from command_factory import CommandFactory
class ParkingStratergy():
    
    def execute(self,input):
        command = Command(input)
        command_name = command.get_name()
        command_args = command.get_params()
        CommandFactory(command_name,command_args)
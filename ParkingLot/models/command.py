class Command():
    name = None
    args = []
    
    def get_name(self):
        return self.name
    
    def get_params(self):
        return self.args
    
    def __init__(self,command) -> None:
        command_split_list = command.split(" ")
        if len(command_split_list)<=0:
            raise ("The command is invalid")
        
        self.name = command_split_list[0]
        command_split_list.pop(0)
        self.args= command_split_list
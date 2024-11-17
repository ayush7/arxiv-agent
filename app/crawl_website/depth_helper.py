
class DepthKeeper:
    def __init__(self, depth_limit=2) -> None:
        self.current_depth = 1
        self.depth_limit = depth_limit
    
    def increment_depth(self):
        self.current_depth = self.current_depth  + 1
    
    def check_depth(self):
        """
        Returns True or False to send a signal to continue crawling
        """
        if self.current_depth <= self.depth_limit:
            return True 
        else:
            return False 
        
    
    
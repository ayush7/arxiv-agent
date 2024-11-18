import badmouth_professor, daily_report_agent, post_writer_agent, summarizer_agent

"""
When initializing the model, either -> 
Pass: [1,2,3,4] 

OR

["summarizer", "daily report", "post writer", "badmouth"]
The numbers correspond to the order

"""

class Agents:
    def __init__(self, agents = []) -> None:
        self.agents = agents 
        
        if 1 in agents or "summarizer" in agents:
            self.sum_agent = True
        else:
            self.sum_agent = False

        if 2 in agents or "daily report" in agents:
            self.daily_agent = True
        else:
            self.daily_agent = False

        if 3 in agents or "post writer" in agents:
            self.post_agent = True
        else:
            self.post_agent = False

        if 4 in agents or "badmouth" in agents:
            self.bad_agent = True
        else:
            self.bad_agent = False


    def run_post_writer(self, data):
        pass 


    def run_summary(self, data):
        pass 


    def run_badmouth(self, data):
        pass 
    

    def run_singular_agents(self, data):
        """
        Runs agents that only depend on single pdf file
        """
        pass 


    def run_agents(self, data_singulars, data_all):
        """
        Runs all agents
        """
        pass 

        
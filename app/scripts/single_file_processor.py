"""
Gets the link to an arxiv paper, parses and performs agentic hoobadoo and saves results.
"""
from pdf_parser import download_pdf, parse_pdf
import os 
import uuid
from agents import invoke_agents
import json
from pathlib import Path



class ArxivLinkProcessor:
    def __init__(self, arxiv_link=None, 
                 auto_run = True, 
                 delete_downloaded_files=False, 
                 save_parsed_data = True,
                 parsed_data_dir = '.parsed_data',
                 agents = [1,3,4]) -> None:
        # check validity of link 
        self.arxiv_link = arxiv_link
        self.valid = self.check_validity_of_link()
        self.delete_downloaded_files = delete_downloaded_files
        if auto_run and self.valid:
            self.invoke()
        self.agent_obj = invoke_agents.Agents(agents=agents)
        self.save_parsed_data = save_parsed_data
        self.parsed_data_dir = parsed_data_dir

    
    def check_validity_of_link(self):
        validity = download_pdf.is_arxiv_pdf(self.arxiv_link)
        return validity

    def invoke(self):
        if self.check_validity_of_link(self.arxiv_link) == False:
            print(f"The Link is Invalid : {self.arxiv_link}")
            return ValueError 


        # Download PDF
        file = download_pdf.download_arxiv_pdf(self.arxiv_link)
        if file == None:
            print(f"Error in downloading pdf : {self.arxiv_link}")
            return ValueError
        
        # Parse PDF 
        parsed_data = parse_pdf.parse_pdf(file)

        # Save parsed Data
        if self.save_parsed_data:
            file_name = uuid.uuid4()
            file_path = os.path.join(self.parsed_data_dir, file_name) + '.json'
            Path(self.parsed_data_dir).mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(parsed_data,f, indent=4)




        # Run agents
        agents_outputs = self.agent_obj.run_singular_agents(data=parsed_data["mega_chunk"])



        # Delete Downloaded File
        if os.path.exists(file):
            os.remove(file)


        # Save Agents outputs


        return agents_outputs
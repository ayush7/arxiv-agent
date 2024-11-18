# arxiv-agent
LLM Based Agent to scrape recent AI developments from arxiv and summarize the latest research
<br>
A LLM based crawler/scraper for Arxiv to read the latest papers from arxiv.org and give a briefing for each new paper.


## TO-DO
- [x] Website Scraper
- [x] PDF Links Extraction
- [x] PDF scraper
- [x] Support OpenAI calls
- [x] Support Gemini calls
- [x] Support Anthropic/Claude
- [ ] :question: Modifiable depth for crawler - Might not be needed as arxiv presents all newly released papers in a single page
- [x] Module for single Link Processing
- [ ] Agents - From ground UP
    - [ ] :exclamation: Base structure
    - [ ] summarizer
    - [ ] post_writer 
    - [ ] daily report
    - [ ] badmouth professor
- [ ] Agents - Add CrewAI agents and experiment with it some of their tools
    - [ ] summarizer
    - [ ] post_writer 
    - [ ] daily report
    - [ ] badmouth professor
- [x] :question: Enable Local Models with Ollama - Partially done. Base code written - add prompt completion formats
- [ ] Create Internal API
- [ ] GUI - Maybe with streamlit
- [ ] Dockerize 


* Maybe do this too 
- [ ] Add TTS with Cartesia API 
- [ ] Persistent RAG database with classic RAG techniques
- [ ] Advanced RAG implementation with Colpali and GraphRAG 
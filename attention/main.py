import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hyperon import MeTTa
from agents.scheduler import ParallelScheduler
from agents.agent_base import AgentObject

def main():
    metta = MeTTa()

    scheduler = ParallelScheduler(metta)
    
    # List of available agents and their path
    # agent_configs = [
    #     ("AFImportanceDiffusionAgent", "../metta-attention/attention/agents/mettaAgents/ImportanceDiffusionAgent/AFImportanceDiffusionAgent/AFImportanceDiffusionAgent-runner.metta"),
    #     ("WAImportanceDiffusionAgent", "../metta-attention/attention/agents/mettaAgents/ImportanceDiffusionAgent/WAImportanceDiffusionAgent/WAImportanceDiffusionAgent-runner.metta"),
    #     ("AFRentCollectionAgent", "../metta-attention/attention/agents/mettaAgents/RentCollectionAgent/AFRentCollectionAgent/AFRentCollectionAgent-runner.metta"),
    #     ("WARentCollectionAgent", "../metta-attention/attention/agents/mettaAgents/RentCollectionAgent/WARentCollectionAgent/WARentCollectionAgent-runner.metta"),
    #     ("HebbianUpdatingAgent", "../metta-attention/attention/agents/mettaAgents/HebbianUpdatingAgent/HebbianUpdatingAgent-runner.metta"),
    #     ("ForgettingAgent", "../metta-attention/attention/agents/mettaAgents/ForgettingAgent/ForgettingAgent-runner.metta"),
    # ]


    # Register agents
    print("\nRegistering agents...")

    # Looping through the list of tuples to register and run agents in the schduler
    # for agent_name, path in agent_configs:
    #     scheduler.register_agent(agent_name, lambda p = path: AgentObject(metta=metta, path = p))

    
    


    scheduler.register_agent("AFImportanceDiffusionAgent", 
        lambda: AgentObject(metta=metta, path="../metta-attention/attention/agents/mettaAgents/ImportanceDiffusionAgent/AFImportanceDiffusionAgent/AFImportanceDiffusionAgent-runner.metta"))
    scheduler.register_agent("WAImportanceDiffusionAgent", 
            lambda: AgentObject(metta=metta, path="../metta-attention/attention/agents/mettaAgents/ImportanceDiffusionAgent/WAImportanceDiffusionAgent/WAImportanceDiffusionAgent-runner.metta"))
    scheduler.register_agent("AFRentCollectionAgent", 
        lambda: AgentObject(metta=metta, path="../metta-attention/attention/agents/mettaAgents/RentCollectionAgent/AFRentCollectionAgent/AFRentCollectionAgent-runner.metta"))
    scheduler.register_agent("WARentCollectionAgent", 
        lambda: AgentObject(metta=metta, path="../metta-attention/attention/agents/mettaAgents/RentCollectionAgent/WARentCollectionAgent/WARentCollectionAgent-runner.metta"))
    scheduler.register_agent("HebbianUpdatingAgent", 
        lambda: AgentObject(metta=metta, path="../metta-attention/attention/agents/mettaAgents/HebbianUpdatingAgent/HebbianUpdatingAgent-runner.metta"))
    scheduler.register_agent("ForgettingAgent", 
        lambda: AgentObject(metta=metta, path="../metta-attention/attention/agents/mettaAgents/ForgettingAgent/ForgettingAgent-runner.metta"))
    

    print("\nAgent System Ready!")

    # No need of while loop here and not recommedned the following print statement to enter the try block
    print("\nRunning agents in continuous mode. Press Ctrl+C to stop.")
    while True:
        try:
            scheduler.run_continuously()
        except KeyboardInterrupt:
            print("\nReceived interrupt signal. Stopping system...")

        except Exception as e:
            print(f"\n Error: {e}")

        finally:
            print("System stopped. Goodbye!")

if __name__ == "__main__":
    main()
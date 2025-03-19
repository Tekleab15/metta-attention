import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hyperon import MeTTa
from agents.scheduler import ParallelScheduler
from agents.agent_base import AgentObject

def main():
    metta = MeTTa()

    scheduler = ParallelScheduler(metta)

    base_dir = os.path.abspath(os.path.dirname(__file__))
    
    # List available agents with absolute paths

    agent_configs = [
        ("AFImportanceDiffusionAgent", os.path.join(base_dir, "agents", "mettaAgents", "ImportanceDiffusionAgent", "AFImportanceDiffusionAgent", "AFImportanceDiffusionAgent-runner.metta")),
        ("WAImportanceDiffusionAgent", os.path.join(base_dir, "agents", "mettaAgents", "ImportanceDiffusionAgent", "WAImportanceDiffusionAgent", "WAImportanceDiffusionAgent-runner.metta")),
        ("AFRentCollectionAgent", os.path.join(base_dir, "agents", "mettaAgents", "RentCollectionAgent", "AFRentCollectionAgent", "AFRentCollectionAgent-runner.metta")),
        ("WARentCollectionAgent", os.path.join(base_dir, "agents", "mettaAgents", "RentCollectionAgent", "WARentCollectionAgent", "WARentCollectionAgent-runner.metta")),
        ("HebbianUpdatingAgent", os.path.join(base_dir, "agents", "mettaAgents", "HebbianUpdatingAgent", "HebbianUpdatingAgent-runner.metta")),
        ("ForgettingAgent", os.path.join(base_dir, "agents", "mettaAgents", "ForgettingAgent", "ForgettingAgent-runner.metta")),
    ]

    # Register agents
    print("\nRegistering agents...")

    # Looping through the list of tuples to register and run agents in the schduler
    for agent_name, path in agent_configs:
        if not os.path.isfile(path):
            print(f"Warning: File not found for agent {agent_name}: {path}")
        scheduler.register_agent(agent_name, lambda p = path: AgentObject(metta=metta, path = p))

    print("\nAgent System Ready!")

    # No need of while loop here and not recommedned the following print statement to enter the try block
    print("\nRunning agents in continuous mode. Press Ctrl+C to stop.")

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
# api_key: str, llm_id: str, voice_id: str
from retell import Retell

def create_retell_agent():
    try:
        client = Retell(api_key="key_aa3f852d528b7e9d451db22c1d1a")

        agent_response = client.agent.create(
            response_engine={
                "llm_id": "llm_c68f80a279496fbc4f294aacf6f4",
                "type": "retell-llm",
            },
            voice_id="play-Andrew"
        )
        print("Agent created successfully!")
        print("Agent ID:", agent_response.agent_id)
        return agent_response

    except Exception as e:
        print("Failed to create agent:")
        print(e)
        return None



from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

# Reload the environment variables with override
load_dotenv(override=True)

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_organization = os.getenv("OPENAI_ORGANIZATION")

# Debugging environment variables
print(f"OPENAI_API_KEY: {openai_api_key}")
print(f"OPENAI_ORGANIZATION: {openai_organization}")

def generate_company_name():
    try:
        # Initialize the ChatOpenAI with API key and organization
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            openai_api_key=openai_api_key,
            openai_organization=openai_organization,
        )

        # Generate company names
        company_name = llm(
            [
                SystemMessage(
                    content="Você é um assistente IA que sempre responde em Português do Brasil"
                ),
                HumanMessage(
                    content="Gere 5 ideias de nomes para empresas no segmento Pets"
                ),
            ]
        )

        return company_name

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print(generate_company_name())

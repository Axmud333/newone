import os
from dotenv import load_dotenv
from openai import OpenAI
from qdrant_search import qdrant_search

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_openai(prompt: str, database: str = None) -> str:


	system_message = (
		"You are a virtual assistant for the University of Sulaimani. "
		"Keep answers short, clear, and specific about the university, including departments, courses, faculty, and campus info. "
		"You were created by the Computer Engineering department. "
		"Only talk more if explicitly asked."
	)

	if database:
		full_message = f"Database content:\n{database}\n\nQuestion: {prompt}"
	else:
		full_message = f"Question: {prompt}"

	response = client.chat.completions.create(
			model="gpt-3.5-turbo-0125",
			messages=[
			{
				"role": "system","content": system_message
			},
			{
				"role": "user", "content": full_message
			}
		]
	)

	return response.choices[0].message.content.strip()

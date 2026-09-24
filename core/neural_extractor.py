import os
import json
import time
from typing import Optional
from dotenv import load_dotenv
from core.dsl_schema import ContractAST

load_dotenv()

EXTRACTION_SYSTEM_INSTRUCTION = """You are an expert Formal Methods and Neuro-Symbolic AI Engineer specializing in Financial Contracts and Credit Agreements.
Your task is to analyze legal contract text and compile it into a formal Intermediate Representation (ContractAST) for verification by an SMT solver (Z3).

For each financial or temporal condition:
1. Identify all numerical variables, states, and metrics (e.g. 'total_debt', 'ebitda', 'interest_expense', 'notice_days', 'cure_days', 'is_acquisition').
2. Parse each covenant/clause into a clean, well-formed mathematical formula (e.g. 'total_debt / ebitda <= 3.5' or 'cure_days >= 15').
3. Formulate the core Legal Invariants that must logically hold to avoid default loops, contradictory caps, or impossible covenants.
4. Output strictly according to the provided JSON schema.
"""

class NeuralContractExtractor:
    """Extracts formal ContractAST from natural language legal contracts using Gemini API."""

    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-2.5-flash"):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model_name = model_name or os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        self.client = None

        if self.api_key and self.api_key != "your_gemini_api_key_here":
            try:
                from google import genai
                self.client = genai.Client(api_key=self.api_key)
            except Exception as e:
                print(f"[NeuralExtractor] Error initializing Google GenAI Client: {e}")

    def extract_ast(self, contract_text: str, max_retries: int = 3) -> ContractAST:
        """Calls Gemini API with structured Pydantic schema to extract ContractAST."""
        if not self.client:
            raise ValueError(
                "Gemini API Key is not set! Please provide your API key in the app or .env file, "
                "or switch to 'Instant Offline Demo' mode."
            )

        from google.genai import types

        prompt = f"Extract all financial covenants, variables, and legal invariants from the following legal contract text:\n\n{contract_text}"

        for attempt in range(max_retries):
            try:
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=EXTRACTION_SYSTEM_INSTRUCTION,
                        response_mime_type="application/json",
                        response_schema=ContractAST,
                        temperature=0.1
                    )
                )

                parsed_json = json.loads(response.text)
                return ContractAST(**parsed_json)

            except Exception as e:
                err_msg = str(e)
                if "429" in err_msg or "ResourceExhausted" in err_msg:
                    wait_time = (attempt + 1) * 3
                    print(f"[NeuralExtractor] Rate limit hit (429). Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    raise RuntimeError(f"Gemini API extraction failed: {err_msg}")

        raise RuntimeError("Max retries exceeded due to rate limits. Try again in 60 seconds or use Offline Demo mode.")

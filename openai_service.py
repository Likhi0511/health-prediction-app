from openai import OpenAI
from dotenv import load_dotenv

import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_remark(
    glucose,
    haemoglobin,
    cholesterol
):

    prompt = f"""
    Patient Blood Test Results

    Glucose: {glucose}

    Haemoglobin: {haemoglobin}

    Cholesterol: {cholesterol}
"""
    return prompt
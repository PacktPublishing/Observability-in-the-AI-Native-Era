from deepeval import assert_test
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import GEval
import os
from deepeval.models import OllamaModel
from deepeval.metrics import AnswerRelevancyMetric

model = OllamaModel(
    model="tinyllama",
    base_url="http://localhost:11434",
    temperature=0
)

def output():
    with open('askingdeepseektocountr.txt','r') as actual_output:
        actual_output= actual_output.read()
        return(actual_output)
    
def test_correctness():
    correctness_metric = GEval(
        name="Correctness",
        model=model,
        criteria="Determine if the 'actual output' is correct based on the 'expected output'.",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        threshold=0.5
    )
    test_case = LLMTestCase(
        input= "How many times does the letter R appear in the word strawberry?",
        # Replace this with the actual output from your LLM application
        actual_output = output(),
        expected_output="The letter R appears 3 times in the word strawberry."
    )
    assert_test(test_case, [correctness_metric])
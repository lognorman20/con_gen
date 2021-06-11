from aitextgen import aitextgen

# these lines are for mac users. comment out if not mac
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# generating predictions
def generate(user_input) -> str:
    # loading in model
    ai = aitextgen(model_folder="models/trained_model", to_gpu=False)
    return ai.generate_one(nonempty_output=False, prompt=user_input, min_length=100, temperature=0.6, top_p=0.9)

print(generate("I am starting to believe aliens"))
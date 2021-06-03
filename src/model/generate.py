from aitextgen import aitextgen

# for mac users like me, comment the two lines below out if not mac
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# loading in model
ai = aitextgen(model_folder="/Users/logno/Documents/GitHub/conspiracy_generation/models/trained_model", to_gpu=False)

# generating predictions
def generate(user_input) -> str:
    return ai.generate_one(nonempty_output=False, prompt=user_input, min_length=100, temperature=1.0, top_p=0.9)

print(generate("The moon landing is"))
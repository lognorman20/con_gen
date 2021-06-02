import logging
logging.basicConfig(
        format="%(asctime)s — %(levelname)s — %(name)s — %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        level=logging.INFO
    )

from aitextgen import aitextgen

ai = aitextgen(tf_gpt2="124M", to_gpu=True)

file_name = "/Users/logno/Documents/GitHub/conspiracy_generation/data/processed/corpus.txt"

ai.train(file_name,
         line_by_line=False,
         from_cache=False,
         num_steps=2,
         generate_every=1000,
         save_every=1000,
         save_gdrive=False,
         learning_rate=1e-3,
         fp16=False,
         batch_size=1, 
         )

ai.save()
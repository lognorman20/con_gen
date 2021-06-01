import gpt_2_simple as gpt2

# downloading model
gpt2.download_gpt2(model_name="124M")

file_name = "/Users/logno/Documents/GitHub/conspiracy_generation/data/interim/corpus.txt"

# train model on corpus
sess = gpt2.start_tf_sess()

gpt2.finetune(sess,
              dataset=file_name,
              model_name='124M',
              steps=200,
              restore_from='fresh',
              run_name='run1',
              print_every=10,
              sample_every=100,
              )
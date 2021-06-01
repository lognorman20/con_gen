import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name="run1", checkpoint_dir='/Users/logno/Documents/GitHub/conspiracy_generation/models/checkpoint/',
model_dir='/Users/logno/Documents/GitHub/conspiracy_generation/models/', multi_gpu=False)

text = gpt2.generate(sess,
              length=50,
              temperature=0.9,
              top_p=0.9,
              prefix="The moon landing is fake because",
              nsamples=3,
              truncate='<|endoftext|>'
              )

print(text)
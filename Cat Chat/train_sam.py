import gpt_2_simple as gpt2
import tensorflow as tf
tf.compat.v1.reset_default_graph()
sess = gpt2.start_tf_sess()
# gpt2.download_gpt2(model_name="355M")
# dir_name = "data"
# gpt2.encode_dataset(dir_name)
file_name = "text_encoded.npz"
gpt2.finetune(sess,
              dataset=file_name,
              model_name='124M',
              steps=138000,
              restore_from='latest',
              run_name='run1',
              print_every=100,
              sample_every=1000,
              sample_length=128,
              only_train_transformer_layers = True,
              accumulate_gradients = 1)

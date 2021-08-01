import tensorflow as tf
import numpy as np
from bert import modeling,optimization,tokenization
 
config_path = './bert/chinese_L-12_H-768_A-12/bert_config.json'
checkpoint_path = './bert/chinese_L-12_H-768_A-12/bert_model.ckpt'
dict_path = './bert/chinese_L-12_H-768_A-12/vocab.txt'
bert_config = modeling.BertConfig.from_json_file(config_path)
tokenizer = tokenization.FullTokenizer(vocab_file=dict_path,do_lower_case=False)
 
testText = '我想听周杰伦的稻香'
 
tokens = tokenizer.tokenize(testText)
tokens = ['[CLS]']+tokens+['[SEP]']
input_ids = tokenizer.convert_tokens_to_ids(tokens)
 
print(tokens)
print(input_ids)
 
input_mask = [1]*len(input_ids)
segment_ids = [0]*len(input_ids)
 
print(tokens)
print(input_ids)
print(input_mask)
 
maxLen = 128
while len(input_ids) < maxLen:
    input_ids.append(0)
    input_mask.append(0)
    segment_ids.append(0)
 
assert len(input_ids) == maxLen
assert len(segment_ids) == maxLen
assert len(input_mask) == maxLen
 
input_ids = np.reshape(np.array(input_ids),(1,-1))
input_mask = np.reshape(np.array(input_mask),(1,-1))
segment_ids = np.reshape(np.array(segment_ids),(1,-1))
 
 
input_ids_p=tf.placeholder(shape=[None,None],dtype=tf.int32,name="input_ids_p")
input_mask_p=tf.placeholder(shape=[None,None],dtype=tf.int32,name="input_mask_p")
segment_ids_p=tf.placeholder(shape=[None,None],dtype=tf.int32,name="segment_ids_p")
 
model = modeling.BertModel(config=bert_config,
                           is_training=False,
                           input_ids=input_ids_p,
                           input_mask=input_mask_p,
                           token_type_ids=segment_ids_p,
                           use_one_hot_embeddings=False)
output = model.get_sequence_output()
dense_to_100 = tf.layers.dense(output,100,name='dense_to_100')
 
 
# saver = tf.train.Saver()
tvars = tf.trainable_variables()
(assignment_map, initialized_variable_names) = modeling.get_assignment_map_from_checkpoint(tvars, checkpoint_path)
tf.train.init_from_checkpoint(checkpoint_path, assignment_map)
 
with tf.Session() as sess:
    # sess.run(tf.variables_ini/tializer(tf.global_variables()))
    sess.run(tf.global_variables_initializer())
    # saver.restore(sess,save_path=checkpoint_path)
    print(sess.run(output,feed_dict={
        input_ids_p: input_ids,
        input_mask_p: input_mask,
        segment_ids_p: segment_ids
    }))
    print(sess.run(tf.shape(dense_to_100),feed_dict={
        input_ids_p: input_ids,
        input_mask_p: input_mask,
        segment_ids_p: segment_ids
    }))


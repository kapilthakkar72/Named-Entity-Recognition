# Named-Entity-Recognition

To Run Mallet CRF:

java -cp "/home/surbhi/Desktop/Named-Entity-Recognition/mallet-2.0.8RC3/class:/home/surbhi/Desktop/Named-Entity-Recognition/mallet-2.0.8RC3/lib/mallet-deps.jar" cc.mallet.fst.SimpleTagger --train true --test lab --threads 8 --model-file /home/surbhi/Desktop/Named-Entity-Recognition/nercrf a2_train.txt

This will create "nercrf" file, which can be used for prediction.

java -cp "/home/surbhi/Desktop/Named-Entity-Recognition/mallet-2.0.8RC3/class:/home/surbhi/Desktop/Named-Entity-Recognition/mallet-2.0.8RC3/lib/mallet-deps.jar" cc.mallet.fst.SimpleTagger --model-file /home/surbhi/Desktop/Named-Entity-Recognition/nercrf a2_test.txt > ner_op.txt

--------------------------------------------------------------------------------
##########            File Details:                                  ###########
--------------------------------------------------------------------------------

1. A2.pdf : Problem Statement

2. a2_train_full.txt : Total tagged data available for NER. Which is divided into 2 parts, as follows:

2a. a2_train.txt : 80 % of total tagged data available for NER

2b. a2_test.txt : 20 % of total tagged data available for NER (without label) and their label is available in a2_test_gold.txt

3. accuracy_check.py : To check accuracy of NER tagger

4. format_checker.py : to check whether op generated is in required format or not

5. mallet-tutorial.pdf : name is self-explanatory

6. tokens_to_tweet.py : Given tweets are in token format. For POS tasks and other it needs to be converted into tweets. This file does that.

7. unlabelled_tweets : corpora of unlabelled tweets.

8. helper_files/N.json : corpora of unlabelled tweets

9. helper_files/jsonToText.py : python file to convert json to text of above J.json file

10. helper_files/remove_labels.py: python file to remove labels from tagged data. (Used while separating training and testing data)

# Preprocess it to convert it to conll format
echo "Converting to conll format for input"
python preprocess_conll_format.py $1 > conll_ip
echo "done"
# Run POS on top of that
echo "Running POS tagger"
./runTagger.sh --output-format conll --input-format conll --no-confidence conll_ip > test_with_pos
echo "Done"
# Removing tabs
python remove_space.py test_with_pos > test_with_pos_updated
# Finally produce output
echo "Running NER"
java -cp "/home/surbhi/Desktop/Named-Entity-Recognition/mallet-2.0.8RC3/class:/home/surbhi/Desktop/Named-Entity-Recognition/mallet-2.0.8RC3/lib/mallet-deps.jar" cc.mallet.fst.SimpleTagger --model-file /home/surbhi/Desktop/Named-Entity-Recognition/nercrf test_with_pos_updated > ner_op.txt
echo "Done"
# Map output to tweets
echo "Mapping tweets to output"
python mapping_nerop_tweets.py $1 ner_op.txt > $2
echo "Done"
# Run format checker for that
echo "Running format checker"
python format_checker.py $1 $2
echo "Done"
# Running accuracy test
echo "calculating Accuracy"
python accuracy_check.py $2 a2_test_gold.txt
echo "Calculating F-score"
python Fscore_ner.py $2 a2_test_gold.txt
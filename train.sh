# First Remove labels
echo "Removing labels"
python remove_labels.py a2_train.txt labels > withoutLabel
echo "Done"
# Run POS Tagger on given Tweets
# For that first convert input to conll format : $1 is input file
echo "conll format"
python preprocess_conll_format.py withoutLabel > conll_ip.txt
echo "Done"
# Run POS on top of that
echo "pos tagger"
./runTagger.sh --output-format conll --input-format conll --no-confidence conll_ip.txt > train_with_pos
echo "Done"
# Removing tabs
python remove_space.py train_with_pos > train_with_pos_updated
# Append Labels to file
echo "appending labels"
python append_labels.py train_with_pos_updated labels > training_file
echo "Done"
# Finally Train it
echo "training"
java -cp "/home/surbhi/Desktop/Named-Entity-Recognition/mallet-2.0.8RC3/class:/home/surbhi/Desktop/Named-Entity-Recognition/mallet-2.0.8RC3/lib/mallet-deps.jar" cc.mallet.fst.SimpleTagger --train true --iterations 50 --test lab --threads 8 --model-file /home/surbhi/Desktop/Named-Entity-Recognition/nercrf training_file
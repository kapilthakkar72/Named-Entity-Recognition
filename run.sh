# Convert tokens to tweets
python tokens_to_tweet.py $1 > tweets.txt
# Run POS on top of that
./runTagger.sh --output-format conll tweets.txt > pos_op.txt
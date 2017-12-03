file="submission.zip"

if [ -f $file ] ; then
    rm $file
fi

zip submission.zip MyBot.py hlt/

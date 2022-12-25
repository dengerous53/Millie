if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Millie-bobby/Millie /Millie 
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Millie 
fi
cd /Millie 
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 millie.py

echo "copying your bot data ...."
git clone https://github.com/Renishrplay/Millie-1.git /Millie
cd /Millie
echo "installing some packages..."
pip3 install -U -r requirements.txt
echo "Starting Bot...."
echo "MILLIE DEPLOYED SUCCESSFULLY"
python3 millie.py

tell application "Terminal"
	activate
  do script "sudo easy_install pip" in window 1
  do script "pip install -r requirements.txt" in window 1
	do script "physics.py" in window 1
end tell

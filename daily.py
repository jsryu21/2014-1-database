import os
import time

def execute():
	os.system("python player.py")
	os.system("python team.py")
	os.system("python game.py")
	now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
	os.system("python match.py 1 > result_" + now + ".tab")
	os.system("python match.py 1 orange > result_orange_" + now + ".tab")

if __name__ == "__main__":
	execute()

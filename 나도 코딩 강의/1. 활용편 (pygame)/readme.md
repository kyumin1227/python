pipx 를 사용하여 독립된 파이썬 인터프리터를 설치 하였음

패키지로는 pygame만 설치하였으며

vscode의 인터프리터 설정은 아마 한글 폴더에 띄어쓰기 때문에 제대로 지정이 되지 않는것 같음

vscode에서 자동완성을 쓰기 위해 해당 인터프리터(myenv/bin/activate) 설정을 하기 위해서는 해당 폴더를 여는 방법 밖에 못찾음

.vscode/setting.json 에 해당 프로젝트의 기본 파이썬 언어를 "../myenv/bin/python"로 설정 해두었음

명령어 모음

which python - 현재 터미널에서 실행중인 파이썬의 경로를 보여줌
pip3 list - 해당 인터프리터에 설치된 패키지를 보여줌
pipx list - 해당 인터프리터에 설치된 어플리케이션(장고, tkinter, pandas 등)을 보여줌

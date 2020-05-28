# Git 정리

## Git scm 명령어

### 명령어
1. 'git init'
> - 새로운 Git저장소를 생성, 현재 디렉토리(소스 파일이 있는 폴더)를 GitHub로 다운로드, 업로드 하기 위해 초기화(지정)한다.

2. 'git remote add 저장소명 url'
> - Git init로 지정한 디렉토리를 Git 서버와 연결합니다.

3. 'git add *'
> - 현재 디렉토리에 있는 모든 파일과 폴더를 git에게 알려줍니다.
> - Remote로 연결이 되어있지만 Git은 파일 및 폴더를 모르고 있습니다.
> - 매번 폴더/파일이 추가 및 수정을 하실 때마다 쓰셔야합니다.
> - 특정 파일만 올릴 경우 '\*' 을 파일 이름으로 지정하시면 됩니다.

4. 'git commit -m "메세지 내용"'
> - Add로 알려진 파일 및 폴더에 코멘트를 남깁니다.
> - 코멘트는 Github 사이트에 들어가시면 [파일 이름, Commit, 업로드] 로 가운데에 표기됩니다.

5. 'git push -u 저장소명 master'
> - 연결한 저장소명으로 파일을 업로드 합니다.
> - master는 branch이며 Create new repository 로 생성했으면 기본적으로 가지고 있는 이름입니다.
> - 윗 명령줄을 쓴 다음 부터는 `git push`로  생략하여 바로 업로드 가능합니다.
> - 만약 본인이 생성하지 않는 저장소에 업로드 할려면 해당 저장소에 연결을 한 후에 branch를 생성하여 master 대신 쓰면됩니다.
> - 윗 줄의 상세한 내용은 추 후 추가 예정

6. 'git pull'
> - Git 저장소에 있는 폴더 및 파일을 다운로드 합니다.
> - 컴퓨터에서 작업 한 후에 다른 컴퓨터에서 작업을 할려고 할 때 쓰입니다.
> - push와 함께 자주쓰일 명령어입니다.

7. 'git clone url'
> - url 주소를 현재 디렉토리에 다운로드 생성합니다.
> - git init를 할 필요가 없습니다. 이미 .git도 같이 생성됩니다.

8. 순서
> - 초기 순서
> - git init -> git remote -> git add -> git commit -> git push
> > - 후에 pull과 add -> commit -> push 반복 
> - 다른 컴퓨터에서의 작업할 때
> - git clone -> git add -> git commit -> git push
> > - 후에 pull과 add -> commit -> push 반복 


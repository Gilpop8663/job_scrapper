1.검색창에 영어만 칠 수 있게 자바스크립트 설정했습니다.
스택오버플로우에는 한글로 검색을 하면 검색 결과가 없어 오류가 나는 것을 방지하였습니다.

2.Flask 를 이용해 로그인 기능을 만들었습니다.
직업 검색에 의미가 있진 않지만 사이트에 애정을 담아서 연습하는 겸 만들어 보았습니다.

3.원하는 사이트 별로 혹은 모든 사이트의 검색 결과를 볼 수 있습니다.
input type="checkbox"를 통해 어떤 사이트에서 검색할지 site란 name으로 args로 보내주어 사이트별로 검색할 수 있게 하였고 db [word+site] = jobs를 통해 데이터베이스 또한 각각 관리해 주었습니다. 그리고 checkbox를 한 개씩 설정할 수 있도록 자바스크립트로 설정해주었습니다.

4.검색 결과에 회사의 로고 이미지를 볼 수 있습니다.
검색 결과에 회사의 SO 사이트에만 있는 회사 이미지를 보내주었고 Indeed 사이트에는 회사 이미지가 없어서 투명 PNG 이미지를 보내주었습니다.

5.python random 모듈을 이용해서 랜덤 rgb, 랜덤 좋아요 숫자, 랜덤 조회수를 보내주었습니다.
python에서 색도 랜덤으로 보낼 수 있나 했는데 random 모듈을 통해서 해결이 가능했고 좀 더 실제 같은 사이트를 만들기 위해 다른 요소들을 랜덤 값으로 보내주었습니다.

6.로딩 진행 상황을 사용자에게 알려주었습니다.
검색을 하다 보면 처음 사이트를 이용하는 사용자에게는 검색되고 있는 중인지 헷갈릴 것 같아 로딩 창을 구현해야겠다고 생각하게 되었습니다. 구현 방법은 setInterval을 이용해 진짜 진행상황이 아닌 가짜 진행 상황을 보여주었습니다.
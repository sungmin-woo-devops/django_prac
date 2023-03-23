Page Not Found (404) 에러는 클라이언트가 요청한 페이지를 찾을 수 없을 때 발생하는 오류이다.

장고는 클라이언트가 웹 브라우저에 /pybo/ 라는 페이지를 요청하면 해당 페이지를 가져오는 URL 매핑이 있는지 config/urls.py 파일을 뒤져 찾아본다.

그런데 아직 /pybo/ 페이지에 해당하는 URL 매칭을 장고에 등록하지 않았다. 그래서 장고는 /pybo/ 페이지를 찾을 수 없다는 에러를 띄우는 것이다.

---

비유를 들어 이 상황을 생각해보자면 이렇다. 편의점에서 제로 콜라 있어요? 라고 고객이 점원에게 물었는데, 제로 콜라가 없는 상황인 것이다. (요청한 물건이 없네요...)

---

그렇다면 어떻게 해결할 수 있을까? 장고가 사용자의 페이지 요청을 이해할 수 있도록 config/urls.py에 /pybo/ 파일을 수정한다.

---

- config.urls.py는 페이지 요청 시 가장 먼저 호출되며, 요청 URL과 뷰 함수를 1:1로 연결해준다.
- 뷰 함수란 views.py 파일 내 정의된 함수로 화면을 보여주기 위한 용도로 사용된다.


#Django
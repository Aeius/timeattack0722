# timeattack0722

문제풀때 다음 가입된 candidate 계정 정보를 사용하세요. candidate1@test.com // 12345678 

admin 계정은 david@test.com // 1234

1. 지원자가 지원한 `지원서 상태`를 저장할 수 있도록 모델을 추가해보세요.

2. admin 또는 장고쉘/SQL으로 1번에서 작성한 모델에 다음 상태값을 추가해보세요.
(`writing`, `submitted`, `under review`, `interview planned`, `in recruitment progress`)

3. 지난 타임어택에서 어떤 채용공고에 지원했는지를 저장하기 위한 JobPostActivity 모델에서 지원한 상태를 가지도록 1번에서 추가한 모델과 관계를 지어 보세요.

4. post/views.py : ApplyView, post 메소드를 호출할때, 즉 지원할 때 제출했다(submitted)는 초기상태를 저장하도록 수정해보세요.

5. status에 따라서 필터링하는 GET메소드를 구현해보세요.

candidate1@test.com 계정으로 로그인 후에 JWT 토큰을 사용해서 다음과 같이 요청해서 테스트해보세요.

6. 채용담당자가 채용진행 상황(interviewed, accepted, offer in progress)등을 남길수 있도록 모델을 추가해보세요.

7. 채용담당자가 채용진행 상황을 변경한 로그를 저장할 수 있도록 모델을 추가해보고 JobPostActivity과 관계를 지어 보세요.

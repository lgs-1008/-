나이스에서 급식정보를 크롤링 해온 후 restframework를 이용하여 api로 뿌려주는것입니다.
celery를 이용하여 매달 1일 자동으로 크롤링 해오도록 추가할 예정입니다.(미완)
JWT를 사용하여 보안을 적용시킬 예정입니다. 로컬에서 테스트중입니다.(미완)
AWS를 활용하였습니다.
링크 : 
ec2-13-125-249-182.ap-northeast-2.compute.amazonaws.com:8080/

날짜가 pk입니다. 
http://ec2-13-125-249-182.ap-northeast-2.compute.amazonaws.com:8080/mealdatas/20191216
이런식으로 필터링 조회 가능합니다.

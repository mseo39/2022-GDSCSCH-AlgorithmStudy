#신규 아이디 추천 = 규칙에 맞는 아이디 추천
"""
카카오에 입사한 신입 개발자 네오는 "카카오계정개발팀"에 배치되어, 카카오 서비스에 가입하는 유저들의 아이디를 생성하는 업무를 담당하게 되었습니다. 
"네오"에게 주어진 첫 업무는 새로 가입하는 유저들이 카카오 아이디 규칙에 맞지 않는 아이디를 입력했을 때, 
입력된 아이디와 유사하면서 규칙에 맞는 아이디를 추천해주는 프로그램을 개발하는 것입니다.
다음은 카카오 아이디의 규칙입니다.

1. 아이디의 길이는 3자이상 15자 이하
2. 아이디는 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 문자만 사용할 수 있음
3. 단, 마침표는 처음과 끝에 시용할 수 없으며 또한 연속으로 사용할 수 없음

"네오"는 다음과 같이 7단계의 순차적인 처리 과정을 통해 
신규 유저가 입력한 아이디가 카카오 아이디 규칙에 맞는 지 검사하고 
규칙에 맞지 않은 경우 규칙에 맞는 새로운 아이디를 추천해 주려고 합니다.
검사> 맞지 않은 경우 추천

단계
1. 대문자를 소문자로

2. 알파벳, 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자를 제거

3. 마침표가 2번 연속으로 있으면 하나의 마침표로 치환
4. 마침표가 처음과 끝에 있다면 제거
5. 만약 빈 문자열이라면 a를 대입
6. 길이가 16자 이상이면 처음 15문자를 제외한 나머지를 제거_ 제거 후 마침표가 마지막에 존재한다면 마침표를 제거
7. 길이가 2이하라면 마지막문자를 길이가 3이 될때까지 반복합니다
"""
def solution(new_id):
    # 1번 대문자를 소문자로 변경
    new_id=new_id.lower()
    # 2번
    new_id="".join([i for i in new_id if i not in "~!@#$%^&*()=+[{]}:?,<>/"])
    # 3번, 4번
    new_id=".".join([i for i in new_id.split(".") if i!=""])
    #문자열 길이 검사
    # 5번
    if not len(new_id):# 빈문자열이라면
        new_id="a" #a를 대입
    # 6번
    if len(new_id)>15: # 16이상이라면
        new_id=new_id[:15] #처음부터 15자까지의 문자만 가져옴
    # 7번
    if len(new_id)<=2: # 2이하라면
        new_id+=new_id[-1]*(3-len(new_id)) #마지막 문자를 3이될때까지 반복
    #정리
    if new_id[0]==".":
        new_id=new_id[1:]
    if new_id[-1]==".":
        new_id=new_id[:-1]
    return new_id

print(solution("abcdefghijklmn.p"))
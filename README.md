# SERVER API

## 회원관리
<br>

|아이디 중복체크||
|:-----------|---|
|HTTP Method|POST|
|요청 url|/id_overlap|
|Request Parameters|<table><tr> <th>Name</th>    <th>Type</th>    <th>Madatory</th>  </tr>  <tr>    <td>user_id</td>    <td>string</td>    <td>O</td> </tr></table>|
|Respone Body|{<br>“code” : “0000”,<br>“mag” : “중복 없음”<br>}|
|code|<li>0000 - 중복업음</li><li>1001 - 아이디 중복</li>|
---
<br></br>
|회원가입||
|:-----------|---|
|HTTP Method|POST|
|요청 url|/signup|
|Request Parameters|<table><tr> <th>Name</th>    <th>Type</th>    <th>Madatory</th>  </tr>  <tr>    <td>user_id</td>    <td>string</td>    <td>O</td> </tr></tr>  <tr>    <td>user_password1</td>    <td>string</td>    <td>O</td> </tr></tr>  <tr>    <td>user_password2</td>    <td>string</td>    <td>O</td> </tr></table>|
|Respone Body|{<br>“code” : “0000”,<br>“mag” : “가입 성공”<br>}|
|code|<li>0000 - 가입성공</li><li>1001 - 비밀번호 확인</li>|
---
<br></br>
|로그인||
|:-----------|---|
|HTTP Method|POST|
|요청 url|/login|
|Request Parameters|<table><tr> <th>Name</th>    <th>Type</th>    <th>Madatory</th>  </tr>  <tr>    <td>user_id</td>    <td>string</td>    <td>O</td> </tr></tr>  <tr>    <td>user_password</td>    <td>string</td>    <td>O</td> </tr></table>|
|Respone Body|{<br>“code” : “0000”,<br>“mag” : “로그인 성공”<br>}|
|code|<li>0000 - 로그인 성공</li><li>1001 - 로그인 실패</li>|
---
<br></br>
|회원목록 조회||
|:-----------|---|
|HTTP Method|POST|
|요청 url|/user_list|
|Request Parameters|<table><tr> <th>Name</th>    <th>Type</th>    <th>Madatory</th>  </tr>  <tr>    <td></td>    <td></td>    <td></td> </tr></tr>  <tr>    </table>|
|Respone Body|{<br>“username” : id,<br>“password” : encrypted password<br>}|
---
<br></br>
|다음 웹툰||
|:-----------|---|
|HTTP Method|POST|
|요청 url|/daumwebtoon|
|Request Parameters|<table><tr> <th>Name</th>    <th>Type</th>    <th>Madatory</th>  </tr>  <tr>    <td>date</td>    <td>string</td>    <td>O</td> </tr></table><br>ex ) 2021-01-07|
|Respone Body|{<br>“name” : name,<br>“url” : webtoon url,<br>“image” : image url<br>}|
---
<br></br>
|네이버 웹툰||
|:-----------|---|
|HTTP Method|POST|
|요청 url|/naverwebtoon|
|Request Parameters|<table><tr> <th>Name</th>    <th>Type</th>    <th>Madatory</th>  </tr>  <tr>    <td>date</td>    <td>string</td>    <td>O</td> </tr></table><br>ex ) 2021-01-07|
|Respone Body|{<br>“name” : name,<br>“url” : webtoon url,<br>“image” : image url<br>}|
---

<br></br>
|네이버 뉴스||
|:-----------|---|
|HTTP Method|POST|
|요청 url|/navernews|
|Request Parameters|<table><tr> <th>Name</th>    <th>Type</th>    <th>Madatory</th>  </tr>  <tr>    <td>date</td>    <td>string</td>    <td>O</td> </tr></table><br>ex ) 2021-01-07|
|Respone Body|{<br>“name” : name,<br>“url” : news url,<br>“image” : image url<br>}|
---

<br></br>
|사용자 기록||
|:-----------|---|
|HTTP Method|POST|
|요청 url|/history|
|Request Parameters|<table><tr> <th>Name</th>    <th>Type</th>    <th>Madatory</th>  </tr>  <tr>    <td>user_id</td>    <td>string</td>    <td>O</td> <tr>    <td>content_type</td>    <td>string</td>    <td>O</td> <tr>    <td>content_number</td>    <td>string</td>    <td>O</td>  </tr> </tr> </tr></table><br>ex ) user2021, youtube, 110|
|Respone Body|{<br>“code” : “0000”,<br>“mag” : “데이터 전송 성공”<br>}|
|code|<li>0000 - 데이터 전송 성공</li><li>1001 - 데이터 전송 성공</li>|
---
|유튜브||
|:-----------|---|
|HTTP Method|POST|
|요청 url|/youtube|
|Request Parameters|<table><tr> <th>Name</th>    <th>Type</th>    <th>Madatory</th>  </tr>  <tr>    <td>date</td>    <td>string</td>    <td>O</td> </tr></table><br>ex ) 2021-01-07|
|Respone Body|{<br>“name” : name,<br>“url” : news url,<br>“image” : image url<br>"category":category<br>}|
---

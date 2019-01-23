# Homework_11

1. 다음은 부트스트랩의 어떤 component 이며 아래와 같이 만들려면 어떤 class 를 주어야
   하는가.

![image](https://user-images.githubusercontent.com/30791915/51573828-47f81080-1eee-11e9-9779-10e15c2a21e6.png)

```
Component: Button
class: btn-danger
```
``` html
ex)
<button type="button" class="btn btn-danger">Danger</button>
```



2. 다음은 부트스트랩의 어떤 component인가? 아래와 동일하게 만들어 보시오.  
![image](https://user-images.githubusercontent.com/30791915/51574420-09178a00-1ef1-11e9-8ee6-f51d7ae14f84.png)


```
Component: Alert
```
``` html
<div class="alert alert-info" role="alert">
  Hello SSAFY ?!
</div>
```



3. 다음 빈칸을 채우시오.  
```
“부트스트랩 그리드 시스템은 레이아웃을 ( 12 )개의 column 으로, ( 5 )개의 반응형 사이즈 조건을 사용하여 구축한다.”   
```


4. 아래와 같은 분할을 grid system을 활용하여 만들어 보시오.  

![image](https://user-images.githubusercontent.com/30791915/51574518-762b1f80-1ef1-11e9-83e3-568a7b968d11.png)
![image](https://user-images.githubusercontent.com/30791915/51574521-7c210080-1ef1-11e9-9f66-7db5ea879a9b.png)


``` html
<div class="container">
        <!-- row 생성 -->
        <div class="row">
            <div class="col-3">
                25%
            </div>
            <div class="col-6">
                50%
            </div>
            <div class="col-3">
                25%
            </div>
        </div>
    </div>
```
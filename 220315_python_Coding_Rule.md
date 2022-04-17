Index  

* Anaconda & Jupyter notebook  
1. [가상환경](#가상환경)  
2. [주피터 노트북 화면 font](#주피터 노트북-화면-font)
3. [가상환경Backup/복원](#아나콘다-가상환경-backup/복원)  
4. 

</br>  


* Python  
1. [Array](#Array)  
2. [Image 처리](#Image-save-&-call)  
3. 

</br>

---  

### 아나콘다-주피터노트북  
#### 가상환경  

* 리스트 확인  

    ```  
    conda info --envs  
    ```  
  
* 주피터 노트북 화면 font  

    ```  
    jt -t onedork -T -N -kl -f roboto -fs 9 -tfs 9 -nfs 9 -tfs 9 -ofs 8 -cellw 100% -lineh 150 -cursc r -cursw 2
    ```  
 

### 아나콘다-가상환경 backup/복원
 - 가상환경 export
   : "conda env export > 파일명. yaml" 입력  
 
    ```  
    $ conda env export > D:\env_backup\py35.yml  
    ```  
   - 여기서 이 명령어를 시행하는 Prompt는 백업할 env의 프롬프트임.  
 
- 백업파일을 이용하여 가상환경 생성

    ```  
    $ conda env create --name py35 --file D:\env_backup\py35.yml  
    ```  


### Python

#### Array

- numpy.ndarray  
  - NumPy의 N차원 배열 객체(C의 array와 동일 개념)로, 하나의 데이터 타입만 넣을 수 있다(Python의 list와 차이점)  
  
</br>   

#### Image save & call 
* image 저장 및 호출  

    ```  
    import cv2
    
    img = cv2.imread("imgs/Lenna.png") # 이미지 불러오기
    cv2.imshow("Lenna", img) # 불러온 이미지를 Lenna라는 이름으로 창 표시
    cv2.waitKey() # 키보드 입력이 들어올 때까지 창을 유지
    cv2.destroyAllWindows() # 모든 윈도우 창을 제거  
    ```  
      
</br>    

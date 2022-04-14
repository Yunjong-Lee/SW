
- image 저장 및 호출  


    import cv2  

    img = cv2.imread("imgs/Lenna.png") # 이미지 불러오기  

    cv2.imshow("Lenna", img) # 불러온 이미지를 Lenna라는 이름으로 창 표시.  

    cv2.waitKey() # 키보드 입력이 들어올 때까지 창을 유지  
    cv2.destroyAllWindows() # 모든 윈도우 창을 제거  

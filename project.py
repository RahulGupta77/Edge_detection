import cv2 

def preprocessing(img):
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    blur_img = cv2.GaussianBlur(gray_img,(5,5),0)  
    
    return blur_img
    

def sobel(img):
    
    new_img = preprocessing(img)   
    
    output = cv2.Sobel(new_img,ddepth=cv2.CV_8U,dx=1,dy=1,ksize=5)
    
    return output 


def canny(img): 
    
    new_img = preprocessing(img)
    
    output = cv2.Canny(new_img,100,300)
    
    return output 



def main():
    
    img = cv2.imread("ball.jpeg")
    
    sobel_img = sobel(img)
    
    canny_img = canny(img)
    
    cv2.imshow("sobel_img", sobel_img)
    
    cv2.imshow("canny_img", canny_img )
        
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
    

    
if __name__ == "__main__":
    main()
    
    
    
    
    
